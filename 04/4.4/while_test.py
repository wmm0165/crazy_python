# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 15:33
# @Author  : wangmengmeng
# 循环的初始化条件
count_i = 0
while count_i < 10:  # 需保证循环条件有为假的情况，否则会死循环
    print("conut:", count_i)
    count_i += 1
print("循环结束！")
