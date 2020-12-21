# -*- coding: utf-8 -*-
# @Time : 2020/12/19 13:46
# @Author : fcj11
# @Email : yangfit@126.com
# @File : test_case.py
# @Project : meishiyuan
import unittest
from page.home_page import HomePage
from page.my_page import MyPage
from case.base_case import BaseCase
from page.shopping_car_page import ShopingCarPage
from model.read_data import read_login_excel


class shopping_case(BaseCase):

    def test_1(self):
        """选择商品 - 加入购物车 - 登录（未登录情况下）- 加入购物车 - 购物车结算 - 选择配送方式 - 提交订单"""
        #选择商品 - 加入购物车
        hp = HomePage(self.driver)
        hp.join_shopping_car()

        #登录
        username,password = read_login_excel()
        MyPage(self.driver).login(username,password)

        #加入购物车
        hp.click_join_shopping_car()
        #点击确定
        hp.click_confirm()

        #购物车 - 选择配送方式 - 提交订单
        ShopingCarPage(self.driver).submit_oder()


if __name__ == '__main__':
    unittest.main()
