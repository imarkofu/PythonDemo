#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from enum import Enum, unique

# 使用枚举类

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC = 12
# 好处是简单，缺点是类型是int，并且仍然是变量。

# 更好的方法是为这样的枚举类型定义一个class类型
# 然后，每个常量都是class的一个唯一实例
# Python提供了Enum类来实现这个功能：

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ",", member.value)


# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# @unique装饰器可以帮助我们检查保证没有重复值。
# 访问这些枚举类型可以有若干种方法：

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
# print(Weekday(7))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


# 使用元类
# 动态语言和静态语言最大的不同
# 就是函数和类的定义
# 不是编译时定义的，而是运行时动态创建的。
# 写一个hello.py模块
class Hello(object):
    def hello(self, name='World'):
        print('Hello, %s.' % name)


# 当Python解释器载入hello模块时
# 就会依次执行该模块的所有语句
# 执行结果就是动态创建出一个Hello的class对象，测试如下：

# from hello import Hello
# h = Hello()
# h.hello()
# Hello, World.
# print(type(Hello))
# <class 'type'>
# print(type(h))
# <class 'hello.Hello'>

# type()函数可以查看一个类型或变量的类型
# Hello是一个class，它的类型就是type
# 而h是一个实例，它的类型就是class Hello。


# type()函数既可以返回一个对象的类型
# 又可以创建出新的类型
# 比如，我们可以通过type()函数创建出Hello类
# 而无需通过class Hello(object)...的定义：


def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()
print(type(Hello()))
print(type(h))


# 要创建一个class对象，type()函数依次传入3个参数：
# 1、class的名称
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


# __new__()方法接收到的参数依次是：
# 1、当前准备创建的类的对象；
# 2、类的名字；
# 3、类继承的父类集合；
# 4、类的方法集合。

L = MyList()
L.add(1)
print(L)


# 普通list没有add方法
# L2 = list()
# L2.add(1)

# 动态修改有什么意义？
# 直接在MyList定义中写上add()方法不是更简单吗？
# 正常情况下，确实应该直接写，通过metaclass修改纯属变态。

# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# 把关系数据库的一行映射为一个对象
# 也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义
# 因为只有使用者才能根据表的结构定义出对应的类来。


# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()

# 父类Model和属性类型StringField、IntegerField是由ORM框架提供的
# 剩下的魔术方法比如save()全部由metaclass自动完成
# 虽然metaclass的编写会比较复杂
# 但ORM的使用者用起来却异常简单。


# 按上面的接口来实现该ORM
# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field
# 比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 编写最复杂的ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs);
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s ' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()



