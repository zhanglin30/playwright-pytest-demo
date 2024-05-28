# -*- coding: utf-8 -*-
# @Time : 2024/5/27 下午2:43
# @Author : zl
# @File : KanbanPage.py
import allure


class KanbanPage():
    def __init__(self,page):
        self.page =page

        # 添加任务按钮
        self.add_task_button= page.locator(".list-add-card-btn").first
        #输入框
        self.new_input=page.get_by_placeholder("Enter提交，Shift+Enter换行").first
        #添加输入框的添加按钮
        self.add_button=page.get_by_role("button", name="添加")

        #编辑页面
        #编辑任务描述按钮
        self.edit_desc_start=page.locator("#divTaskDescTitle")
        #任务描述的输入框
        self.edit_desc_div=page.get_by_placeholder("支持Markdown，Ctrl+V粘贴图片，Ctrl+")
        #任务描述的保存按钮
        self.edit_desc_save_button=page.locator("#taskDescriptionDiv").get_by_role("button", name="保存")
        #评论的输入框
        self.taskcontent_input.get_by_placeholder("输入评论... 可@其他看板成员，Ctrl+Enter保存")
        #评论的保存按钮
        self.taskcontent_save_button=page.locator("#divTaskContentInput").get_by_role("button", name="保存")



    #点击某个任务

    def click_task(self,name):
        """
        :param name:传入要点击的任务名称
        :return:
        """
        with allure.step("点击任务:"+name):
            self.page.get_by_text(name).click()

    def add_task(self,name):
        """
        :param name:传入要添加的任务名称
        :return:
        """
        with allure.step("添加任务:"+name):
            self.add_task_button.click()
            self.new_input.fill(name)
            self.add_button.click()

    def move_task(self,name,target_num:int):
        """
        :param name:传入要移动的任务名称
        :param target_num:传入要移动到的看板序号
        :return:
        """
        with allure.step("移动任务:"+name+"到第"+str(target_num)+"个看板"):
            self.page.get_by_text(name).hover()
            self.page.mouse.down()
            self.page.get_by_text("添加卡片").nth(target_num-1).hover()
            self.page.mouse.up()

    @allure.step("删除任务{1}")
    def del_task(self,name):
        """
        :param name:传入要删除的任务名称
        :return:
        """
        self.page.get_by_text(name).hover()
        self.page.locator(".edit-and-delete-card > span:nth-child(2)").click()
        self. page.locator("#divDeleteTask").get_by_text("删除", exact=True).click()




