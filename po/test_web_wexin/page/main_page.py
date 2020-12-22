from selenium.webdriver.common.by import By

from po.test_web_wexin.page.add_member_page import AddMemberPage
from po.test_web_wexin.page.assert_party_page import AssertPartyPage
from po.test_web_wexin.page.base_page import BasePage
from po.test_web_wexin.page.contact_page import ContactPage
from po.test_web_wexin.page.add_party_page import AddPartyPage


class MainPage(BasePage):
    _localhost_add = '.ww_indexImg_AddMember'

    def goto_add_member(self):
        """
        跳转到成员页面
        :return:
        """
        self.driver.find_element_by_css_selector(self._localhost_add).click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)

    def goto_add_party(self):
        """
        添加部门
        :return:
        """
        self.find(By.ID, 'menu_contacts').click()
        self.find(By.CSS_SELECTOR, '.js_create_dropdown').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return AddPartyPage(self.driver)

    def goto_assert_party(self):
        """
        验证添加的部门
        :return:
        """
        self.find(By.ID, 'menu_contacts').click()
        return AssertPartyPage(self.driver)
