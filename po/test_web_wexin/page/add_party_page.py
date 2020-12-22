from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from po.test_web_wexin.page.assert_party_page import AssertPartyPage
from po.test_web_wexin.page.base_page import BasePage


class AddPartyPage(BasePage):

    def add_party(self):
        """
        创建部门
        :return:
        """
        self.find(By.CSS_SELECTOR, '.inputDlg_item .ww_inputText').send_keys("test")
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.wait((By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853117193840_anchor"]'))
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853117193840_anchor"]').click()
        self.find(By.CSS_SELECTOR, '.ww_dialog_foot .ww_btn_Blue').click()

        return AssertPartyPage(self.driver)
