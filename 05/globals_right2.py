# -*- coding: utf-8 -*-
# @Time : 2019/6/23 11:26
# @Author : wangmengmeng
name = 'wang'
def test():
    global name
    print(name) # wang
    name = '孙悟空'
test()
print(name) # 孙悟空