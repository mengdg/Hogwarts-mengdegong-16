import selenium
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
