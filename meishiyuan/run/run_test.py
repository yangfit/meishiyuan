# -*- coding: utf-8 -*-
# @Time : 2020/12/20 14:59
# @Author : fcj11
# @Email : yangfit@126.com
# @File : run_test.py
# @Project : meishiyuan
import unittest
import time
from BeautifulReport import BeautifulReport
from config.config import REPORT_PATH, CASE_PATH

suite = unittest.defaultTestLoader.discover(CASE_PATH, 'test_case.py')
now_time = time.strftime("%Y%m%d%H%M%S")
filename = f'meishiyuan-report-{now_time}'
runner = BeautifulReport(suite)
runner.report(description='美食源购物流程自动化测试',
              filename=filename,
              report_dir=REPORT_PATH)