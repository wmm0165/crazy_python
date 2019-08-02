# -*- coding: utf-8 -*-
# @Time : 2019/8/2 14:33
# @Author : wangmengmeng
import threading

def action(max):
    for i in range(max):
        # 调用threading模块的current_thread()函数获取当前进程
        # 调用线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName()+ "" + str(i))

for i in range(100):
    print(threading.current_thread().getName() + "" + str(i))
    if i == 20:
        t1 = threading.Thread(target=action,args=(100,))
        t1.start()
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print('主线程执行完成!')