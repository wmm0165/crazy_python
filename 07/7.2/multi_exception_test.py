# -*- coding: utf-8 -*-
# @Time : 2019/9/11 17:23
# @Author : wangmengmeng
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：",c)
except (IndexError, ValueError, ArithmeticError):
    print("程序发生了数组越界、数字格式异常、算术异常之一")
except:
    print("未知异常")