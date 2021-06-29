#coding=utf-8
from handle.open_handle import OpenHandle
from page.open_page import OpenPage
from base.base_driver import BaseDriver
from time import sleep
class OpenBusiness:
    def __init__(self,i):
        self.open_page = OpenPage(i)
        self.open_handle = OpenHandle(i)
        self.android_driver=BaseDriver()
    def permission_allow(self):
        #允许权限
        except_message = self.open_page.get_permission_message()
        if except_message!=None:
            sleep(1)
            self.open_handle.click_permission_allow_button()
        else:
            return None
    def permission_allow_all(self):
        self.permission_allow()
        self.permission_allow()
        self.permission_allow()

    def voice(self):
        self.open_handle.click_voiceBtn()
        sleep(1)

    def title_text(self):
        pass



