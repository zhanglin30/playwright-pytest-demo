# -*- coding: utf-8 -*-
# @Time : 2024/5/27 下午2:43
# @Author : zl
# @File : KanbanPage.py
import allure
import yaml
import time

class KanbanPage():
    def __init__(self, page):
        self.page = page
        self.load_elements(self.page,'.\pages\KanbanPage\KanbanPage.yml')
    def load_elements(self,testpage, yaml_path):
        with open(yaml_path, 'r') as file:
            elements_data = yaml.safe_load(file)['elements']
            for element in elements_data:
                setattr(testpage, element['name'], testpage.locator(element['selector']).first)

    def add_task1(self,name):
        """
        :param name:传入要添加的任务名称
        :return:
        """
        with allure.step("添加任务:"+name):
            self.page.add_task_button.click()
            self.page.new_input.fill(name)
            self.page.add_button.click()



