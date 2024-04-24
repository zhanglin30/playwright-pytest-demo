# -*- coding: utf-8 -*-
# @Time : 2024/4/24 下午2:31
# @Author : zl
# @File : config.py.py
"""存放配置文件"""
import os
#获取项目根目录
base_dir = os.path.dirname(os.path.abspath(__file__))
#指定报告的路径
AllureReport = os.path.join(base_dir, "TestReport", "AllureReport")
AllureResult = os.path.join(base_dir, "TestReport", "AllureResult")
Screenshot = os.path.join(base_dir, "TestReport", "Screenshot")

#指定登录信息存放的位置
auth_path = os.path.join(base_dir, "auth", "login.json")

#指定浏览器的位置
CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

#指定项目的根目录
base_url = "https://www.leangoo.com"