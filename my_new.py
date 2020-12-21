# -*- coding: utf-8 -*-
# @Time : 2020/12/17 14:09
# @Author : fcj11
# @Email : yangfit@126.com
# @File : my_new.py
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
# # 点击【我的】
# driver.find_element(By.XPATH, '//android.widget.TextView[@text=\"我的 \"]').click()
# sleep(4)
# # 点击【钱包】
# driver.find_element(By.XPATH,
#                     '//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# sleep(4)
# locator = driver.find_element(By.XPATH,'//android.view.View[@resource-id=\"root\"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]').click()
driver.tap([(150,150)],500)
sleep(2)
driver.tap([(300,300)],500)
sleep(10)
driver.quit()
