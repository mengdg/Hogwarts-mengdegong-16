from test_selenium.base import Base
from selenium.webdriver.common.by import By

import time


class TestWindows(Base):
    def test_window(self):
        self.driver.get('https://wwww.baidu.com')
        self.driver.find_element(By.LINK_TEXT, '登录').click()

        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('username')

        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('1060093716@qq.com')
        time.sleep(5)
