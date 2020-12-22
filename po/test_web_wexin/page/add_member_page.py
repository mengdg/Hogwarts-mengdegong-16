from selenium.webdriver.common.by import By

from po.test_web_wexin.page.base_page import BasePage
from po.test_web_wexin.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _localhost_username = (By.ID, 'username')
    _localhost_id = (By.ID, 'memberAdd_acctid')
    _localhost_phone = (By.ID, 'memberAdd_phone')
    _localhost_save = (By.CSS_SELECTOR, '.js_btn_save')
    _localhost_fail = (By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips")

    def add_member(self):
        """
        添加成员操作
        :return:
        """

        self.driver.find_element(*self._localhost_username).send_keys('萌萌2')
        self.driver.find_element(*self._localhost_id).send_keys('1102')
        self.driver.find_element(*self._localhost_phone).send_keys('13366470797')
        self.driver.find_element(*self._localhost_save).click()

        return ContactPage(self.driver)

    def add_member_fail(self, uid, phone):
        self.find(self._localhost_username).send_keys('萌萌2')
        self.find(self._localhost_id).send_keys(uid)
        self.find(self._localhost_phone).send_keys(phone)
        self.find(self._localhost_save).click()
        fail_text = self.find(self._localhost_fail).text
        return fail_text
