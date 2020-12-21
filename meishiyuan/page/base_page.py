# -*- coding: utf-8 -*-
# @Time : 2020/12/19 11:27
# @Author : fcj11
# @Email : yangfit@126.com
# @File : base_page.py
# @Project : meishiyuan
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):   #封装driver.find_element
        return self.driver.find_element(*locator)

    def find_elements(self, locator):   ##封装driver.find_elements
        return self.driver.find_elements(*locator)

    def tap(self, x, y):   #封装tap
        qqq = self.driver.get_window_size()
        xx = qqq['width'] * x / 1080
        yy = qqq['height'] * y / 1920
        return self.driver.tap([(xx, yy)], 100)
