# -*- coding: utf-8 -*-
# @Time : 2020/12/16 16:17
# @Author : fcj11
# @Email : yangfit@126.com
# @File : app.py
# @Project : app自动化脚本
from appium import webdriver
from appium.webdriver.common.mobileby import By
from time import sleep
# 组装capacity
desired_capabilities = {
    # 测试机平台：Android or ios
    'platformName': 'Android',
    # 测试机名称，通过adb devices获取
    'deviceName': 'f9911602',
    # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
    'platformVersion': '10',
    # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
    'appPackage': 'com.kuaishou.nebula',
    # 待测appium activity
    'appActivity': 'com.yxcorp.gifshow.HomeActivity',
    'unicodeKeyboard':True,
    'resetKeyboard':True






}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)


driver.quit()