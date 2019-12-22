# -*- coding: utf-8 -*-
# @Time : 2019/12/20 16:38
# @Author : wangmengmeng

"""分隔、连接方法"""
s = 'crazyit.org is a good site'
print(s.split())  # 使用空白对字符串进行分割
print(s.split(None, 2))  # 使用空白对字符串进行分割，最多只分割前两个单词
print(s.split('.'))  # 使用.进行分割
mylist = s.split()
print('/'.join(mylist))  # 使用/作为分隔符，将mylist连接成字符串
print(','.join(mylist))  # 使用，作为分隔符，将mylist连接成字符串
