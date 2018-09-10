#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from collections import Iterable
from collections import Iterator
# import builtins
from functools import reduce

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
# list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# 为什么list、dict、str等数据类型不是Iterator？
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 高阶函数
# 变量可以指向函数
print(abs(-10))
print(abs)
f = abs
print(f)
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
print(f(-10))

# 函数名也变量
# abs = 10
# print(abs(-1))
# 把abs指向10后，就无法通过abs(-10)调用该函数了！
# builtins.abs = 10


# 传入函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素
# 并把结果作为新的Iterator返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def mul(a, b):
        return a * b
    return reduce(mul, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    i = s.index('.')
    return reduce(fn, map(char2num, s[:i])) + reduce(fn, map(char2num, s[i+1:])) * (0.1**len(s[i+1:]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
