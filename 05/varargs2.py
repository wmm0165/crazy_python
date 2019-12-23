# -*- coding: utf-8 -*-
# @Time : 2019/12/23 16:54
# @Author : wangmengmeng
"""形参前加个*意味着该参数可以接收多个参数值，多个参数值被当作元组传入"""
def test(*nums):
    for i in nums:
        print(i)


aa = [1, 2]
print('------')
test(aa)  # 不加*的话会被当做一个参数
print('------')
test(*aa)
print('------')
test(3, 4)
