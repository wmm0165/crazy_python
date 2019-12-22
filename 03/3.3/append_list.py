# -*- coding: utf-8 -*-
# @Time : 2019/12/22 20:58
# @Author : wangmengmeng
a_list = ['crazyit', 20, -2]
a_list.append('fkit')
print(a_list)
a_tuple = (3.4, 5.6)
a_list.append(a_tuple)  # 追加元组，元组被当作一个元素
print(a_list)
a_list.append(['a', 'b'])  # 追加列表，列表被当作一个元素
print(a_list)

b_list = ['a', 30]
b_list.extend((-2, 3.1))  # 追加元组中的所有元素
print(b_list)
b_list.append(['C', 'R', 'A'])  # 追加列表中的所有元素
print(b_list)

c_list = list(range(1, 6))
print(c_list)
c_list.insert(3, 'CRAZY')  # 在索引3处增加一个字符串
print(c_list)
c_list.insert(3, tuple('crzay')) # 在索引3处增加一个元组，元组被当作一个元素
print(c_list)
