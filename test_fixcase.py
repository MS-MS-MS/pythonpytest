# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/11 15:03
@Author  : MaSai
@FileName: test_fixcase.py
@SoftWare: PyCharm
"""
"""
# __title__  =
# __Time__   = 2020-04-06 15:50
# __Author__ = 小菠萝测试笔记
# __Blog__   = https://www.cnblogs.com/poloyy/
# """
# import pytest
#
# # 调用方式一
# @pytest.fixture
# def login():
#     print("输入账号，密码先登录")
#
#
# def test_s1(login):
#     print("用例 1：登录之后其它动作 111")
#
#
# def test_s2():  # 不传 login
#     print("用例 2：不需要登录，操作 222")
#
#
# # 调用方式二
# @pytest.fixture
# def login2():
#     print("please输入账号，密码先登录")
#
#
# @pytest.mark.usefixtures("login2", "login")
# # @pytest.fixture
# # def test_s11(login2, login):
# def test_s11():
#     print("用例 11：登录之后其它动作 111")
#
#
# # 调用方式三
# @pytest.fixture(autouse=True)
# def login3():
#     print("====auto===")
#
#
# # 不是test开头，加了装饰器也不会执行fixture
# @pytest.mark.usefixtures("login2")
# def loginss():
#     print(123)

