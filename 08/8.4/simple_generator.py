# -*- coding: utf-8 -*-
# @Time : 2019/8/31 18:09
# @Author : wangmengmeng
def test(val, step):
    print("----函数开始执行----")
    cur = 0
    for i in range(5):
        cur += i * step
        yield cur


t = test(10, 2)   # 此时函数并未执行，只是返回一个生成器
print(t)
# print(next(t))
# print(next(t))
for ele in t:
    print(ele)
