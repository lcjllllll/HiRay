#coding=utf-8
import sys
sys.path.append(r'D:/PyWork/HiRay/HiRay')
from appium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep

def get_driver():
    desired_caps={
  "platformName": "Android",
  "deviceName": "8735563c",#a336ca7
  "platformVision": "9.0",
  "appPackage": "com.sylincom.voicecontrol",
  "appActivity": ".InitActivity",
  "autoGrantPermissions": True
}
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return driver
def get_permission():
    #小智助手获取权限
    except_message = driver.find_element_by_id("com.android.permissioncontroller:id/permission_message")
    if except_message!=None:
        permission_allow_button = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        sleep(1)
        permission_allow_button.click()
    else:
        return None
def enter():
    btn_enter=driver.find_element_by_id("com.sylincom.voicecontrol:id/btn_enter")
    btn_enter.click()

def voiceBtn():
    voiceBtn=driver.find_element_by_id("com.sylincom.voicecontrol:id/voiceBtn")
    voiceBtn.click()

# 点击知道了
def tap_know():
    driver.tap([(500,1271), (579,1347)], 500)


#获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y1,x,y1)

def swipe_right():
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1)



# [500,1271][579,1347]
# 左右滑动
def swipe_on(direction):
    if direction == 'left':
        swipe_left()
    else:
        swipe_right()



driver = get_driver()
sleep(3)
swipe_on('left')
sleep(1)
swipe_on('left')
sleep(1)
swipe_on('left')
sleep(3)
enter()
sleep(1)
voiceBtn()
sleep(1)
tap_know()

