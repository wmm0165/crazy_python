# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 17:13
# @Author  : wangmengmeng

"""
形参前加个*意味着该参数可以接收多个参数值，多个参数值被当作元组传入
"""
def test(a, *books):
    print(books)
    for b in books:
        print(b)
    print(a)

test(5,"疯狂ios讲义","疯狂android讲义")