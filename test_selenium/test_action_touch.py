from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
import time


class TestTouch():
    def setup(self):
        option = Options()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele_search = self.driver.find_element_by_id('su')
        ele.send_keys('selenium测试')
        time.sleep(3)
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele, 0, 10000).perform()
