# -*- coding: utf-8 -*-
# @Time : 2019/12/20 15:22
# @Author : wangmengmeng

b1 = bytes()
# 直接在ASCII字符串前添加b前缀来得到字节串
b2 = b''
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])

# 调用bytes()函数来构建字节串
b4 = bytes('我爱python编程',encoding='utf-8')
print(b4)
# 调用字符串的encode方法来构建字节串
b5 = "学习python很有趣".encode('utf-8')
print(b5)
st = b5.decode('utf-8') # 将bytes对象解码成字符串，默认使用UTF-8进行解码
print(st)