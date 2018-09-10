#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import time
import pickle
import json
from io import BytesIO
from io import StringIO

# IO编程
# 文件读写

f = open('C:/Users/Gallen/Desktop/see.txt', 'r')
# 如果文件不存在，open()函数就会抛出一个IOError的错误
print(f.read())

# 文件使用完毕后必须关闭
f.close()

try:
    f = open('C:/Users/Gallen/Desktop/see.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('C:/Users/Gallen/Desktop/see.txt', 'r') as f:
    print(f.read())

# 这和前面的try ... finally是一样的

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：


# file-like Object


# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# 还可以是内存的字节流，网络流，自定义流等等
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# 二进制文件
f = open('C:/Users/Gallen/Desktop/a.jpg', 'rb')
print(f.read())

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# 例如，读取GBK编码的文件：

f = open('C:/Users/Gallen/Desktop/tt.txt', 'r', encoding='gbk')
print(f.read())

# 遇到有些编码不规范的文件
f = open('C:/Users/Gallen/Desktop/tt.txt', 'r', encoding='gbk', errors='ignore')
f.close()

# 写文件
f = open('C:/Users/Gallen/Desktop/test.txt', 'w')
f.write("Hello World!")
f.close()

# 同样
with open('C:/Users/Gallen/Desktop/test.txt', 'w') as f:
    f.write('Hello, world!')

# 要写入特定编码的文本文件，给open()函数传入encoding参数

# 'w'模式写入文件时，如果文件已存在，会直接覆盖
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

fpath = r'C:\Windows\system.ini'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)

# StringIO


f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。


# 操作文件和目录

print(os.name)
# windows不提供
# print(os.uname())

print(os.environ)
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('C:\Tools\workspace\idea\PythonDemo\Demo', 'testdir'))
# 然后创建一个目录:
os.mkdir(os.path.join('C:\Tools\workspace\idea\PythonDemo\Demo', 'testdir'))
os.rmdir(os.path.join('C:\Tools\workspace\idea\PythonDemo\Demo', 'testdir'))
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 因为Windows和Linux/Unix/Mac不同

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
print(os.path.split('C:/Users/Gallen/Desktop/see.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('C:/Users/Gallen/Desktop/see.txt'))

# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


def listdir(path):
    curPath = os.path.abspath(path)
    print('   createTime   ', 'size ', 'fileName')
    for fn in os.listdir(curPath):
        absfile = os.path.join(path, fn)
        fileinfo = os.stat(absfile)
        createTime = time.strftime("%Y-%m-%d %X", time.localtime(fileinfo.st_ctime))
        filesize = ''
        if os.path.isfile(absfile):
            filesize += str(os.path.getsize(absfile))
        print(createTime, filesize, fn)


def search(path, des):
    for fn in os.listdir(path):
        absfile = os.path.join(path, fn)
        if os.path.isfile(absfile):
            if fn.find(des) != -1:
                print(absfile)
        else:
            search(absfile, des)


listdir('.')
search('.', '.py')


# 序列化
# Python提供了pickle模块来实现序列化。

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
# pickle.dumps()方法把任意对象序列化成一个bytes，
# 然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
os.remove('dump.txt')


# JSON
print(json.dumps(d))

# JSON反序列化为Python对象
json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str))


# JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 21, 89)
# TypeError: Object of type Student is not JSON serializable
# json.dumps(s)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(s, default=student2dict))
# 更换类后依然不能序列化
# 把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 同样的道理，反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"name": "Bob", "age": 21, "score": 89}'
print(json.loads(json_str, object_hook=dict2student))


obj = dict(name='小明', age=20)
print(json.dumps(obj))
print(json.dumps(obj, ensure_ascii=False))
print(json.dumps(obj, ensure_ascii=True))
