# -*- coding: utf-8 -*-
# @Time : 2019/8/16 14:18
# @Author : wangmengmeng
class Bird:

    @staticmethod  # 静态方法，静态方法在类中也不需要传入self参数
    def info(p):
        print("静态方法:", p)


Bird.info('crazyit')  # 通过类访问静态方法
b = Bird()
b.info('fkit')  # 通过对象访问静态方法

