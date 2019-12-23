# -*- coding: utf-8 -*-
# @Time : 2019/12/23 10:29
# @Author : wangmengmeng


"""index()用于判断某个元素在列表中的出现位置"""
a_list = [2, 30, 'a', 'b', 'crazyit', 30]
print(a_list.index(30))  # 定位30元素出现的位置
print(a_list.index(30, 2))  # 从2开始，定位30出现的位置
print(a_list.index(30, 2, 4))  # 在索引2和4之间定位30出现的位置，找不到该元素 ValueError