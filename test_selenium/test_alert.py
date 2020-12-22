from selenium.webdriver import ActionChains

from test_selenium.base import Base
import time


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        self.driver.switch_to_frame('iframeResult')

        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        time.sleep(2)
        self.driver.switch_to_alert().accept()

        self.driver.switch_to.default_content()

        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(2)
