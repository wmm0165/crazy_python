# -*- coding: utf-8 -*-
# @Time : 2019/9/12 0:52
# @Author : wangmengmeng


def test():
    try:
        return True  # 由于finally中包含return，该return语句失效
    finally:
        return False


a = test()
print(a)
