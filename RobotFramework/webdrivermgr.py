from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def chromedriver_path():

    return ChromeDriverManager().install()