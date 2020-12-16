import pytest


@pytest.fixture(scope="module")
def myfixture():
    print("开始计算")
    yield
    print('结束计算')


def pytest_collection_modifyitems(session, config, items):
    print('session', session)
    print('config', config)
    print('items', items)
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
