# -*- coding: utf-8 -*-
# @Time : 2024/5/27 下午2:43
# @Author : zl
# @File : KanbanPage.py
import allure


class KanbanPage():
    def __init__(self,page):
        self.page =page
        self.add_task_button= page.locator(".list-add-card-btn").first
        self.new_input=page.get_by_placeholder("Enter提交，Shift+Enter换行").first
        self.add_button=page.get_by_role("button", name="添加")



    #点击某个任务

    def click_task(self,page,name):
        with allure.step("点击任务:"+name):
            self.page.get_by_text(name).click()

    def add_task(self,name):
        with allure.step("添加任务:"+name):
            self.add_task_button.click()
            self.new_input.fill(name)
            self.add_button.click()

    def move_task(self,name,target_num:int):
        with allure.step("移动任务:"+name+"到第"+str(target_num)+"个看板"):
            #self.page.get_by_text(name).drag_to(self.page.get_by_text(target_name))不行
            self.page.get_by_text(name).hover()
            self.page.mouse.down()

            self.page.get_by_text("添加卡片").nth(target_num-1).hover()
            self.page.mouse.up()

    def del_task(self,name):
        with allure.step("删除任务:"+name):
            self.page.get_by_text(name).hover()
            self.page.locator(".edit-and-delete-card > span:nth-child(2)").click()
            self. page.locator("#divDeleteTask").get_by_text("删除", exact=True).click()




