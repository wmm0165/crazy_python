# -*- coding: utf-8 -*-
# @Time : 2019/6/23 0:16
# @Author : wangmengmeng

def say_hi(name = '孙悟空', message="欢迎来到疯狂软件" ):
    print(name,",您好" )
    print("消息是:",message)
say_hi()
say_hi("白骨精")
say_hi("白骨精","欢迎学习python")
say_hi(message="欢迎学习python")