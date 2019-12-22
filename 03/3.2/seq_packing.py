# -*- coding: utf-8 -*-
# @Time : 2019/7/29 17:55
# @Author : wangmengmeng
# 序列封包：将10，20，30封装成元组后赋值给vals
vals = 10, 20, 30  # 把多个值赋给一个变量时，python程序会自动将多个值封装成元组
print(vals)
print(type(vals))
print(vals[1])
# 序列解包：将a_tuple元组的个各元素依次赋值给a,b,c,d,e变量
a_tuple = tuple(range(1, 10, 2))
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
a_list = ['fkit', 'crazyit']
# 序列解包，将a_lis序列的各元素依次赋值给a_str,b_str
a_str, b_str = a_list
print(a_str, b_str)
# 序列解包时只分解出部分变量，剩下的依然使用列表变量保存
first, second, *rest = range(10)  # * 表示该变量为一个列表
print(first)
print(second)
print(rest)
