# -*- coding: utf-8 -*-
# @Time : 2024/5/27 下午2:56
# @Author : zl
# @File : Test_kanban.py.py
import allure

from pages.KanbanPage.KanbanPage import KanbanPage
from pages.HomePage.HomePage import HomePage
from Tools.RandomUtil import RandomUtil
from Common.AllurePretty import AllurePretty

#定义变量用于参数传递
task_name = "zl测试自动化任务"+RandomUtil.get_strbystart("")
class Test_kanban:

    @allure.title("测试看板添加任务")
    def test_kanban_add(self, page):
        home = HomePage(page)
        home.home2kanban_cilck("zl测试ui自动化看板")
        kanban = KanbanPage(page)
        kanban.add_task(task_name)
    #     #page.pause()
    @allure.title("测试看板移动任务")
    def test_kanban_move_task(self, page):
        home = HomePage(page)
        home.home2kanban_cilck("zl测试ui自动化看板")
        kanban = KanbanPage(page)
        kanban.move_task(task_name,3)
    @allure.title("测试看板删除任务")
    def test_kanban_del_task(self, page):
        home = HomePage(page)
        home.home2kanban_cilck("zl测试ui自动化看板")

        kanban = KanbanPage(page)
        #page.pause()
        kanban.del_task(task_name)




