# -*- coding: utf-8 -*-
# @Time : 2019/8/16 14:04
# @Author : wangmengmeng
def foo():
    print("全局空间的foo方法")
bar = 20
class Bird:
    def foo():
        print("Bird空间的foo方法")
    bar = 200

foo()
print(bar)
Bird.foo()
print(Bird.bar)