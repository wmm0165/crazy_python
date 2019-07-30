# -*- coding: utf-8 -*-
# @Time : 2019/7/30 20:39
# @Author : wangmengmeng
# update()执行时，若key-value已存在则被覆盖，不存在则被添加到字典
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDT': 7.9}
cars.update({'BMW': 4.5, 'PORSCHE': 9.3})
print(cars)
