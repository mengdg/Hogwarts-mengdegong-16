from selenium.webdriver.common.by import By

from po.test_web_wexin.page.base_page import BasePage
import time


class AssertPartyPage(BasePage):

    def get_party(self):
        """
        验证部门列表
        :return:
        """
        time.sleep(3)
        res = self.finds(By.CSS_SELECTOR, '.jstree-anchor')
        partys_list = [i.text for i in res]
        print(partys_list)
        return partys_list