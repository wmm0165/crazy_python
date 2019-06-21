# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 13:52
# @Author  : wangmengmeng

# slice的完整语法：[start: end: step],其中start包含，end不包含

a_tuple = ('crazyit', 20, 5.6 , 'fkit', -17)
print(a_tuple[1:3]) # (20, 5.6)
print(a_tuple[-3:-1]) # (5.6, 'fkit')
print(a_tuple[1:-2]) # (20, 5.6)
print(a_tuple[-3:4]) # (5.6, 'fkit')