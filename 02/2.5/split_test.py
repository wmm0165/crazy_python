# -*- coding: utf-8 -*-
# @Time : 2019/12/20 16:38
# @Author : wangmengmeng
def likes(names):
    # your code here
    if len(names) == 0:
        print("no one likes this")
    elif len(names) == 1:
        print("%s likes this" % names[0])
    elif len(names) == 2:
        print("%s and %s likes this" % (names[0],names[1]))
    elif len(names) == 3:
        print("%s,%s and %s likes this" %(names[0],names[1],names[2]))
    else:
        print("%s ,%s and %s others like this" % (names[0], names[1], len(names) - 2))
