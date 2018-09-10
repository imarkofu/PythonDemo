#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(100 + 200 + 300)


print("hello world!!!")

print('The quick brown fox', 'jumps over', 'the lay dog')

# name = input("input name:")
#
# print('name=' + name)

print('1024 * 768 =', 1024 * 768)


# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('''line1
... line2
... line3''')

print(r'''hello,\n
world''')

a = 123
print(a)
a = "ABC"
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print(10 / 3)
print(10 // 3)

n = 123
f = 456.789
s1 = 'hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

print('ABC'.encode('ASCII'))
print('中文'.encode('UTF-8'))
# print('中文'.encode('ASCII'))


print(b'ABC'.decode('ASCII'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8'))
print(b'\xe4\xb8\xad\xee\x96'.decode('UTF-8', errors='ignore'))

print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('UTF-8')))

print('Hello, %s' % 'World')
print('Hi, %s, you have $%d.' % ('Michael', 10000))
print('%05d-%03d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}'.format('小明', 17.125))

