# -*- coding: utf-8 -*-
# @Time : 2019/6/23 11:24
# @Author : wangmengmeng
name = 'wang'
def test():
    print(globals()['name']) # wang
    name = 'mengmeng'
test()
print(name) # wang