# -*- coding: utf-8 -*-
# @Time : 2020/12/19 13:45
# @Author : fcj11
# @Email : yangfit@126.com
# @File : base_case.py
# @Project : meishiyuan
import unittest
from time import sleep
from model.start_app import startapp


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = startapp()  # 启动app
        sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()  # 关闭app
