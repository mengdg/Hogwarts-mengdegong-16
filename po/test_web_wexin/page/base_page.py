import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)

            self.__cookie_login()

            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        else:
            self.driver = base_driver

    def __cookie_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('data.yaml', encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for c in yaml_data:
                self.driver.add_cookie(c)

    def find(self, by, value=None):
        # 如果传入的是元组，需要解元组
        if value is None:
            return self.driver.find_element(*by)
        return self.driver.find_element(by, value)

    def finds(self, by, value=None):
        # 如果传入的是元组，需要解元组
        if value is None:
            return self.driver.find_elements(*by)
        return self.driver.find_elements(by, value)

    def wait(self, value):
        WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(value))

    def quit(self):
        self.driver.quit()