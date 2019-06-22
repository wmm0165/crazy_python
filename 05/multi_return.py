# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 16:58
# @Author  : wangmengmeng
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count
my_list = [20 , 15 , 2.8,'a', 35 , 5.9, 1.8]
tp = sum_and_avg(my_list)
print(tp) # 返回结果是元组
s, avg = sum_and_avg(my_list) # 可以使用多个变量接受函数返回的多个值
print(s)
print(avg)