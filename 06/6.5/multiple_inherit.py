# -*- coding: utf-8 -*-
# @Time : 2019/8/19 17:48
# @Author : wangmengmeng
# python支持多继承，但是还是尽量使用单继承，以免出错
class Item:
    def info(self):
        print("Item中方法：", '这是一个商品')


class Product:
    def info(self):
        print("Product中方法：", '这是一个工业产品')


class Mouse(Item, Product):
    pass


m = Mouse()
m.info()  # 排在前面的父类方法中的方法会"遮蔽"排在后面的父类中的方法
