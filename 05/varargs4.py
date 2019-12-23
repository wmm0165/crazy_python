# -*- coding: utf-8 -*-
# @Time : 2019/12/23 17:08
# @Author : wangmengmeng
"""逆向参数收集：指的是在已有列表、元组、字典等对象的前提下，把它们的元素“拆开”后传递给函数的参数
逆向参数收集需要在列表、元组参数前添加一个*，在字典参数前添加**
"""
def test(name, message):
    print("用户名：", name)
    print("欢迎消息：", message)


my_list = ['孙悟空', '欢迎来到疯狂软件']
test(*my_list)
