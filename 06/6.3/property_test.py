# -*- coding: utf-8 -*-
# @Time : 2019/8/19 14:06
# @Author : wangmengmeng
class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setsize(self,size):
        self.width,self.height = size

    def getsize(self):
        return self.width,self.height

    def delsize(self):
        self.width,self.height = 0,0

    size = property(getsize,setsize,delsize,'用于描述矩形大小的属性')

print(Rectagle.size.__doc__)
help(Rectagle.size)
rect = Rectagle(4,3)
print(rect.size)


