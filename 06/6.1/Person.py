# -*- coding: utf-8 -*-
# @Time : 2019/8/13 17:52
# @Author : wangmengmeng
class Person:
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


if __name__ == '__main__':
    p = Person()
    print(p.name, p.age)
    p.name = '李刚'
    p.say('python 语言很简单，学习很容易')
    print(p.name, p.age)
    p.skills = ['programming', 'swimming']  # 为p对象增加一个skills实例变量
    print(p.skills)
    del p.name # 删除实例变量
    # print(p.name)  # AttributeError
    def info(self):
        print("---info函数---",self)
    p.foo = info
    p.foo(p)

