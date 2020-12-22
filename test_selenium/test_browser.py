from test_selenium.base import Base
from selenium import webdriver
import os


class TestBrowser(Base):

    # 执行 browser=firefox pytest test_browser.py
    def test_browser(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'safari':
            self.driver = webdriver.Safari()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
