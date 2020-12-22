from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.ID, 'droppable').text)

        self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)
