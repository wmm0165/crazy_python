# -*- coding: utf-8 -*-
# @Time : 2019/12/22 0:00
# @Author : wangmengmeng
import time

"""python的两个bool值是True和False，特别地，True可被当做整数1使用，Flase可被当做整数0使用"""
print("1和True是否相等", 1 == True)
print("0和False是否相等", 0 == False)

"""== 比较两个变量的值，is比较两个变量是否引用同一个对象"""
a = time.gmtime()
b = time.gmtime()
print(a == b)
print(id(a))
print(id(b))  # 查看对象的内存地址
print(a is b)  # 每次调用gmtime()都返回不同的对象
