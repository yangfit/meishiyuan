# -*- coding: utf-8 -*-
# @Time : 2020/12/17 16:51
# @Author : fcj11
# @Email : yangfit@126.com
# @File : swipe.py
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
sleep(8)

while True:
    driver.swipe(300, 1000, 300, 400, 300)
    sleep(5)