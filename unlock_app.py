# -*- coding: utf-8 -*-
# @Time : 2020/12/18 14:18
# @Author : fcj11
# @Email : yangfit@126.com
# @File : unlock_app.py
# @Project : app自动化脚本
from time import sleep

from appium import webdriver

desired_capabilities = {
    # 测试机平台：Android or ios
    'platformName': 'Android',
    # 测试机名称，通过adb devices获取
    'deviceName': 'emulator-5554',
    # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
    'platformVersion': '7.1.2',
    # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
    'appPackage': 'com.meishio.app',
    # 待测appium activity
    'appActivity': 'module.home.activity.SplashActivity',
    'unicodeKeyboard': True,
    # 'resetKeyboard':True

}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
#锁屏

driver.keyevent(26)
sleep(2)
#获取坐标
size = driver.get_window_size()
print(size)
x = size['width']
y = size['height']

#解锁,出现九宫格图文解锁
driver.back()
sleep(1)
driver.swipe(0.5*x,0.8*y,0.5*x,0.2*y,500)
sleep(2)

#九宫格解锁哟
# action = TouchAction(driver)
# action.press(x=198,y=804)
#
# action.move_to(x=521,y=804)
# action.move_to(x=198,y=1127)
# action.move_to(x=521,y=1127)
# action.release()
# action.perform()
# driver.quit()





s = [1,2,3,5,7,8,9]
gesture(s)