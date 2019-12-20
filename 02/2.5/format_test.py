# -*- coding: utf-8 -*-
# @Time : 2019/7/28 23:15
# @Author : wangmengmeng
user = 'mengmeng'
age = 25
print("%s is a %s years old girl" % (user, age))  # %s使用str()将变量或表达式转为字符串

# %d表示转换为带符号的十进制形式的整数
num2 = 30
print("num2 is: %06d" % num2)  # 0:表示不补充空格而是补充0
print("num2 is: %+06d" % num2)  # +：表示数值总带着符号（正数带+，负数带-）
print("num2 is: %-6d" % num2)  # -：表示左对齐

# %f表示转换为十进制形式的浮点数
my_value = 3.001415926535
print("my_value is: %8.3f" % my_value)  # 最小宽度为8，小数点后保留3位
print("my_value is: %08.3f" % my_value)  # 最小宽度为8，小数点后保留3位，左边补0
print("my_value is: %+08.3f" % my_value)  # 最小宽度为8，小数点后保留3位，左边补0，始终带符号
the_name = "Charlie"
print("the name is: %.3s" % the_name)  # 只保留3个字符
print("the name is: %10.2s" % the_name)  # 只保留2个字符，最小宽度为10
