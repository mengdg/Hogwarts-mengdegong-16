from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChain:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_open(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath('//input[3]')
        element_double_click = self.driver.find_element_by_xpath('//input[2]')
        element_right_click = self.driver.find_element_by_xpath('//input[4]')

        action = ActionChains(self.driver)
        # click
        action.click(element_click)
        # double click
        action.double_click(element_double_click)
        # right click
        action.context_click(element_right_click)
        time.sleep(4)
        # 开始
        action.perform()

    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(5)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        ele = self.driver.find_element_by_id('dragger')
        to_ele = self.driver.find_element_by_xpath('//div[2]')
        action = ActionChains(self.driver)
        # 第一种方式
        # action.drag_and_drop(ele, to_ele)
        # 第二种方式
        # action.click_and_hold(ele).release(to_ele)
        # 第三种方式
        action.click_and_hold(ele).move_to_element(to_ele).release()
        action.perform()
        time.sleep(5)

    def test_send_key(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('top').pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(3)
        action.perform()
