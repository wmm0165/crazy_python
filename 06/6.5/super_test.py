# -*- coding: utf-8 -*-
# @Time : 2019/8/19 19:37
# @Author : wangmengmeng
# 子类的构造方法调用父类的构造方法
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是:', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是: %s,地址是%s' % (self.favorite, self.address))


# Manager继承了Employee、Customer
class Manager(Employee, Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')
        # 通过super()函数调用父类的构造方法
        super().__init__(salary)
        # 与上一行代码的效果相同
        #        super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)


# 创建Manager对象
m = Manager(25000, 'IT产品', '广州')
m.work()  # ①
m.info()  # ②
