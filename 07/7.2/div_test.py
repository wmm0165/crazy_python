# -*- coding: utf-8 -*-
# @Time : 2019/9/11 15:46
# @Author : wangmengmeng
"""捕获异常的原则：先捕获小异常在捕获大异常"""
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("您输入的两个数相除的结果是：",c)
except IndexError:
    print("索引错误：运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误：程序只能接受整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")


