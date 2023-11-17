from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options

class EdgeBrowser(Edge):
    def __init__(self) -> None:       
        return None
        
    @staticmethod    
    def __call__(arguments: list = ['--start-maximized'])-> webdriver:
        option = Options()
        for argument in arguments:
            option.add_argument(argument)
        return Edge(options=option)