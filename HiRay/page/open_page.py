#coding=utf-8
from util.get_by_local import GetByLocal
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
class OpenPage:
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)
    #获取遥控器页面中所有元素的信息
    def get_permission_message(self):
        return self.get_by_local.get_element('permission_message')

    def get_permission_deny_button(self):
        return self.get_by_local.get_element('permission_deny_button')

    def get_permission_allow_button(self):
        return self.get_by_local.get_element('permission_allow_button')

    def get_powerBtn_ba(self):
        return self.get_by_local.get_element('powerBtn_ba')

    def get_keyboardBtn_ba(self):
        return self.get_by_local.get_element('keyboardBtn_ba')

    def get_set_ba(self):
        return self.get_by_local.get_element('set_ba')

    def get_homeBtn_ba(self):
        return self.get_by_local.get_element('homeBtn_ba')

    def get_minusBtn(self):
        return self.get_by_local.get_element('minusBtn')

    def get_addBtn(self):
        return self.get_by_local.get_element('addBtn')

    def get_menuBtn(self):
        return self.get_by_local.get_element('menuBtn')

    def get_okBtn(self):
        return self.get_by_local.get_element('okBtn')

    def get_directionBtn(self):
        return self.get_by_local.get_element('directionBtn')

    def get_voiceBtn(self):
        return self.get_by_local.get_element('voiceBtn')

    def get_returnBtn(self):
        return self.get_by_local.get_element('returnBtn')

    def get_devicelistBtn(self):
        return self.get_by_local.get_element('devicelistBtn')

    def get_rightButton(self):
        return self.get_by_local.get_element('rightButton')

    def get_leftButton(self):
        return self.get_by_local.get_element('leftButton')

    def get_titleText(self):
        return self.get_by_local.get_element('title_text')



    def get_tost_element(self,message):
        """获取toast元素：连接成功"""
        sleep(1)
        tost_element = ('xpath','//*[contains(@text,'+message+')]')
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))


