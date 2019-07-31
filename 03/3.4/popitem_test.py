# -*- coding: utf-8 -*-
# @Time : 2019/7/31 14:34
# @Author : wangmengmeng
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDT': 7.9}
print(cars)
print(cars.popitem())  # 弹出字典底层存储的最后一个key-value对，是个元组
print(cars)
# 将弹出项的key、value分别赋值给k、v
k, v = cars.popitem()
print(k, v)
