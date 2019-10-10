# -*- coding: utf-8 -*-
# @Time : 2019/8/2 14:33
# @Author : wangmengmeng

import threading


# 定义一个普通的action函数，该函数准备作为线程执行体
def action(max):
    for i in range(max):
        print(threading.current_thread().getName() + " " + str(i))


# 下面是主程序（也就是主线程的执行体）
for i in range(100):
    print(threading.current_thread().getName() + " " + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        # 创建并启动第二个线程
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print('主线程执行完成!')
