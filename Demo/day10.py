#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import functools
import time

# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# lambda x: x * x
# 等效
# def f(x):
#     return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能由一个表达式，不用写return
# 返回值就是该表达式的结果
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
# 匿名函数也是函数对象，也可以把匿名函数赋值给一个变量，再利用这个变量调用该函数

f = lambda x: x * x
print(f)
print(f(5))


# 同样可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print(L)
print(list(filter(lambda x: x % 2 == 1, range(1, 20))))


# 装饰器
def now():
    print('2018-08-13')


f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)


# 我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print('call %s:' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2018-08-13')


now()
# 把@log放到now()函数的定义处，相当于执行了语句
now = log(now)


# 由于log()是一个decorator，返回一个函数
# 所以原来的now()函数任然存在，只是想在同名的now变量指向了新的变量
# 于是调用now()将执行新的函数，即log()函数中返回的wrapper()函数

# wrapper函数的参数定义是(*args, **kw)
# 因此wrapper()函数可以接收任意参数的调用
# 在wrapper()函数内，首先打印日志，再调用原函数


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2018-08-13')


now()
# 和两层嵌套的decorator相比，三层嵌套的效果是这样的
now = log('execute')(now)

# 首先执行log('execute')
# 返回decorator函数
# 再调用返回函数，参数是now函数
# 返回值最终是wrapper函数

# 以上两种decorator的定义都没有问题，但还差一步
# 因为函数也是对象，它有__name__等属性
# 经过wrapper装饰过的函数__name__属性已经从'now'变成'wrapper'
print(now.__name__)
# 所以需要把原始函数的__name__属性复制到wrapper函数中
# 否则有些依赖函数签名的代码将会出错

# 需要编写wrapper.__name__ = func.__name__这样的代码
# Python内置functools.wraps就是干这个的


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        rs = fn(*args, **kw)
        print()
        print('%s executed in %s ms' % (fn.__name__, time.time() - start))
        return rs
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 支持@log和@log('execute')
def log(exe):
    if callable(exe):
        def wrapper(*args, **kw):
            print('call %s' % exe.__name__)
            return exe(*args, **kw)
        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print('%s %s' % (exe, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator


@log
def now1():
    pass


@log('execute')
def now2():
    pass


now1()
now2()

