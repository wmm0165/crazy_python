# -*- coding: utf-8 -*-
# @Time : 2019/6/28 11:25
# @Author : wangmengmeng
# os.path_test.py
import os
import time

print(os.path.abspath("abc.txt"))  # 获取绝对路径
print(os.path.commonprefix(['/usr/lib', 'usr/local/lib']))
print(os.path.dirname('abc/xyz/README.txt'))  # 获取目录
print(os.path.exists('abc/xyz/README.txt'))  # 判断目录是否存在
print(time.ctime(os.path.getatime('os.path_test.py')))  # 获取最近一次访问时间
print(time.ctime(os.path.getmtime('os.path_test.py')))  # 获取最近一次修改时间
print(time.ctime(os.path.getctime('os.path_test.py')))  # 获取创建时间
print(os.path.getsize('os.path_test.py'))  # 获取文件大小
print(os.path.isfile('os.path_test.py'))  # 判断是否为文件
print(os.path.isdir('os.path_test.py'))  # 判断是否为目录
print(os.path.samefile('os.path_test.py', './os.path_test.py'))  # 判断是否为同一个文件
print(os.listdir('.'))  # 列出所有目录下的文件或文件夹
