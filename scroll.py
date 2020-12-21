# -*- coding: utf-8 -*-
# @Time : 2020/12/17 16:07
# @Author : fcj11
# @Email : yangfit@126.com
# @File : sctoll.py
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
# el1 = driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"娱乐\"]')
# al2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"要闻\"]')
# driver.scroll(el1,al2)
driver.tap([(677,153)],500)
sleep(4)
el1 = driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"房产\"]')
el2 = driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"小说\"]')
driver.drag_and_drop(el1,el2)
sleep(3)
driver.tap([(670,186)],500)
sleep(2)
driver.tap([(675,83)],500)
sleep(2)
driver.swipe(300,480,300,1000,300)
sleep(5)
driver.swipe(300,1000,300,400,300)
sleep(5)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)
sleep(2)
driver.flick(300,1000,300,400)

sleep(10)

driver.quit()