from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po.test_web_wexin.page.base_page import BasePage


class ContactPage(BasePage):
    _localhost_member = ".member_colRight_memberTable_td:nth-child(2)"

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        from po.test_web_wexin.page.add_member_page import AddMemberPage
        self.wait((By.CSS_SELECTOR, '.ww_operationBar .js_add_member'))
        self.find(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
        return AddMemberPage(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言
        :return:
        """
        self.wait((By.CSS_SELECTOR, self._localhost_member))
        members = self.driver.find_elements_by_css_selector(self._localhost_member)
        member_res = [i.text for i in members]
        # member_list = []
        # for member in members:
        #     member_list.append(member.text)
        return member_res
