# -*- coding: utf-8 -*-
# @Time : 2019/7/30 20:33
# @Author : wangmengmeng
"""get(): 根据key来获取value，用法相当于[]语法，区别在于方括号语法访问不存在的key时会报错KeyError，get()只是返回None，不会报错"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDT': 7.9}
print(cars.get('BMW'))
print(cars.get('PORSCHE'))
print(cars['PORSCHE'])
