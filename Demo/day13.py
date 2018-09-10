#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import types


# 集成和多态


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()
cat = Cat()
cat.run()


class Dog(Animal):
    def run(self):
        print('Dog is running')


dog = Dog()
dog.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())

# “开闭”原则
# 对扩展开放，对修改封闭


# 静态语言 vs 动态语言

# 对于静态语言来说，如果传入Animal类型
# 则传入的对象必须是Animal类型或它的子类
# 否则无法调用run()方法

# 对于动态语言来说，则不一定需要传入Animal类型
# 自需要保证传入的对象有一个run()方法即可


# 获取对象信息

# 当我们拿到一个对象的引用时
# 如何知道这个对象是什么类型、有哪些方法呢

# 使用type()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(c))

print("======================")
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance

# 能使用type()判断的基本类型也可以使用isinstance()判断

# 并且还能判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()

# 如果要获得一个对象的所有属性和方法，可以用dir()函数
print(dir('abc'))


# 类似__xxx__的属性和方法都有特殊用途
# 比如__len__返回长度
# 如果调用len()函数试图获取一个对象的长度
# 实际它自动去调用该对象的__len__()方法


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))


# 仅仅把属性和方法列出来是不够的
# 配合getattr()、setattr()以及hasattr()
# 我们可以直接操作一个对象的状态


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 有属性x吗
print(hasattr(obj, 'x'))
print(obj.x)

# 有属性y吗
print(hasattr(obj, 'y'))
# 设置一个属性y
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

# 如果试图获取一个不存在的属性
# 会抛出AttributeError的错误
# getattr(obj, 'z')

# 可以传入一个default参数，如果属性不存在，则返回默认值
print(getattr(obj, 'z', 404))


print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())


# 如果能使用obj.x的情况下
# 绝不要写getattr(obj, 'x')

# 正确示例
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None



