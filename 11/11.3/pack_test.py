# -*- coding: utf-8 -*-
# @Time : 2019/9/12 23:58
# @Author : wangmengmeng
from tkinter import *

root = Tk()
root.title('pack布局')
for i in range(3):
    lab = Label(root, text= "第%d个Label"%(i+1),bg = '#eeeeee')
    lab.pack()
root.mainloop()