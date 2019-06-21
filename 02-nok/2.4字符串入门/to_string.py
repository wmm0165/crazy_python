# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 11:39
# @Author  : wangmengmeng
# 数值与字符串拼接
s1 = '这本书的价格是：'
p = 99.8
# print(s1 + p) 会报错 TypeError: must be str, not float
print(s1 + str(p))
print(s1 + repr(p))
# output:
# 这本书的价格是：99.8
# 这本书的价格是：99.8
