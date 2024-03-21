# -*- coding: utf-8 -*-
# @Time : 2024/3/20 14:28
# @Author : zl
# @File : HomePage.py
class HomePage():
    def __init__(self,page):
        self.page =page
        #每个输入框或按钮对应的位置
        self.search_input = page.locator("#txtSearchBoard_inBoardListPage")
        self.search_button1 =page.get_by_text("全站搜索")

    def navigate(self):
        self.page.goto("/kanban/board_list#/home/list")

    # 查询
    def search(self, value):

        self.search_input.fill(value)
        self.search_button1.click()
