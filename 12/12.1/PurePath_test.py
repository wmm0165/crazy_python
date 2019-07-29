# -*- coding: utf-8 -*-
# @Time : 2019/6/27 11:13
# @Author : wangmengmeng
from pathlib import *
pp = PurePath('setup.py')
print(type(pp)) # <class 'pathlib.PureWindowsPath'>
pp = PurePath('crazyit','some/path','info')
print(pp) # crazyit\some\path\info
pp = PurePath()
print(pp) # .  默认使用当前路径
pp = PureWindowsPath('c:/windows','d:info') # 只有最后一个根路径及其子路径生效，windows下只有盘符才算根路径，仅有/是不算的
print(pp) # d:info