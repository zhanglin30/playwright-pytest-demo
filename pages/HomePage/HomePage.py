# -*- coding: utf-8 -*-
# @Time : 2024/3/20 14:28
# @Author : zl
# @File : HomePage.py
import time

import allure
class HomePage():
    def __init__(self,page):
        self.page =page
        #每个输入框或按钮对应的位置
        self.url="/kanban/board_list#/home/list"
        self.search_input = page.locator("#txtSearchBoard_inBoardListPage")
        self.search_button1 =page.get_by_text("全站搜索")

    def home2kanban_cilck(self,name):
        with allure.step("打开页面"):
            self.page.goto(self.url)
        #time.sleep(2)
        with allure.step("点击 kanban"):
            self.page.locator("section").filter(has_text=name).click()


    # 查询
    def search(self, value):
        with allure.step("打开页面"):
            self.page.goto(self.url)
        with allure.step("输入关键词:}"+value):
            self.search_input.fill(value)
        with allure.step("点击搜索"):
            self.search_button1.click()
