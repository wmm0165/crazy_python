# -*- coding: utf-8 -*-
# @Time : 2019/6/23 11:12
# @Author : wangmengmeng
def test():
    age = 30
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age'] = 12 # 修改局部变量age
    print(age) # age不会被修改
    globals()['x'] = 19
x = 15
y = 20
print(globals())
print(locals())
globals()['x'] = 21
print(x)
locals()['x'] =39
print(x)