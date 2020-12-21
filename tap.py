# -*- coding: utf-8 -*-
# @Time : 2020/12/17 15:17
# @Author : fcj11
# @Email : yangfit@126.com
# @File : tap.py
# @Project : app自动化脚本
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import By

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.tencent.news',
    'appActivity': 'com.tencent.news.activity.SplashActivity',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True

}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
#点击视频
sleep(5)
driver.tap([(150,150)],500)
sleep(5)
#选择第一个视频
driver.tap([(500,500)],500)
sleep(5)
#点击输入框
driver.tap([(200,85)],500)
sleep(5)
#点击第一个热门
driver.tap([(250,230)],500)
sleep(5)
#从左往右滑动

driver.swipe(200,200,600,200,500)

sleep(10)
driver.quit()



