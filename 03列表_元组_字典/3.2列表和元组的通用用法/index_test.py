# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 13:46
# @Author  : wangmengmeng
# 列表和元组都能通过索引访问元素
# 列表的元素相当于一个变量 ，程序既可使用它的值，也可对元素赋值；元组的元素则相当于一个常量 ， 程序只能使用它的值 ， 不能对它重新赋值
a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[2])
print(a_tuple[-1])
print(a_tuple[-2])
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b_tuple[2: 8: 2])  # (3, 5, 7)
