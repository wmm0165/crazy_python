# -*- coding: utf-8 -*-
# @Time : 2019/6/28 11:25
# @Author : wangmengmeng
import os
import time

print(os.path.abspath("abc.txt"))  # 获取绝对路径
print(os.path.commonprefix(['/usr/lib', 'usr/local/lib']))
print(os.path.dirname('abc/xyz/README.txt')) # 获取目录
print(os.path.exists('abc/xyz/README.txt')) # 判断目录是否存在
print(time.ctime(os.path.getatime('os.path_test.py'))) # 获取最近一次访问时间
print(time.ctime(os.path.getmtime('os.path_test.py'))) # 获取最近一次修改时间
print(time.ctime(os.path.getctime('os.path_test.py'))) # 获取创建时间