# -*- coding: utf-8 -*-
# @Time : 2019/10/10 22:16
# @Author : wangmengmeng
import threading


def action(max):
    for i in range(max):
        print(threading.current_thread().name + "" + str(i))
t = threading.Thread(target=action,args=(100,),name="后台进程")
t.daemon = True  # 必须在start（）前设置
t.start()
for i in range(10):
    print(threading.current_thread().name + "" + str(i))