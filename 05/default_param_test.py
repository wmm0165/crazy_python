# -*- coding: utf-8 -*-
# @Time : 2019/6/23 0:16
# @Author : wangmengmeng

"""
参数默认值：
在某些情况下，程序需要在定义函数时为一个或多个形参指定默认值-这样在调用函数时就可以省略为该形参传入参数值，而是直接使用该形参的默认值
"""

def say_hi(name='孙悟空', message="欢迎来到疯狂软件"):
    print(name, ",您好")
    print("消息是:", message)


say_hi()  # 全部使用默认值
say_hi("白骨精")
say_hi("白骨精", "欢迎学习python")
say_hi(message="欢迎学习python")
say_hi('白骨精', message="欢迎学习python")  # 调用函数时关键字参数必须位于位置参数的后面
