from datetime import datetime
from time import sleep
import os
import re

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .browserFactory import BrowserFactory
from .consts import CEPS
from .logger import LoggerClass

class SCRAPER(LoggerClass):
    def __init__(self,
                 SHIP: bool = False, 
                 WebDriver: str = 'Chrome',
                 Options: list = ['--start-maximized'],
                 Wait: int = 5,
                 Log_file: str ='debug.log', 
                 Log_level: str ='INFO'
                 ) -> None:
        
        super().__init__(Log_file, Log_level)

        self.driver = BrowserFactory()(webdriver=WebDriver, arguments=Options)
        self.wait = WebDriverWait(self.driver, Wait)
        self.ship = SHIP
        self.product_price = [] 
        if self.ship:
            self.ship_price = []
  
    def get_value(self, by: str = 'css selector', locator: str = None, value: str = None):
        try:
            text = self.driver.find_element(
                                            by, 
                                            locator
                                           ).text
            
            self.info(f'text collected: {text}')
             
            price = re.findall(r'(\d*\.?,?\d+,?\.?\d+)', text)[0]
            
            
            self.info(f'{value} price value collected: {price}')
            
        except NoSuchElementException:
            self.info(f'{value} price text not found')
            self.info(f'setting the price to None')            
            price = ''
        
        
        if value == 'PRODUCT':
            self.product_price.append(price)
        
        elif self.ship and value == 'SHIP':
            self.ship_price.append(price)

    def _get_quant(self, quant):
        try:
            quant_ = re.findall(r'\((\d+)\)', quant)[0]
        except:
            quant_ = '1'
        
        self.info(f'quantity to be set: {quant_}')
        
        return quant_

    def _get_cep(self, uf: str) -> str:
        cep = CEPS[uf]
        return cep

    def insert_value(
                    self, by: str = 'css selector', 
                    locator: str = None, insert: str = None, 
                    value: str = None, clear: bool = False, click: bool = False
                    ) -> None:

        if insert == 'CEP':
            value = self._get_cep(value)
        elif insert == 'QUANTIDADE':
            value = self._get_quant(value)
        try:
            sleep(0.5)
            element = self.driver.find_element(
                                              by,
                                              locator
                                              )
            if click:
                element.click()
            self.info('element located')
            
            if clear:
                element.send_keys(Keys.CONTROL + 'A')
            
            element.send_keys(value)
            self.info(f'send value: {value}')
            sleep(0.5)
        
        except Exception as e:
            self.info(f'error at insert {insert}')
            self.error(f'ERROR {e}')

    def select_packing(self, by: str= 'css selector', 
                       locator: str= None, dict_spcs: list = [...]
                       ) -> None:
        try:
            elements = self.driver.find_elements(
                                                by, locator
                                                )
            for element in elements:
                if element.text in dict_spcs:
                    element.click()
                else:
                    pass
        except Exception as e:
            self.info('error at select packing')
            self.error(e)

    def click(
             self, 
             by: str = 'css selector', 
             locator: str = None, 
             click: str = None,
             SUBMIT: bool = False,
             ) -> bool:

        try:
            if SUBMIT:
                self.wait.until(EC.element_to_be_clickable(
                    (by, locator))).submit()
            else:
                self.wait.until(EC.visibility_of_element_located(
                    (by, locator))).click()
            return True
        
        except Exception as e:
            self.info(f'error clicking in {click}')
            self.error(e)
            return False

    def get_screenshot(self, inform_cod: str, zoom_size: int = 1, folder_prints: str = 'prints') -> None:
        try:
            dir_path = os.path.abspath(
                folder_prints) + f"\\{inform_cod}_{datetime.now().strftime('%d_%m_%Y')}.png"
            
            self.driver.execute_script(f"document.body.style.zoom={zoom_size}")
            self.driver.save_screenshot(dir_path)
            self.driver.execute_script("document.body.style.zoom=1")
            
            self.info(f'screenshot path: {dir_path}')
        except Exception as e:
            self.info('erro at get_screenshot')
            self.error(e)
            
    def go_url(self, url: str, APPEND: bool = True) -> bool:
        try:
            self.driver.get(url=url)
            self.info(f'Requested url: {url}')    
            return False
        
        except Exception as e:
            self.info('error at go url')
            self.error(e)
            if APPEND:
                self.product_price.append('')
                if self.ship:
                    self.ship_price.append('')
            
            return True

    def generate_cargo(self, sheet: pd.DataFrame) -> pd.DataFrame:
        sheet['preco_coleta'] = self.product_price
        if self.ship:
            sheet['frete_coleta'] = self.ship_price

        return sheet

    def scroll(self, Page: str, qtd: int = 1):
        scroll: dict = {
            'DOWN': Keys.PAGE_DOWN,
            'UP': Keys.PAGE_UP
        }
        for _ in range(qtd):
            self.driver.find_element(
                                    by= 'xpath', 
                                    value= "//html"
                                    ).send_keys(scroll[Page])
