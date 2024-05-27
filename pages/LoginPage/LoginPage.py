# -*- coding: utf-8 -*-
import time

import allure


class LoginPage():
    def __init__(self,page):
        self.page =page
        #每个输入框或按钮对应的位置
        self.url="/kanban/login/into#/"
        self.username_input = page.get_by_placeholder("手机号或邮箱账号")
        self.password_input =page.get_by_placeholder("密码")
        self.login_button = page.get_by_role("button", name="开始使用")


    # 登录操作
    def login(self, username,password):
        with allure.step("打开页面"):
            self.page.goto(self.url)
        with allure.step("输入用户名"):
            self.username_input.fill(username)
        with allure.step("密码"):
            self.password_input.fill(password)
        with allure.step("点击登录"):
            self.login_button.click()
        time.sleep(5)






