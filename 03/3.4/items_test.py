# -*- coding: utf-8 -*-
# @Time : 2019/7/31 14:14
# @Author : wangmengmeng
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDT': 7.9}
# 获取字典中的所有key-value对,返回一个dict_items对象
ims = cars.items()
print(ims)
print(type(ims))
print(list(ims)) # 将dict_items转换为列表
print(list(ims)[2]) # 访问第二个key-value对
# 获取字典中的所有key，返回一个dict-keys对象
kys = cars.keys()
print(kys)
print(type(kys))
print(list(kys)) # 将dict-keys转换成列表
print(list(kys)[1]) # 访问第二个key
# 获取字典中的所有value,返回一个dict-values对象
vals = cars.values()
print(vals)
print(type(vals))
print(list(vals)) # 将dict-values转换为列表
print(list(vals)[1]) # 访问第2个value

