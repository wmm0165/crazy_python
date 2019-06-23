# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 17:13
# @Author  : wangmengmeng

def test(a, *books):
    print(books)
    for b in books:
        print(b)
    print(a)

test(5,"疯狂ios讲义","疯狂android讲义")