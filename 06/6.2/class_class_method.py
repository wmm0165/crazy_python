# -*- coding: utf-8 -*-
# @Time : 2019/8/16 14:18
# @Author : wangmengmeng
class Bird:
    @classmethod  # 类方法
    def fly(cls):
        print("类方法fly:", cls)


Bird.fly()  # 通过类访问类方法
b = Bird()
b.fly()  # 通过对象访问类方法
