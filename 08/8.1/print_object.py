# -*- coding: utf-8 -*-
# @Time : 2019/9/10 20:17
# @Author : wangmengmeng
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return "Item[name=" + self.name +",price=" + str(self.price)
im =Item('鼠标',29.8)
print(im)
print(im.__repr__())
