import pytest


def setup():
    print('setup --------')


def teardown():
    print('teardown --------')


def setup_module():
    print('setup: 每个模块前执行')


def teardown_module():
    print('teardown: 每个模块后执行')


def setup_function():
    print('setup: 每个函数前执行')


def teardown_function():
    print('teardown: 每个函数后执行')


def test_four():
    print('test-four')


def test_five():
    print('test-five')


class TestClass:

    def setup(self):
        print('setup ========')

    def teardown(self):
        print('teardown ========')

    def setup_class(self):
        print('setup: 每个类开始执行')

    def teardown_class(self):
        print('teardown: 每个类结束执行')

    def setup_method(self):
        print("setup: 每个用例开始执行")

    def teardown_method(self):
        print('teardown：每个用例结束执行')

    def test_one(self):
        print('test-one')

    def test_two(self):
        print('test-two')

    def test_three(self):
        print('test-three')
