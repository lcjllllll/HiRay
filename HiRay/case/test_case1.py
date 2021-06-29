#coding=utf-8
import HTMLTestRunner
import time
import unittest
# from appium import webdriver
from bussiness.open_bussiness import OpenBusiness
from time import sleep
# import threading
class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("this is class setup")
        cls.open_business = OpenBusiness()
    def setUp(self):
        print("this is setup")

    def test_01(self):
        self.open_business.voice()
        sleep(1)
        # self.open_business.device_connect()
        # self.assertEqual(1,2,"数据错误")
        print("this is case1")

    def test_02(self):
        self.assertEqual(1,3,"数据错误")
        print("this is case2")
    def tearDown(self):
        print("this is teardown")
        # if sys.exc_info()[0]: #截图
        #     self.login_business.login_handle.login_page.driver.save_screnshot("D:/jpg/test01.png")

    @classmethod
    def tearDownClass(cls):
        print("this is class teardown")



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01"))
    suite.addTest(CaseTest("test_02"))
    # unittest.TestRunner.run(suite)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("时间" + now)
    html_file = "D:/report/result" + now + ".html"
    with open(html_file, 'wb') as fp:
        # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title="自动化测试",
            description="自动化测试设备"
        )
        # 执行测试用例
        runner.run(suite)
        # 关闭文件流，不关的话生成的报告是空的
        fp.close()