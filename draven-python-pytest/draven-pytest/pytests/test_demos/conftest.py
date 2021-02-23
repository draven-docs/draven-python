import pytest

'''数据共享
    文件名 唯一
    与运行用例须同一package 必须包含 __init__.py
    使用时不需要要导入conftest.py
    全局配置均可写在这里



'''


@pytest.fixture()
def login():
    print("login ...")
