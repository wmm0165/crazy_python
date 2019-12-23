# -*- coding: utf-8 -*-
# @Time : 2019/12/23 13:47
# @Author : wangmengmeng
"""setfault()：用于根据key来获取对应的value值。如果该key-value存在，则直接返回key对应的value；如果该key-value不存在，则先为该key设置默认的value，然后再返回key对应的value"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.setdefault('PORSCHE', 9.2))
print(cars)
print(cars.setdefault('BMW', 3.4))
print(cars)