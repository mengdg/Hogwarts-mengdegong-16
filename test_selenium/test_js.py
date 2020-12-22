import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from test_selenium.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get('http://baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('selenium测试')
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        time.sleep(5)

        print(self.driver.execute_script('return document.title'))
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))

    def test_time(self):
        self.driver.get('https://www.12306.cn/index/')
        time.sleep(2)
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-31'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(5)
