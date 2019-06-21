# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 15:12
# @Author  : wangmengmeng

# 定义空字符串
s = "" # 会当作false处理，同理还有False,None,0
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')
my_list = [] # 会当作false处理
if my_list:
    print('my_list不是空列表')
else:
    print('my_list是空列表')

my_dict = {} # 会当作false处理
if my_dict:
    print('my_dict不是空字典')
else:
    print('my_dict是空字典')


