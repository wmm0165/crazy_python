# -*- coding: utf-8 -*-
# @Time : 2019/12/20 17:37
# @Author : wangmengmeng
"""True_statements if expression else False_statements
三目运算符的规则：先对逻辑表达式expression求值，如果逻辑表达式返回True，则返回True_statements；
如果逻辑表达式返回False，则执行并返回False_statements
"""
a = 5
b = 3
st = "a 大于 b" if a > b else "a不大于b"
print(st)