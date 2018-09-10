#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# 定制类

# __slots__
# __len__()
# __str__
# __repr__
# __iter__
# __getitem__
# __getattr__
# __call__

class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


print(Student('Michael'))

# 如果一个类想被用于for ... in循环，类似list或tuple那样
# 就必须实现一个__iter__()方法


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

# Fib虽然能作用于for循环，看起来和list有点像
# 但把它当list使用还是不行
# 比如
# Fib()[5]


class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])

print(list(range(100))[5:10])

# 对于Fib却报错
# 原因是__getitem__()传入的参数可能是一个int
# 也可能是一个切片对象slice，所以要做判断：


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):  # n是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # n是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0:5])
print(f[:10])
# 没有对step参数作处理
print(f[:10:2])


class Student(object):
    def __init__(self):
        self.name = 'Michael'


s = Student()
print(s.name)
# print(s.score)


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'score':
            return 99


s = Student()
print(s.name)
print(s.score)


class Student(object):
    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute\'%s\'' % item)


# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？
# 作用就是，可以针对完全动态的情况作调用。
s = Student()
print(s.age())

# 举例
# 很多网站搞REST API
# http://api.server/user/friends
# http://api.server/user/timeline/list


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path
    __repr__ = __str__


print(Chain().status.user.timeline.list)

# 这样无论API怎么变，SDK都可以根据URL实现完成动态的调用
# 而且不随API的增加而改变

# 还有些REST API会把参数放在URL中，比如GitHub的API
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名
# Chain().users('michael').repos


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()


print(callable(Student('Michael')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象

# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path=''):
        return Chain('%s/:%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)


