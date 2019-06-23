# -*- coding: utf-8 -*-
# @Time : 2019/6/22 22:08
# @Author : wangmengmeng
def girth(width, height):
    print("width:", width)
    print("height:", height)
    return 2 * (width + height)


print(girth(3.5, 4.8))
print(girth(width=3.5, height=4.8))
print(girth(height=4.8, width=3.5))
print(girth(3.5, height=4.8))
