#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 排序算法
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)


# 返回函数
# 函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 如果不需要立刻求和，而是在后面的代码中
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# 闭包
# 返回的函数在其定义内部引用了局部变量args
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 闭包用起来简单，实现起来可不容易。

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()


print(f1())
print(f2())
print(f3())
# 返回闭包时牢记一点：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 缺点是代码较长，可利用lambda函数缩短代码


def createCounter():
    a = [0]
    def counter():
        a[0] = a[0] + 1
        return a[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

