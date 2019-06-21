# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 11:01
# @Author  : wangmengmeng
# 浮点数有两种表示形式:1.十进制形式 2.科学计数形式
afl = 5.2345556
print(afl)
af2 = 25.2345
print(af2)
f1 = 5.12e2
print(f1)
f2 = 5e3 # 虽然值是5000，但它依然是浮点型值
print(f2)
print(type(f2))
# output：
# 5.2345556
# 25.2345
# 512.0
# 5000.0
# <class 'float'>