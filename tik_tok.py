# -*- coding: utf-8 -*-
# @Time : 2020/12/16 21:33
# @Author : fcj11
# @Email : yangfit@126.com
# @File : tik_tok.py
# @Project : app自动化脚本
from appium import webdriver

# 组装capacity
desired_capabilities = {
    # 测试机平台：Android or ios
    'platformName': 'Android',
    # 测试机名称，通过adb devices获取
    'deviceName': '127.0.0.1:62001',
    # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
    'platformVersion': '7.1.2',
    # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
    'appPackage': 'com.ss.android.ugc.aweme',
    # 待测appium activity
    'appActivity': 'com.tencent.news.activity.SplashActivity',

}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.find_elements_by_id('com.tencent.news:id/wz')