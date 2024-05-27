# -*- coding: utf-8 -*-
import os

import pytest

import config

if __name__ == '__main__':
    os.system(f"del {os.path.join(config.Screenshot, '*.png')}")
    # 只跑登录接口
    # pytest.main(["-v", "-s",'TestCase/Test_login/Test_login.py', '--reruns=0',  f'--alluredir={config.AllureResult}', "--clean-alluredir"])
    pytest.main(["-v", "-s", '--reruns=0', 'TestCase/Test_kanban/Test_kanban.py',  f'--alluredir={config.AllureResult}', "--clean-alluredir"])
    # 以多线程的形式跑除登录接口
    #pytest.main(["-v", "-s", '--reruns=0','-k=not login', '-n=4',f'--alluredir={config.AllureResult}'])
    # 生成报告
    os.system(f'allure generate {config.AllureResult} -o {config.AllureReport} --clean')