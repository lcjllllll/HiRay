#coding=utf-8
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
from HiRay_keyword.get_data import GetData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ActionMethod:
    def __init__(self):
        base_driver =BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)
    def input(self, *args):
        # 输入值
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],"元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        # 点击
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.click()

    def get_text(self, *args):
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        print("----------------------"+element.text)
        return element.text

    def sleep_time(self, *args):
        #区分开系统时间
        sleep(args[0])

    # 获取屏幕的宽高

    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_left(self, *args):
        x1 = self.get_size()[0] / 10 * 8
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 2
        self.driver.swipe(x1, y1, x, y1)

    def swipe_right(self, *args):
        x1 = self.get_size()[0] / 10 * 2
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x, y1)

    def swipe_up(self, *args):
        x1 = self.get_size()[0] / 10 * 2
        y1 = self.get_size()[1] / 10 * 9
        y2= self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y2,1000)

    def swipe_down(self, *args):
        x1 = self.get_size()[0] / 10 * 2
        y1 = self.get_size()[1] / 10
        y2= self.get_size()[1] / 10* 9
        self.driver.swipe(x1, y1, x1, y2)

    def swipe_on(self, *args):
        if args =='up':
            self.swipe_up()
        elif args=='down':
            self.swipe_down()
        elif args=='left':
            self.swipe_left()
        else:
            self.swipe_right()

    # 点击知道了
    def tap_know(self,*args):
        self.driver.tap([(500, 1271), (579, 1347)], 500)

    def get_element(self, *args):
        """封装找元素的方法"""
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element

    def get_tost_element(self,message):
        """获取toast元素：连接成功"""
        sleep(1)
        tost_element = ('xpath','//*[contains(@text,'+message+')]')
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))

if __name__ == '__main__':
    action=ActionMethod()
    action.get_text("title_guild")