# -*- coding: utf-8 -*-
# @Time : 2019/8/5 11:36
# @Author : wangmengmeng
import threading
import time
class Account:
    # 定义构造器
    def __init__(self,account_bo,balance):
        self.account_no = account_bo
        self.balance = balance
