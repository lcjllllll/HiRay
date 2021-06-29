#coding=utf-8
import HTMLTestRunner
import time
import unittest
# from appium import webdriver
from util.server import Server
from bussiness.open_bussiness import OpenBusiness
from util.write_user_command import WriteUserCommand
from time import sleep
import threading
import multiprocessing

class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName) #父类的方法是不动的
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("this is class setup",parames)
        cls.open_business = OpenBusiness(parames)
    def setUp(self):
        print("this is setup")

    def test_01(self):
        print("test case 里面的参数",parames)
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


def appium_init():
    server = Server()
    server.main()

def get_suite(i):
    print("get_suite里面的",i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01",parame=i))
    suite.addTest(CaseTest("test_02",parame=i))
    # unittest.TestRunner.run(suite)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("时间" + now)
    html_file = "D:/report/"+str(i)+"result" + now + ".html"
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

def get_count():
    write_device_file =WriteUserCommand()
    count = write_device_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    threads = []

    # for i in range(get_count()):#几个设备几个进程
    #     # print(i)
    #     t = threading.Thread(target=get_suite, args=(i,))
    #     threads.append(t)
    #     # t.start()
    # for j in threads:
    #     j.start()

    for i in range(get_count()):#几个设备几个进程
        # print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
        # t.start()
    for j in threads:
        j.start()