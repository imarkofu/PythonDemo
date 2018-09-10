#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

r1 = 12.34
r2 = 9.08
r3 = 73.1

s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3

print(max(1, 2, 3, -5))
print(int('124'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

print(hex(255))
print(hex(1000))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


def nop():
    pass


if s1 >= 18:
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(12))


# 返回多个值

def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。


# ax^2 + bx + c = 0
def quadratic(aa, b, c):
    if aa == 0:
        raise TypeError('a != 0')
    elif b * b - 4 * aa * c < 0:
        raise TypeError("b^2 - 4 * a * c >= 0")
    else:
        return ((-b + math.sqrt(b * b - 4 * aa * c)) / (2 * aa)), ((-b - math.sqrt(b * b - 4 * aa * c)) / (2 * aa))


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x):
    return x * x


print(power(5))


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(5, 3))
# 旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用
# print(power(5))


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(5))
print(power(5, 4))
# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。


def enroll(name, gender, age=6, city='Beijing'):
    print("======================")
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# 默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())
# 因为默认参数L也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
#
#  定义默认参数要牢记一点：默认参数必须指向不变对象！
#


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())


