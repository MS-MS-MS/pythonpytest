# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/11 16:42
@Author  : MaSai
@FileName: test_demo.py
@SoftWare: PyCharm
"""
import pytest

"""
@pytest.fixture 和 pytest.mark.usefixtures区别
1 usefixtures 可以控制用用例的执行顺序 
注意叠加顺序，先执行的放底层，后执行的放上层

"""

@pytest.fixture
def login():
    print("打开浏览器")
    yield 1


@pytest.fixture
def login1():
    print("关闭浏览器")


class TestDmoe:
    def test_case(self, login1, login):
        print("在登陆成功之后，执行测试用例1")




@pytest.fixture(scope="class")
def fn():
    return 1
    print("打开浏览器")


@pytest.fixture(scope="class")
def fn1():
    print("关闭浏览器")


@pytest.mark.usefixtures("fn1")
@pytest.mark.usefixtures("fn")
class TestCase:
    def test_1(self):
        print("调用")



# @pytest.fixture()
# def test1():
#     print('\n开始执行function')
#
# @pytest.mark.usefixtures('test1')
# def test_a():
#     print('---用例a执行---')
#
#
# @pytest.mark.usefixtures('test1')
# class TestCase:
#
#     def test_b(self):
#         print('---用例b执行---')
#
#     def test_c(self):
#         print('---用例c执行---')