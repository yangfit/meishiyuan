# -*- coding: utf-8 -*-
# @Time : 2020/12/20 15:58
# @Author : fcj11
# @Email : yangfit@126.com
# @File : kuaishou.py
# @Project : meishiyuan
from appium import webdriver

def startapp():
    desired_capabilities = {
        # 测试机平台：Android or ios
        'platformName': 'Android',
        # 测试机名称，通过adb devices获取
        'deviceName': 'emulator-5554',
        # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
        'platformVersion': '7.1.2',
        # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
        'appPackage': 'com.meishio.app',
        # 待测app 的 activity 名
        'appActivity': 'module.home.activity.SplashActivity',
        #中文输入
        'unicodeKeyboard': True,
        }
    # 启动appium session，url为appium的监听地址
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)   #隐式等待30秒