# -*- coding: utf-8 -*-
# @Time : 2019/6/27 11:26
# @Author : wangmengmeng
from pathlib import *

p = Path('../')
for x in p.iterdir(): # 返回当前目录下的所有文件和子目录
    print(x)