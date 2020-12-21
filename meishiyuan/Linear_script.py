# -*- coding: utf-8 -*-
# @Time : 2020/12/19 11:38
# @Author : fcj11
# @Email : yangfit@126.com
# @File : Linear_script.py
# @Project : meishiyuan
from appium import webdriver
from appium.webdriver.common.mobileby import By
from time import sleep
# 组装capacity
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
    'unicodeKeyboard':True,
    # 'resetKeyboard':True

}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
sleep(2)
driver.find_element(By.ID,'com.meishio.app:id/lead_skip').click()
sleep(1)
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
sleep(2)
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
sleep(2)
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
sleep(3)
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
