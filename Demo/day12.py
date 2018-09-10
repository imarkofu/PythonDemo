#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 面向对象编程

# Python中，所有数据类型都可以视为对象，当然也可以自定义对象
# 自定义的对象数据类型就是面向对象中的类（Class）的概念

# 面向过程
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


# 面向对象
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 类和实例
# 面向对象最重要的概念就是类(Class)和示例(Instance)
# ::类是抽象的模板

print(bart)
print(Student)

bart.name = 'Bart Simpson 01'
bart.print_score()

# __init__方法的第一个参数永远是self
# 表示创建的实例本身
# self不需要传，Python解释器自己会把实例变量传进去


# 数据封装
# 面向对象编程的一个重要特点就是数据疯转
# 上面的Student类中，每个实例都拥有各自的name和score

bart.age = 18
print(bart.age)


# print(lisa.age)


# 访问限制

# 外部代码可以通过直接调用实例变量的方法来操作数据
# 这样就隐藏了内部的复杂逻辑
# 但是外呼代码还是可以自由地修改一个实例的name和score属性

# 如果要让内部属性不被外呼访问
# 可以把属性的名称前加上两个下划线__
# 实例变量名如果以__开头，就变成了私有变量(private)
# 只有内部可以访问，外部不能访问
#

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s = %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)
# print(bart.__name)
bart.print_score()

# 需要注意的是，再Python中，变量名类似__xxx__的
# 是特殊变量，特殊变量是可以直接访问的，不是private的
# 所以不能用__name__、__score__的变量名

# 双下划线开头的实例变量是不是一定不能从外呼访问呢？
# 其实也不是
# 不能访问__name
# 是因为Python解释器对外把__name变量改成了_Student__name

# print(bart._Student__name)
# 但是强烈建议你不要这么干
# 不同版本的Python解释器可能会把__name改成不同的变量名

# 总的来说
# Python本身没有任何机制阻止你干坏事，一切靠自觉

# 注意下面的错误写法
bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.__name = 'New Name'
print(bart.__name)
print(bart.get_name())

# 表面上看，外部代码"成功"的设置了__name变量
# 但实际上这个__name和class内部的__name不是一个变量


