# -*- coding: utf-8 -*-
# @Time : 2019/10/10 22:56
# @Author : wangmengmeng
from concurrent.futures import ThreadPoolExecutor
import time
import threading


def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum = my_sum + i
    return my_sum
pool =ThreadPoolExecutor(max_workers=2)
future1 = pool.submit(action,50)
future2 = pool.submit(action,100)
print(future1.done())
time.sleep(3)
print(future2.done())
print(future1.result())
print(future2.result())
pool.shutdown()