# -*- coding: utf-8 -*-
# @Time : 2019/8/19 17:38
# @Author : wangmengmeng
class Fruit:
    def info(self):
        print("我是一个水果！重%g克" % self.weight)


class Food:
    def taste(self):
        print("不同食物口感不同")


class Apple(Fruit, Food):
    pass


a = Apple()
a.weight = 5.6
a.info()
a.taste()
