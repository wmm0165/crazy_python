# -*- coding: utf-8 -*-
# @Time : 2019/12/20 16:38
# @Author : wangmengmeng
s = ' this is a puppy '
print(s.lstrip())  # 删除字符串左边的空白
print(s.rstrip())  # 删除字符串右边的空白
print(s.strip())  # 删除字符串两边的空白
print(s)  # s本身不会被改变

s2 = 'i think it is a scarecrow'
print(s2.lstrip('itow'))  # 删除左边的i、t、o、w字符
print(s2.strip('itow'))  # 删除右边的i、t、o、w字符
print(s2.rstrip('itow'))  # 删除两边的i、t、o、w字符
