# -*- coding: utf-8 -*-
# @Time : 2019/8/19 19:30
# @Author : wangmengmeng
class BaseClass:
    def foo(self):
        print("父类中定义的foo方法")


class SubClass(BaseClass):
    def foo(self):
        print("子类复写父类中的foo方法")

    def bar(self):
        print("执行bar方法")
        self.foo()
        BaseClass.foo(self)  # 使用类名调用实例方法调用父类被重写的方法


sc = SubClass()
sc.bar()
