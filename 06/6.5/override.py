# -*- coding: utf-8 -*-
# @Time : 2019/8/19 17:55
# @Author : wangmengmeng
# 子类包含与父类同名方法的现象称为重写
class Bird:
    def fly(self):
        print("我在天空里自由自在的飞翔...")


class Ostrich(Bird):
    def fly(self):
        print("我只能在地上奔跑...")


os = Ostrich()
os.fly()
