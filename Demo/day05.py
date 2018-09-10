#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from collections import Iterable

L = []
n = 1
while n < 100:
    L.append(n)
    n += 2

print(L)

# 切片
L = ['Michael', 'Sarah', "Tracy", 'Bob', 'Jack']
for i in range(3):
    print(i, '=', L[i])

# 从索引0开始取，直到索引3为止
print(L[0:3])
# 如果第一个索引是0，还可以省略
print(L[:3])
print(L[1:3])
# 支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L)
# 取前10个
print(L[:10])
# 取后10个
print(L[-10:])
# 取11-20
print(L[10:20])
# 取前10个，每2个取一个
print(L[:10:2])
# 取所有，每5个取一个
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list
print(L[:])


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('中文乱码'[:3])
print('ABCDEFG'[::2])


def trim(s):
    ls = len(s)
    if ls == 0:
        return s
    i = 0
    while i < ls and s[i:i + 1] != ' ':
        i += 1
    if i == ls:
        return ''
    start = i
    i = ls
    while i > start and s[i-1:i] != ' ':
        i -= 1
    return s[start:i]


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# 迭代
# for ... in
for key in {'a': 1, 'b': 2, 'c': 3}:
    print(key)
for value in {'a': 1, 'b': 2, 'c': 3}.values():
    print(value)
for ch in 'ABC':
    print(ch)
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办
for i, value in enumerate(['A', 'B', 'C']):
    print(i, '=', value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, '^2=', y)


def findMinAndMax(L):
    ll = len(L)
    if ll == 0:
        return (None, None)
    elif ll == 1:
        return (L[0], L[0])
    min = max = L[0]
    for i in L[1:]:
        if min > i:
            min = i
        elif max < i:
            max = i
    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

