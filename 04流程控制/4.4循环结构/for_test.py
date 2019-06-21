# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 15:46
# @Author  : wangmengmeng
s_max = int(input("请输入您要计算的阶乘："))
result = 1
for num in range(1, s_max + 1):
    result *= num

print(result)