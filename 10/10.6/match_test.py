# -*- coding: utf-8 -*-
# @Time : 2019/8/5 19:33
# @Author : wangmengmeng
import re

m1 = re.match('www', 'www.fkit.org')
print(m1.span())
print(m1.group())
print(re.match('fkit', 'www.fkit.org'))
m2 = re.search('www', 'www.fkit.org')
print(m2.span())
print(m2.group())
m3 = re.search('fkit', 'www.fkit.org')
print(m3.span())
print(m3.group())
