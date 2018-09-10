#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 使用@property


# 绑定属性时，如果我们直接把属性暴露出去，虽然写起来简单
# 但是没办法检查参数，导致可以把成绩随便改
class Student(object):
    pass


s = Student()
s.score = 9999


# 所以
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())


# s.set_score(9999)
# 上面的调用方法又略显复杂，没有直接用属性这么简单
# 装饰器(decorator)可以给函数动态加上功能


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value


s = Student()
s.score = 60  # 实际转化为s.set_score(60)
print(s.score)  # 实际转化为s.get_score()


# s.score = 9999


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


# 上面的birth是可读写，而age就是一个只读属性


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self.height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


# 多重继承

# 继承是面向对象的一个重要方法
# 继承，子类就可以扩展父类的功能


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print("Running...")


class Flyable(object):
    def fly(self):
        print("Flying...")


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为MixIn。


# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass


# MixIn的目的就是给一个类增加多个功能
# 优先考虑多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系


# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
#
#
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
#
#
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass






