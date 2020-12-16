import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./data.yaml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        ids_datas = datas["myid"]
        return [add_datas, sub_datas, mul_datas, div_datas, ids_datas]


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print('开始计算')

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[4])
    def test_add(self, a, b, expect):
        assert expect == a + b

    @pytest.mark.parametrize('a,b,expect', get_datas()[1], ids=get_datas()[4])
    def test_sub(self, a, b, expect):
        assert expect == a - b

    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[4])
    def test_mul(self, a, b, expect):
        assert expect == a * b

    @pytest.mark.parametrize('a,b,expect', get_datas()[3], ids=get_datas()[4])
    def test_div(self, a, b, expect):
        assert expect == a / b
