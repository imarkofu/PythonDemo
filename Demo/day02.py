#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', "Tracy"]

print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])

L = []
print(len(L))


# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', "Bob", "Tracy")
# 没有append()，insert()这样的方法。其他获取元素的方法和list是一样的

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
print(t)

# 定义一个空的tuple
t = ()
print(t)

# 但是，要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print(t)

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# Python规定，这种情况下，按小括号进行计算，计算结果自然是1
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：

t = (1, )
print(t)
print(len(t))


# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！


L = [
    ['Apple', 'Google', "Microsoft"],
    ['Java', 'Python', 'Ruby', "PHP"],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


age = 20
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('you age is', age)
    print('kid')

# if判断条件还可以简写
if age:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

# birth = input('birth:')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5

bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)


# dict
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d)
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88

print(d['Jack'])

# 如果key不存在，dict就会报错
# print(d['Thomas'])
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))

d.pop('Bob')
print(d)

# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
#
# 而list相反：
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。

# 需要牢记的第一条就是dict的key必须是不可变对象
# 因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了


s = set([1, 2, 3, 1, 2, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

# set和dict的唯一区别仅在于没有存储对应的value，
# 但是，set的原理和dict一样，所以，同样不可以放入可变对象

a = ['c', 'b', 'e']
a.sort()
print(a)

a = 'abc'
print(a.replace('a', 'A'))
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

