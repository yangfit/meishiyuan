# -*- coding: utf-8 -*-
# @Time : 2020/12/14 22:04
# @Author : fcj11
# @Email : yangfit@126.com
# @File : read_data.py
# @Project : ECShop自动化测试
from config.config import DATA_PATH

import xlrd


def read_login_excel(filename=None,x=0):  # 从data下面login_data.xls读取登录数据
    if not filename:
        filename = DATA_PATH
    data = xlrd.open_workbook(filename + '/login_data.xls')
    table = data.sheet_by_name('login')
    a =  [table.row_values(line) for line in range(1, table.nrows)]
    w,e=a[x]
    return w,int(e)
