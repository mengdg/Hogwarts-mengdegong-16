import pytest

from po.test_web_wexin.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        """
        添加成员用例
        :return:
        """
        res = self.main.goto_add_member().add_member().get_member()
        assert '萌萌2' in res

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成员
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert '萌萌2' in res

    @pytest.mark.parametrize("uid,phone,expect", [("1102", "13366470797", "该帐号已被“萌萌2”占有")])
    def test_add_member_fail(self, uid, phone, expect):
        """
        验证注册失败
        :return:
        """
        res = self.main.goto_add_member().add_member_fail(uid, phone)
        assert res == expect

    def teardown_class(self):
        self.main.quit()
