from po.page.login_page import LoginPage
from po.page.register_page import RegisterPage


class IndexPage:
    def goto_login(self):
        return LoginPage

    def goto_register(self):
        return RegisterPage
