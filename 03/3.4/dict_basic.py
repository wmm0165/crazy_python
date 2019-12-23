# -*- coding: utf-8 -*-
# @Time : 2019/7/30 20:14
# @Author : wangmengmeng

"""
字典的基本用法：
通过key访问value
通过key添加key-value对
通过key删除key-value对
通过key修改key-value对
通过key判断指定key-value是否存在
"""
scores = {'语文': 89}
# 通过key访问value,字典的key就相当于它的索引，只不过这些索引不一定是整数类型，可以是任意不可变类型
print(scores['语文'])
# 对不存在的key赋值，就是增加key-value对
scores['数学'] = 93
scores[92] = 5.7
print(scores)
# 使用del删除key-value对
del scores['语文']
del scores['数学']
print(scores)
# 对存在的key-value对赋值，改变key-value对
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDT': 7.9}
cars['BENS'] = 4.3
print(cars)
# 判断cars是否包含名为AUDT的key
print('AUDT' in cars)
print('PORSCHE' in cars)
