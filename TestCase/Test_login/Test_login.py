# -*- coding: utf-8 -*-
# @Time : 2024/3/20 14:35
# @Author : zl
# @File : Test_home.py.py
from pages.LoginPage.LoginPage import LoginPage
import pytest
import allure



class Test_login:
    @pytest.mark.run(order=0)
    @allure.title('登录')
    @allure.description('正确的账户密码登录')
    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("13003895886","Zlin@5886.")

