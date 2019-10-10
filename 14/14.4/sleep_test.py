# -*- coding: utf-8 -*-
# @Time : 2019/8/5 11:27
# @Author : wangmengmeng
import time

for i in range(4):
    print("当前时间：%s" % time.ctime())
    time.sleep(1) # 调用sleep()函数让线程暂停1s
