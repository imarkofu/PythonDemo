#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


# Python内建的filter()函数用于过滤序列。
# map()类似，filter()也接收一个函数和一个序列
# map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['a', '', 'dsfa', '  '])))


# 求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    # 初始化序列
    it = _odd_iter()
    while True:
        # 返回序列第一个数
        n = next(it)
        yield n
        # 构造新序列
        it = filter(_not_divisible(n), it)


# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def is_palindrome(n):
    n = str(n)
    ll = len(n)
    if ll == 1:
        return True
    i = 0
    while i < ll / 2:
        if n[i] != n[-1 - i]:
            return False
        i += 1
    return True


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
