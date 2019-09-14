# -*- coding: utf-8 -*-
# @Time : 2019/9/13 0:08
# @Author : wangmengmeng
from tkinter import *

class App:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.label = Label(self.master,width=30)
        self.label['font'] = ('Courier',20)
        self.label['bg'] = 'white'
        self.label.pack()
        bn = Button(self.master,text='单击我',command=self.change)
    def change(self):
        self.label['text'] = '欢迎学习python'


