import pytest
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_open(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text('求职面试圈').click()
        self.driver.find_element_by_css_selector('.topic-26766 .title > a').click()
        sleep(5)
