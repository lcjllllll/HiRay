#coding=utf-8
from page.open_page import OpenPage
class OpenHandle:
    def __init__(self,i):
        self.open_page = OpenPage(i)

    def click_permission_allow_button(self):
        self.open_page.get_permission_allow_button().click()

    def click_permission_deny_button(self):
        self.open_page.get_permission_deny_button().click()

    def click_powerBtn_ba(self):
        self.open_page.get_powerBtn_ba().click()

    def click_keyboardBtn_ba(self):
        self.open_page.get_keyboardBtn_ba().click()

    def click_set_ba(self):
        self.open_page.get_set_ba().click()

    def click_homeBtn_ba(self):
        self.open_page.get_homeBtn_ba().click()

    def click_minusBtn(self):
        self.open_page.get_minusBtn().click()

    def click_addBtn(self):
        self.open_page.get_addBtn().click()

    def click_menuBtn(self):
        self.open_page.get_menuBtn().click()
    def click_okBtn(self):
        self.open_page.get_okBtn().click()

    def click_directionBtn(self):
        self.open_page.get_directionBtn().click()

    def click_voiceBtn(self):
        self.open_page.get_voiceBtn().click()

    def click_returnBtn(self):
        self.open_page.get_returnBtn().click()

    def click_devicelistBtn(self):
        self.open_page.get_devicelistBtn().click()

    def click_rightButton(self):
        self.open_page.get_rightButton().click()

    def click_leftButton(self):
        self.open_page.get_leftButton().click()




    def get_fail_tost(self,message):
        tost_element = self.open_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False
