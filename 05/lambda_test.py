# -*- coding: utf-8 -*-
# @Time : 2019/6/23 13:34
# @Author : wangmengmeng
def get_math_fun(type):
    if type == 'square':
        return lambda n: n * n # lambda表达式必须是单行表达式
    elif type == 'cube':
        return lambda n: n * n * n
    else:
        return lambda n:(1 + n) * n / 2
math_fun = get_math_fun('tube')
print(math_fun(5))