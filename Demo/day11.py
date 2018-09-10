#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""a test module"""
__author__ = "Gallen"

import functools
import sys

# 偏函数

print(int("12345"))
print(int('12345', base=8))
print(int('12345', 16))


# base默认值为10
# 如果传入base参数，就可以进行进制转换


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))
print(int2('1010101'))

# functools.partial就是帮助我们创建一个偏函数的
# 不需要我们自己定义int2()函数
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))

# 所以functools.partial的作用
# 就是把一个函数的某些参数给固定住（设置默认值）
# 但也可以在函数调用时传入其他值
print(int2('1000000', base=10))


# 创建偏函数时，实际上可以接收函数对象、*args、**kw
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base
# int2('10010')
# 相当于
# kw = {'base': 2}
# int('10010', **kw)

# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边
# max2(5, 6, 7)
# 相当于
# args = (10, 5, 6, 7)
# max(*args)

# 当函数参数个数太多，需要简化时
# 使用functools.partial可以创建一个新的函数
# 这个新函数可以固定住原函数的部分参数
# 从而在调用时更简单


# 模块
# 使用模块
# Python本身内置了很多非常有用的模块
# 示例sys模块
def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world!")
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

# sys模块有一个argv变量，用list存储命令行的所有参数
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# python3 day11.py
# sys.argv获得的就是['day11.py']
# python3 day11.py Gallen
# sys.argv获得的就是['day11.py', 'Gallen']

# if __name__ == '__main__':
#     test()
# 当我们在命令行运行day11模块文件时
# Python解释器把一个特殊变量__name__置为__main__

# 如果其他地方导入day11模块
# if判断将失败
# if测试可以让一个模块通过命令行运行时执行一些额外的代码
# 最常见的就是运行测试


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量
# 有的函数和变量我们希望给别人使用
# 有的函数和变量我们希望仅仅在模块内部使用

# 正常的函数和变量名时公开的(public)可以被直接使用

# 类似__xxx__这样的变量时特殊变量
# 可以被直接引用，但有特殊用途
# 比如上面的__author__，__name__就是特殊变量
# day11模块定义的文档注释也可以用特殊变量__doc__访问
# 我们自己的变量一般不要用这种变量名

# 类似_xxx和__xxx这样的函数或变量就是非公开的(private)
# 不应该被直接引用
# 这里说“不应该”
# 因为Python并没有一种方法可以完全限制访问private函数或变量
# 但从编程习惯上不应该引用private函数或变量


# 安装第三方模块
# Python通过包管理工具pip完成
# Mac或Linux，安装pip本身这个步骤可以跳过

# 示例PIL(Python Imaging Library)第三方库
# 不过PIL只支持到Python 2.7
# 所以安装基于PIL的Pillow

# pip install Pillow


# 安装常用模块
# 我们经常需要用到很多第三方库
# 上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等
# 用pip一个一个安装费时费力，还需要考虑兼容性

# 推荐直接使用Anaconda
# 这是一个基于Python的数据处理和科学计算平台
# 它已经内置了许多非常有用的第三方库
# 装上Anaconda，就相当于把数十个第三方模块自动安装好


# 模块搜索路径

# 当我们试图加载一个模块时
# Python会在指定的路径下搜索对应的.py文件
# 如果找不到，就会报错

# 默认情况下
# Python解释器会搜索
#   当前目录
#   所有已安装的内置模块
#   第三方模块
# 搜索路径存放在sys模块的path变量中
# imports sys
print(sys.path)

# 我们要添加自己的搜索目录【两种方法】
# 修改sys.path
# imports sys
# sys.path.append('/Users/michael/my_py_scripts')
# 这种方法在运行时修改，运行结束后失效

# 设置环境变量PYTHONPATH
# 该环境变量的内容会被自动添加到模块搜索路径中


