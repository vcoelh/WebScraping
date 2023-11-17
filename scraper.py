from datetime import datetime
import re

import pandas as pd
from tqdm import tqdm
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options

from utils.logger import LoggerClass

class BOOK(LoggerClass):

    def __init__(self, log_file='debug.log', log_level='INFO'):
        super().__init__(log_file, log_level)

        self.driver = self.start()
        
        self.dic = {
                    'names'       : [],
                    'prices'      : [],
                    'urls'        : [],
                    'availability': [],
                    }
        
 
 
    def start(self):
        option = Options()
        option.add_argument('headless')
        option.add_argument('start-maximized')
        driver = Edge(options=option)
        return driver
        
    def get_name(self):
        boxs  = self.driver.find_elements('css selector', '.product_pod a')
        names = [name.text for name in boxs]
        names = [name for name in names if name != '']
        return names
    
    def get_urls(self):
        text = self.driver.find_elements('css selector', '.product_pod a')
        urls = [url.get_attribute('href') for url in text]
        urls = list(dict.fromkeys(urls))
        return urls
    
    def get_prices(self):
        texts = self.driver.find_elements('css selector', '.price_color')
        prices = [re.findall(r'\d+\.?,?\d+', value.text)[0].replace('.', ',') for value in texts]
        return prices
    
    
    def get_availabilitys(self):
        texts = self.driver.find_elements('css selector', '.availability')
        availability  = [value.text for value in texts]
        return availability
    
    def scraper(self):

        for i in tqdm(range(1,51)):
            url = f'https://books.toscrape.com/catalogue/page-{i}.html'
            
            self.driver.get(url=url)
            names         = self.get_name()
            prices        = self.get_prices()
            urls          = self.get_urls()
            availabilitys = self.get_availabilitys()
            
            self.info(f'LEN NAMES COLLECTED: {len(names)}')
            self.info(f'LEN PRICES COLLECTED: {len(prices)}')
            self.info(f'LEN URLS COLLECTED: {len(urls)}')
            self.info(f'LEN AVAILABILITYS COLLECTED: {len(availabilitys)}')
            
            self.dic['names'].extend(names)
            self.dic['prices'].extend(prices)
            self.dic['urls'].extend(urls)
            self.dic['availability'].extend(availabilitys)
        
        self.driver.quit()
        df = pd.DataFrame(self.dic)
        df['Data'] = datetime.now().strftime('%d/%m/%Y')
        return df 
    