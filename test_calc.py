import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("pythoncode/data.yaml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        ids_datas = datas["myid"]
        return [add_datas, sub_datas, mul_datas, div_datas, ids_datas]


class TestCalc:
    # def setup_class(self):
    #     self.cal = Calculator()
    #     print('开始计算')
    #
    # def teardown_class(self):
    #     print('结束计算')

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[4])
    def test_add(self, a, b, expect):
        assert expect == a + b

    @pytest.mark.run(order=3)   # 用例排序
    @pytest.mark.flaky(retuns=3, reruns_delay=2)    # 失败后重新运行
    @pytest.mark.parametrize('a,b,expect', get_datas()[1], ids=get_datas()[4])  # 数据驱动
    def test_sub(self, a, b, expect, myfixture):
        assert expect == a - b + 1

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[4])
    def test_mul(self, a, b, expect):
        assert expect == a * b

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[3], ids=get_datas()[4])
    def test_div(self, a, b, expect):
        assert expect == a / b
