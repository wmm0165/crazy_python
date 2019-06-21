# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 14:01
# @Author  : wangmengmeng
a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
print(a_tuple + b_tuple) # ('crazyit', 20, -1.2, 127, 'crazyit', 'fkit', 3.33)
print(a_tuple) # ('crazyit', 20, -1.2) a_tuple并没有被改变
print(b_tuple) #  (127, 'crazyit', 'fkit', 3.33) b_tuple并没有被改变