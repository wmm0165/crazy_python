# -*- coding: utf-8 -*-
# @Time : 2019/9/14 23:23
# @Author : wangmengmeng
import re

my_date = '2008-08-18'
print(re.sub(r'-', '/', my_date))
print(re.sub(r'-', '/', my_date, 1))
