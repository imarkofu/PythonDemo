#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from types import MethodType
# 实例属性和类属性

# 由于Python时动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法时通过实例变量，或者通过self变量


class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


# 当我们定义一个类属性后，这个属性虽然归类所有
# 但类的所有实例都可以访问
class Student(object):
    name = 'Student'


s = Student()
print(s.name)
print(Student.name)
s.name = "Michael"
print(s.name)
print(Student.name)

del s.name
print(s.name)


# 从上面例子可以看出
# 千万不要对实例属性和类属性使用相同的名字
# 因为相同名称的实例属性将屏蔽类属性
# 当删除实例属性后，将访问到类属性


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


# 面向对象高级编程

# 数据封装、集成和多态只是面向对象程序设计中最基础的3个概念
# 在Python中，面向对象还有很多高级特性
# 多重继承、定制类、元类


def set_age(self, age):
    self.age = age


class Student(object):
    pass


s = Student()
s.name = 'Michael'
s.set_age = MethodType(set_age, s)

print(s.name)
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个不起作用


# 为了给所有实例绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score


s.set_score(100)
print(s.score)


# 如果我们想限制实例的属性，怎么办
# 只允许对Student实例添加name和age属性


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99


# __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用


