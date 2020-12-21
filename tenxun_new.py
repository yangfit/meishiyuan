# -*- coding: utf-8 -*-
# @Time : 2020/12/17 11:31
# @Author : fcj11
# @Email : yangfit@126.com
# @File : tenxun_new.py
# @Project : app自动化脚本
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import By
desired_capabilities = {
    'platformName':'Android',
    'platformVersion':'7.1.2',
    'deviceName':'127.0.0.1:52001',
    'appPackage':'com.tencent.news',
    'appActivity':'com.tencent.news.activity.SplashActivity',
    'noReset':True,
    'unicodeKeyboard':True,
    'resetKeyboard':True

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
driver.implicitly_wait(30)
#1，首页搜索框
driver.find_element(By.ID,'com.tencent.news:id/aol').click()
sleep(5)
#2，输入内容‘嫦娥5号’
driver.find_element(By.ID,'com.tencent.news:id/c7n').send_keys('嫦娥5号')
sleep(5)
#3，回车
sleep(5)
driver.keyevent(66)
sleep(5)
#4，进入搜索结果页面‘嫦娥回家了’
driver.find_element(By.XPATH,'//android.widget.TextView[@text=\"嫦娥5号成功回家！下一步将是载人登月，但还差一个4000吨的大家伙\"]').click()
sleep(5)
#5，返回
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"com.tencent.news:id/cn1\"]').click()
sleep(5)
#6，重新搜索输入‘新冠肺炎’
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id=\"com.tencent.news:id/c7n\"]').send_keys('新冠肺炎')
#7.回车
sleep(10)

driver.quit()