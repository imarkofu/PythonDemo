#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 可变参数
# 但是调用的时候，需要先组装出一个list或tuple：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


# 在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum;


print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))
print(calc())
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# *nums表示把nums这个list的所有元素作为可变参数传进去
calc(calc(*nums))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 关键字参数允许你传入0个或任意个含参数名的参数
# 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, " age:", age, " other:", kw)


person("Michael", 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 关键字参数可以扩展函数的功能
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
person('Jack', 24, **extra)


# 命名关键字参数
# 到底传入了哪些，就需要在函数内部通过kw检查
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, " age:", age, " other:", kw)


# 调用者仍可以传入不受限制的关键字参数
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):
    print('name:', name, " age:", age, " city:", city, " job:", job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)


# person('Jack', 24, 'Beijing', 'Engineer')
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f1(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(100))





