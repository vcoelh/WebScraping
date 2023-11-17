from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

class ChromeBrowser(Chrome):
    def __init__(self) -> None:
        return None       
    
    @staticmethod 
    def __call__(arguments: list = ['--start-maximized'])-> webdriver:
        option = Options() 
        for argument in arguments:
            option.add_argument(argument)
        return Chrome(options=option)