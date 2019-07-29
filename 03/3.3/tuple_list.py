# -*- coding: utf-8 -*-
# @Time : 2019/7/29 23:45
# @Author : wangmengmeng
a_list = ['crazy', 20, -1.2]
a_tuple = tuple(a_list) # 将列表转为元组
print(a_tuple)
a_range = range(1,5)
print(a_range)
print(type(a_range))
b_tuple = tuple(a_range) # 将区间转为元组
print(b_tuple)