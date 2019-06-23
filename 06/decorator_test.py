# -*- coding: utf-8 -*-
# @Time : 2019/6/23 16:43
# @Author : wangmengmeng

def funA(fn):
    print('A')
    fn()
    return 'fkit'


@funA
def funB():
    print('B')


print(funB)


# output:
# A
# B
# fkit

def foo(fn):
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))

    return bar


@foo
def my_test(a):
    print("===my_test函数===", a)


print(my_test)
my_test(10)  # 相当于调用bar
# my_test(6,5)
