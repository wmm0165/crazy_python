# -*- coding: utf-8 -*-
# @Time : 2019/12/23 10:36
# @Author : wangmengmeng
"""关于栈（先入后出），python中没有push()方法，可使用append()代替"""
stack = []
stack.append('fkit')
stack.append('crazyit')
stack.append('mengmeng')
print(stack)
print(stack.pop())
print(stack)