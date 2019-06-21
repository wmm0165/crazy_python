# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 16:22
# @Author  : wangmengmeng
for i in range(0, 3):
    print("i的值是:",i)
    if i == 1:
        # 忽略当次循环的剩下语句
        continue
    print("continue后的输出语句")
# output:
# i的值是: 0
# continue后的输出语句
# i的值是: 1
# i的值是: 2
# continue后的输出语句