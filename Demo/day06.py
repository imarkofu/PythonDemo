#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os

# 列表生成式
print(list(range(1, 11)))

print([x * x for x in range(1, 11)])
# for循环后面还可以加上if判断
print([x * x for x in range(1, 11) if x % 2 == 0])
# 还可以使用两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])
# 三层和三层以上的循环就很少用到了。

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, "=", v)

# 列表生成式也可以使用两个变量来生成list
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', "IBM", 'Apple']
print([s.lower() for s in L])


L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

g = (x * x for x in range(10))
for n in g:
    print(n)

# a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


print(fib(6))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(6)
print(f)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))


def triangles():
    L = [1]
    while True:
        LL = []
        LL = LL + L
        yield LL
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
