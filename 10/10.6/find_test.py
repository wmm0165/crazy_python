# -*- coding: utf-8 -*-
# @Time : 2019/9/14 23:17
# @Author : wangmengmeng
import re

print(re.findall('fkit','FkIt is very good , Fkit.org is my favorite',re.I))
it = re.finditer('fkit','FkIt is very good , Fkit.org is my favorite',re.I)
for e in it:
    print(str(e.span())+"-->"+e.group())