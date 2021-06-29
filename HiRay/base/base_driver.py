#coding=utf-8
from time import sleep
from appium import webdriver
from util.write_user_command import WriteUserCommand
class BaseDriver:
    def android_driver(self,i):
        #devices_name
        #port
        write_file = WriteUserCommand()
        devices = write_file.get_value('device_info_'+str(i),'deviceName')
        port = write_file.get_value('device_info_'+str(i),'port')

        desired_caps = {
            "platformName": "Android",
            "deviceName": devices,
            "platformVision": "10.0",
            "appPackage": "com.sylincom.voicecontrol",
            "appActivity": ".InitActivity",
            "autoGrantPermissions": True
        }
        driver = webdriver.Remote('http://127.0.0.1:'+port+'/wd/hub', desired_caps)
        # driver.implicitly_wait(20)
        return driver
    def ios_driver(self):
        pass
    def get_driver(self):
        pass

if __name__ == '__main__':
    base =BaseDriver()
    base.android_driver()


