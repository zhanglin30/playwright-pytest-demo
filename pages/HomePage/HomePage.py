# -*- coding: utf-8 -*-
# @Time : 2024/3/20 14:28
# @Author : zl
# @File : HomePage.py
import allure
class HomePage():
    def __init__(self,page):
        self.page =page
        #每个输入框或按钮对应的位置
        self.url="/kanban/board_list#/home/list"
        self.search_input = page.locator("#txtSearchBoard_inBoardListPage")
        self.search_button1 =page.get_by_text("全站搜索")

    def navigate(self):
        self.page.goto("/kanban/board_list#/home/list")

    # 查询
    def search(self, value):
        with allure.step("打开页面"):
            self.page.goto(self.url)
        with allure.step("输入关键词"):
            self.search_input.fill(value)
        with allure.step("点击搜索"):
            self.search_button1.click()
