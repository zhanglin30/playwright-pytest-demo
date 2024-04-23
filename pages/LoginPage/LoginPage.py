# -*- coding: utf-8 -*-
import time


class LoginPage():
    def __init__(self,page):
        self.page =page
        #每个输入框或按钮对应的位置
        self.username_input = page.get_by_placeholder("手机号或邮箱账号")
        self.password_input =page.get_by_placeholder("密码")
        self.login_button = page.get_by_role("button", name="开始使用")

    def navigate(self):
        self.page.goto("/kanban/login/into#/")

    # 登录操作
    def login(self, username,password):

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        time.sleep(1000)





