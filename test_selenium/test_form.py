from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        user_name = self.driver.find_element(By.ID, 'user_login')
        user_password = self.driver.find_element(By.ID, 'user_password')
        user_select = self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me')
        login = self.driver.find_element(By.NAME, 'commit')
        user_name.send_keys('1060093716@qq.com')
        print(user_name.get_attribute("value"))
        user_password.send_keys('Mdg123456')
        print(user_password.get_attribute("value"))

        user_select.click()
        login.click()
        sleep(10)
