# playwright+pytest+allure
## 目录说明
1. auth：存放登录后的cookie
2. Common：存放公共方法
3. page：存放页面对象
4. TestCase：存放测试用例
5. TestData：存放测试数据
6. Tools：存放工具类
7. conftest.py：存放测试用例执行前的初始化操作
8. pytest.ini：pytest配置文件
9. run.py：执行测试用例的脚本

## 如何使用
pages放封装的页面对象，包括页面元素定位，页面元素操作，功能封装
TestCase放测试用例，调用页面对象，进行测试用例编写
