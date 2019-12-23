# -*- coding: utf-8 -*-
# @Time : 2019/12/23 10:42
# @Author : wangmengmeng
"""sort(): 用于对列表元素排序"""
a_list = [3, 4, -2, 30, 14, 9.3, 3.4]
a_list.sort()
print(a_list)
b_list = ['python', 'swift', 'ruby', 'go']
b_list.sort()  # 默认按字符串包含的字符的编号来比较大小
print(b_list)

b_list.sort(key=len, reverse=True)  # key指明排序规则，reverse=True表示从大到小
print(b_list)
