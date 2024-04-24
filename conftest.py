# -*- coding: utf-8 -*-
import os

import allure
import pytest
from playwright.sync_api import sync_playwright
from slugify import slugify

import config

pageobjest = None



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """忽略https的错误"""
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.fixture(scope="class")
def page():
    """打开页面的基本操作的封装"""
    # 前置操作
    global pageobjest
    auth_path=config.auth_path
    with sync_playwright() as play:

        browser = play.chromium.launch(headless=False,
                                       executable_path=config.CHROME_PATH)

        # 是否存在认证的缓存，如果存在用缓存的文件打开
        if os.path.exists(auth_path):
            print("使用认证文件")
            context = browser.new_context(base_url=config.base_url, storage_state=auth_path)
        else:
            context = browser.new_context(base_url=config.base_url)

        # 判断是否已经存在浏览器上下文
        if pageobjest is None:
            pageobjest = context.new_page()
        # 返回 pageobjest
        yield pageobjest
        # yield后是执行后的后置处理操作
        # 重新置空
        pageobjest = None
        # 判断认证的缓存是否存在，如果存在跳过，如果不存在写入认证文件的路径
        if os.path.exists(auth_path):
            pass
        else:
            context.storage_state(path=auth_path)
        context.close()
        browser.close()


@pytest.fixture(scope="session", autouse=True)
def auth():
    auth_path=config.auth_path
    if os.path.exists(auth_path):
        os.remove(auth_path)
        print("/n初始化--》删除认证文件")
    yield
    if os.path.exists(auth_path):
        os.remove(auth_path)
        print("/n结束--》删除认证文件")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    allure报告模版
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    """
    if call.when == "call":
        # 失败的情况下
        if call.excinfo is not None and "page" in item.funcargs:
            from playwright.async_api import Page
            page: Page = item.funcargs["page"]

            allure.attach(
                page.screenshot(type='png'),
                name=f"{slugify(item.nodeid)}.png",
                attachment_type=allure.attachment_type.PNG
            )

            # # 向报告中添加视频
            # video_path = page.video.path()
            # page.context.close()  # ensure video saved
            # allure.attach(
            #     open(video_path, 'rb').read(),
            #     name=f"{slugify(item.nodeid)}.webm",
            #     attachment_type=allure.attachment_type.WEBM
            # )

    callers = yield