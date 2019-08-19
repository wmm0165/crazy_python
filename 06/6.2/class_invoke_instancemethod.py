# -*- coding: utf-8 -*-
# @Time : 2019/8/16 14:13
# @Author : wangmengmeng
class User:
    def walk(self):
        print(self,"正在慢慢走")

# User.walk()  # 会报错
u = User()
User.walk(u) # 与下面一行代码等效
u.walk()
