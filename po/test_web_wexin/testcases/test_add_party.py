from po.test_web_wexin.page.main_page import MainPage


class TestAddParty:

    def setup_class(self):
        self.main = MainPage()

    def test_add_party(self):
        """
        添加部门
        :return:
        """
        res = self.main.goto_add_party().add_party().get_party()
        assert 'test' in res

    def teardown(self):
        self.main.quit()
