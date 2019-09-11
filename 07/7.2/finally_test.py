# -*- coding: utf-8 -*-
# @Time : 2019/9/11 23:24
# @Author : wangmengmeng
import os


def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
        return
        os._exit(1)
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally里的资源回收！")


test()
