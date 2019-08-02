# -*- coding: utf-8 -*-
# @Time : 2019/8/2 15:18
# @Author : wangmengmeng
# Timer用于控制指定函数在特定时间内执行一次
from threading import Timer

def hello():
    print("hello world!")
t = Timer(10.0,hello)
t.start()