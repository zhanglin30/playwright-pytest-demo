# -*- coding: utf-8 -*-
# @Time : 2024/3/20 14:35
# @Author : zl
# @File : Test_home.py.py
import allure

from pages.HomePage.HomePage import HomePage
from Tools.ReadYaml import yamlUtil
import os
import pytest


class Test_home_search:


    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("args", yamlUtil(os.getcwd() + "/TestDatas/TestHomeData.yaml").read_yaml())
    def test_home_search(self, page, args):
        allure.dynamic.title('搜索：'+args["value"])
        home_page = HomePage(page)
        home_page.navigate()

        home_page.search(args["value"])