# -*- coding: utf-8 -*-
# @Time : 2019/9/12 14:37
# @Author : wangmengmeng
class SelfException(Exception):
    pass


def main():
    firstMethod()


def firstMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


main()
