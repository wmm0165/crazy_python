# -*- coding: utf-8 -*-
# @Time : 2019/9/11 17:26
# @Author : wangmengmeng
def foo():
    try:
        fis = open("a.txt")
    except Exception as e:
        print(e)
        print(e.args)
        print(e.errno)
        print(e.strerror)


foo()
