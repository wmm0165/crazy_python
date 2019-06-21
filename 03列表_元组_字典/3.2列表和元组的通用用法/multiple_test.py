# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 14:15
# @Author  : wangmengmeng

# 列表和元组乘法的意义是把包含的元素重复n次
a_tuple = ('crazyit', 20)
mul_tuple = a_tuple * 3
print(mul_tuple)  # ('crazyit', 20, 'crazyit', 20, 'crazyit', 20)

a_list = [20, 'python', 3]
mul_list = a_list * 3
print(mul_list) # [20, 'python', 3, 20, 'python', 3, 20, 'python', 3]