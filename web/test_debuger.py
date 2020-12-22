import time

import pytest
import yaml
from selenium import webdriver


class TestWework:
    # @pytest.mark.skip
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置debugger地址
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(executable_path='/Users/mengdegong/Desktop/Hogwarts/testpro0/driver/chromedriver',
                                  options=opt)
        driver.implicitly_wait(5)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        driver.find_element_by_id('menu_apps').click()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(driver.get_cookies(), f)
        print(driver.get_cookies())

    @pytest.mark.skip
    def test_cookie_login(self):
        driver = webdriver.Chrome(executable_path='/Users/mengdegong/Desktop/Hogwarts/testpro0/driver/chromedriver')
        driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('data.yaml', encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for c in yaml_data:
                driver.add_cookie(c)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        driver.find_element_by_id('menu_apps').click()
        time.sleep(5)
        driver.quit()
