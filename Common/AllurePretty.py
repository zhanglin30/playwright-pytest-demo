# -*- coding: utf-8 -*-
# @Time : 2024/4/24 上午11:17
# @Author : zl
# @File : AllurePretty.py.py
"""
测试报告美化
"""
import allure
import functools
import os

import config


class AllurePretty(object):
    @classmethod
    def PrettyAllureCase(cls,page,CaseData):

        allure.dynamic.feature(CaseData.get("模块"))
        allure.dynamic.story(CaseData.get("功能"))
        allure.dynamic.severity(CaseData.get("优先级"))
        allure.dynamic.title(f'{CaseData.get("用例标题")}')

    @classmethod
    def PrettyAllureScreenShot(cls, page, CaseData):
        filename = os.path.join(config.Screenshot, f"{CaseData.get('用例标题')}.png")
        page.screenshot(path=filename)
        allure.attach.file(source=filename, name=CaseData.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    @classmethod
    def PrettyAllureWarpper(cls, func):
        """装饰器函数"""

        @functools.wraps(func)
        def inner(*args, **kwargs):
            flag = True
            # 添加用例信息
            cls.PrettyAllureCase(page=kwargs.get("page"),CaseData=kwargs.get("CaseData"))  # 如何获取case_data?
            r = func(*args, **kwargs)  # 运行用例
            cls.PrettyAllureScreenShot(page=kwargs.get("page"))
            cls.PrettyAllureScreenShot(page=kwargs.get("page"), CaseData=kwargs.get("CaseData"))

        return inner

