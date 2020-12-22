import pytest
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_open(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_link_text('社团').click()

        # def wait(x):
        #     return len(self.driver.find_elements_by_link_text('求职面试圈1')) >= 1
        #
        # WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, '求职面试圈')))
        self.driver.find_element_by_link_text('求职面试圈').click()
        sleep(5)
