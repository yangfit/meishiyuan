# -*- coding: utf-8 -*-
# @Time : 2020/12/17 22:08
# @Author : fcj11
# @Email : yangfit@126.com
# @File : meishiyuan_app.py
# @Project : app自动化脚本
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
sleep(10)
#点击跳过
driver.find_element(By.ID,'com.meishio.app:id/lead_skip').click()
sleep(6)
#刷新
driver.swipe(300,300,300,1500,300)
sleep(4)
#点击农村草鸡蛋
egg = driver.find_element(By.ID,'com.meishio.app:id/product_recommend_home_item')
egg.find_element(By.ID,'com.meishio.app:id/product_recommend_home_item_image').click()
sleep(3)
#点击加入购物车

driver.tap([(450,1840)],500)
# d.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/goods_detail_add_cart\"]').click()
sleep(3)
# #登录
# driver.tap([(100,150)])
driver.find_element(By.ID,'com.meishio.app:id/user_login_username_email_phone').send_keys('username')
sleep(1)
# driver.find_element(By.ID,'com.meishio.app:id/user_login_password').click()
sleep(1)
driver.find_element(By.ID,'com.meishio.app:id/user_login_password').send_keys('123456')
sleep(2)
driver.find_element(By.ID,'com.meishio.app:id/user_login_btn').click()
sleep(5)
#点击购物车
driver.find_element(By.ID,'com.meishio.app:id/goods_detail_cart_image').click()
sleep(3)

#勾选结算商品
driver.find_element(By.ID,'	com.meishio.app:id/shop_cart_goods_item_choice').click()
sleep(3)
#点击结算
driver.find_element(By.ID,'com.meishio.app:id/shop_cart_view_balance').click()
sleep(3)
#添加 收货地址
driver.find_element(By.ID,'	com.meishio.app:id/address_text').click()
sleep(3)


#输入收货人信息
#收货人姓名
driver.find_element(By.ID,'	com.meishio.app:id/add_address_name').click()
sleep(1)
driver.find_element(By.ID,'	com.meishio.app:id/add_address_name').send_keys('你好')
sleep(1)
#手机号
driver.find_element(By.ID,'	com.meishio.app:id/add_address_phone').click()
sleep(1)
driver.find_element(By.ID,'	com.meishio.app:id/add_address_phone').send_keys('12345678902')
sleep(1)
#所在区域
driver.find_element(By.ID,'	com.meishio.app:id/add_address_region').click()
driver.tap([(690,945)],500)
sleep(3)

#详细地址
driver.find_element(By.ID,'com.meishio.app:id/add_address_address').click()
sleep(1)
driver.find_element(By.ID,'com.meishio.app:id/add_address_address').send_keys('某省某市某街道')
sleep(2)

#邮编
driver.find_element(By.ID,'	com.meishio.app:id/add_address_code').click()
sleep(1)
driver.find_element(By.ID,'	com.meishio.app:id/add_address_code').send_keys('644100')
sleep(2)
#点击开始使用
driver.find_element(By.ID,'com.meishio.app:id/user_save_btn').click()

#选择配送方式
driver.find_element(By.ID,'	com.meishio.app:id/order_confirm_shipping_type').click()
sleep(2)
driver.find_element(By.ID,'	com.meishio.app:id/shipping_item_check').click()
sleep(2)
driver.find_element(By.ID,'	com.meishio.app:id/order_confirm_submit').click()











sleep(20)
driver.quit()








