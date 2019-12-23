# -*- coding: utf-8 -*-
# @Time : 2019/12/23 10:26
# @Author : wangmengmeng

"""count()：用于统计列表中某个元素的出现次数"""
a_list = [2, 30, 'a', [5, 30], 30]
print(a_list.count(30))  # 计算列表中30出现的次数
print(a_list.count([5, 30]))  # 计算列表中[5，30]出现的次数

