# -*- coding: utf-8 -*-
# @Time : 2019/12/20 16:38
# @Author : wangmengmeng
s = 'crazyit . org is a good site'
print(s.startswith('crazyit'))  # 判断s是否以crayit开头
print(s.endswith('site'))
print(s.find('org'))  # 查找子串在字符串中出现的位置
print(s.index('org'))
print(s.find('org', 9))
print(s.replace('it', 'xxxx'))  # 替换字符串
