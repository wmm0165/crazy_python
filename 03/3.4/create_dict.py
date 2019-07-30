# -*- coding: utf-8 -*-
# @Time : 2019/7/29 23:59
# @Author : wangmengmeng
# key-value对
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key,不能使用列表（dict要求key必须是不可变类型，列表是可变类型）
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)
# 可以传入多个列表或元组参数作为key-value对，且每个列表或元组只能包含两个元素
vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
# 创建包含3组key-value对的字典
dict3 = dict(vegetables)
print(dict3)
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
dict4 = dict(cars)
print(dict4)
# 指定关键字参数创建字典
dict6 = dict(spinach=1.39, cabbage=2.59)
print(dict6)
