# -*- coding: utf-8 -*-
# @Time : 2020/12/18 16:34
# @Author : fcj11
# @Email : yangfit@126.com
# @File : def_page.py
# @Project : app自动化脚本
from appium.webdriver.common.touch_action import TouchAction

from start_app import start
from appium import webdriver



def gesture(s):
    driver = start()
    action = TouchAction(driver)
    p = [[198,804],[360,804],[521,804],
         [198,964],[360,964],[521,964],
         [198,1127],[360,1127],[521,1127]]
    size = driver.get_window_size()
    if size['height'] ==1280 and size['width'] == 720:
        p = p
    else:
        x_offset = size['width']/720
        y_offset = size['height']/1280
        p = [[i[0]*x_offset,i[1]*y_offset]for i in p]
    print('当前屏幕的九宫格坐标为：',p )
    action.press(x=p[s[0]-1][0],y=p[s[0]-1][1])
    for i in s[1:]:
        action.move_to(x=p[i-1][0] ,y=p[i-1][1])
        action.wait(300)
    action.release()
    action.perform()