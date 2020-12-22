from po.page.index_page import IndexPage


class TestIndex:
    def setup_class(self):
        # 实例化一个变量，可以在类中任何地方调用
        self.index_page = IndexPage

    def test_login(self):
        # 1.跳转到登录页面 2.跳转到扫码页面
        self.index_page.goto_login().login_scanf()

    def test_register(self):
        # 1.跳转到注册页面 2.在注册页面进行注册
        self.index_page.goto_register().register()
