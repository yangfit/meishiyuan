# -*- coding: utf-8 -*-
# @Time : 2020/12/18 11:32
# @Author : fcj11
# @Email : yangfit@126.com
# @File : dialog.py
# @Project : app自动化脚本
from appium import webdriver
from appium.webdriver.common.mobileby import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# 组装capacity
desired_capabilities = {
    # 测试机平台：Android or ios
    'platformName': 'Android',
    # 测试机名称，通过adb devices获取
    'deviceName': '127.0.0.1:62001',
    # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
    'platformVersion': '7.1.2',
    # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
    'appPackage': 'com.tencent.news',
    # 待测appium activity
    'appActivity': 'com.tencent.news.activity.SplashActivity',
    'unicodeKeyboard':True,
    # 'resetKeyboard':True
    'noReset':True,
    'automationName':'Uiautomator2'
}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)

#点击洞见
driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"洞见丨浩瀚星空里的中国脚步\"]').click()
sleep(3)
#点击分享
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"com.tencent.news:id/cn8\"]').click()
sleep(3)
#点击取消
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"com.tencent.news:id/ah5\"]').click()
sleep(1)
#返回
driver.back()

#点击【我的】
driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"我的 \"]').click()
sleep(1)
#点击设置
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.tencent.news:id/aif\"]/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]').click()
sleep(2)
#点击推送设置
driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"推送设置\"]').click()
sleep(2)
#点击接收新闻推送
driver.find_element(By.XPATH,'//android.widget.RelativeLayout[@resource-id=\"com.tencent.news:id/bji\"]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.CompoundButton[1]').click()
driver.back()
driver.back()
driver.back()
driver.back()
#等待出现推出的toast提示
WebDriverWait(driver,10).until(lambda driver:
                               driver.find_element(By.XPATH,'//*[@text="再按一次退出腾讯新闻"]'))
#获取文本
toast = driver.find_element(By.XPATH,'//*[@text="再按一次退出腾讯新闻"]').text
print(toast)


sleep(10)

driver.quit()