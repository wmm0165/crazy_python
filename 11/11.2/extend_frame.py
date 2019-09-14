# -*- coding: utf-8 -*-
# @Time : 2019/9/12 23:44
# @Author : wangmengmeng
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.initWidgets()
    def initWidgets(self):
        w = Label(self)
        bm = PhotoImage(file='serial.png')
        w.x = bm
        w['image']=bm
        w.pack()
        okButton = Button(self,text="确定")
        okButton['background'] = 'yellow'
        okButton.pack()
app = Application()
print(type(app.master))
app.master.title('窗口标题')
app.mainloop()