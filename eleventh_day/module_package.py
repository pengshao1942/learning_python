#导入模块的语法
'''
1、导入整个模块：import 模块名1[as 别名 1], 模块名 2[as 别名 2],...
2、导入模块中指定成员：from 模块名 import 成员名 1[as 别名 1], 成员名 2[as 别名 2],...
'''
'''
两种导入模块方法的区别：
第一种import语句导入整个模块内的所有成员(包括变量、函数、类等)；
第二种import语句只导入模块内的指定成员(除非使用： from 模块名 import * ，但不推荐这种语法)
当使用第一种import语句导入模块中的成员时，必须添加模块名或模块别名前缀；当使用第二种import语句导入模块
中的成员时，无须使用任何前缀，直接使用成员名或成员别名即可
'''

'''
#例如：导入整个sys模块
import sys
print(sys.argv[0]) #使用sys模块名作为前缀来访问模块中的成员
#argv就是sys模块中的变量，用于获取运行Python程序的命令行参数，其中argv[0]用于获取该Python程序的程序名
import sys as s  #导入sys整个模块，并指定别名为s
print(s.argv[0]) #使用 sys模块的别名s作为前缀来访问模块中的成员

#一次导入多个模块
import sys, os
print(sys.argv[0]) 
print(os.sep) #os模块的sep变量代表平台(操作系统)上的路径分隔符：windows是\，linux是 /
import sys as s, os as o  #导入多个模块时，为各个模块指定别名
print(s.argv[0])
print(o.sep)

from sys import argv  #使用from...import导入模块成员的语法来导入指定成员，导入sys模块的argv成员
print(argv[0]) #使用导入成员的语法，直接使用成员名访问，这里就不需要加模块或模块别名作为前缀了
from sys import argv as v #导入sys模块内的argv成员,并为其指定别名v
print(v[0]) #直接使用成员的别名访问
from sys import argv, winver  #导入sys模块内的多个成员：argv、winver
print(argv[0])
print(winver) #sys模块的winver成员记录了该Python的版本号
from sys import argv as v, winver as wv
print(v[0])
print(wv)
'''

'''
#当要调用的多个模板中存在同名成员时，这样调用，给每个模板的成员定别名
from 模块名1 import 成员 as a
from 模块名2 import 成员 as a1
#调用时直接调用别名即可
a()
a1()
'''

#定义模块： 模块就是Python程序，只要导入了模块，就可使用该模块内的所有成员
#模块文件的文件名就是它的模块名，比如： module.py 的模块名就是 module
#编写模块后，要为模块编写说明文档，方便后续使用；在模块定义的第一行代码之前添加如下内容：
'''
模块的功能介绍：...
模块内的变量：...
模块内的函数：...
模块内的类：...
'''
#如：
'''
这个模块的功能是...，该模块包含如下内容
my_book: 字符串变量
say_hi: 简单的函数
User: 代表用户的类
'''
#模块的说明文档，可通过模块的__doc__属性来访问
'''
import os
print(os.__doc__)
'''

#在模块编写完成后，可能需要为模块编写一些测试代码(用例)：用于测试模块中的每一个程序单元是否都能正常运行
#直接使用python运行模块，也是对模块功能的测试

#避免模块中的测试代码在模块调用时执行，即只在测试模块时才执行，可这样做：
'''
在调用测试函数时增加判断；只有当__name__属性为__main__时才调用测试函数，为模块增加如下代码:
#当 __name__为 '__main__'(直接使用python运行该模块)时执行如下代码

if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_User()
再次使用python  module1.py 命令运行该模块，其内的测试代码即可执行
'''
"""
#总结上述，整个模块内容如下：
'''
这是我们编写的第一个模块，该模块包含以下内容
my_book: 字符串变量
say_hi: 简单的函数
User: 代表用户的类
'''
print('这是module 1')
my_book = '疯狂Python讲义'
def say_hi(user):
    print('%s,您好，欢迎学习Python' % user)
class User:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('%s正在慢慢地走路' % self.name)
    def __repr__(self):
        return 'User[name=%s]' % self.name
#以下部分是该模块中成员的测试代码
def test_my_book():
    print(my_book)
def test_say_hi():
    say_hi('孙悟空')
    say_hi(User('Charlie'))
def test_User():
    u = User('白骨精')
    u.walk()
    print(u)
#防止调用该模块时执行模块内的测试代码；即只允许 python module1.py 该模块自己才能执行模块内的测试代码
if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_User()
"""

#定义好模块后，让Python系统能找到并加载该模块
'''两种方法：
1.使用环境变量
2.将模块放在默认的模块加载路径下 
 '''   
#Python根据 PYTHONPATH 环境变量的值来确定到哪里去加载模块
#在windows系统上：设置系统环境变量，设置用户变量即可
#在Linux系统上：进入当前用户的home路径下，在 .bash_profile文件中增加一行
'''
#增加PYTHONPATH环境变量, . 代表当前路径；/home/pengshao/python_module是另一条路径
PYTHONPATH=.:/home/pengshao/python_module
'''
#执行如下命令：使得设置的环境变量生效
'''
export PYTHONPATH
source .bash_profile
'''
#引用模块的程序必须与模块位置一致
#当在同一程序中多次导入同一个模块时，只会生效一次

#默认的模块加载路径： Python默认的模块加载路径由 sys.path 变量代表
#在交互式解释器中执行如下命令：
'''显示Python默认的模块加载路径
>>import sys, pprint
>>pprint.pprint(sys.path)  #pprint可以显示更友好的打印结果
'''
#输出的目录中都可以放模块，但是通常建议将拓展模块添加在lib\site-packages 路径下，此目录专门用于存放Python的拓展模块和包


#案例：编写一个模块
'''
简单的模块，该模块包含以下内容
my_list: 保存列表的变量
print_triangle: 打印由星号组成的三角形的函数
'''

"""
my_list = ['Python', 'Kotlin', 'Swift']
def print_triangle(n):
    '''打印由星号组成的一个三角形'''
    if n <=0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1), end='')
        print('')
#以下是测试代码
def test_print_triangle():  
    print_triangle(3)
    print_triangle(4)
    print_triangle(7)
if __name__ == '__main__':
    test_print_triangle()
"""

#将此模块放在 lib\site-packages 路径下，相当于为Python拓展了一个print_shape模块，任何程序都使用该模块
#在交互解释器中输入如下： 会输出该模块的功能信息
'''
>>import print_shape1
>>print(print_shape1.__doc__)
'''

'''
在导入模块后，可以在模块文件所在目录下看到一个名为 "__pycache__" 的文件夹，
该文件夹里可以看到Python为每个模块都生成一个 *.cpython-python版本号.pyc 的文件，
该文件是Python为模块编译生成的字节码，用于提升该模块的运行效率
'''

#默认情况下，使用 'from 模块名 import' 这样的语句来导入模块，程序会导入该模块中所有不以下划线开头的程序单元
# 借助于模块的 __all__ 变量，将变量的值设置成一个列表，只有该列表中的程序单元才会被暴露出来
# 案例：定义一个包含 __all__ 变量的模块
'''
'测试__all__变量的模块' 

def hello():
    print("Hello, Python")
def world():
    print("Python World is funny")
def test():
    print('--test--')

#定义__all__变量，默认只导入hello和world两个程序单元
__all__ = ['hello', 'world']
'''

#导入all_module 模块中所有的成员
'''
from all_module import *
hello()
world()
#test()  #因为使用了__all__变量，故没有列出的test就没有被导入进来，此时调用会报错
'''

#使用__all__变量的好处是当一个大模块中包含了大量其他程序不需要使用的变量、函数和类时，通过__all__变量即可把它们自动过滤掉
#使用模块内 __all__ 列表之外的程序单元：
'''
1.使用 "import模块名" 来导入模块。通过模块名前缀或模块别名前缀来调用模块内的成员
2.使用 "from 模块名 import 程序单元" 来导入指定程序单元。即使想导入的程序单元没有位于__all__列表中，也依然可以导入
'''




#包：是为了更好地管理多个模块源文件，避免单个模块源文件包含太多的程序单元而变的大而臃肿，不利于模块化开发
#包就是一个文件夹，该文件夹下包含了一个 __init__.py 文件，该文件夹可用于包含多个模块源文件
#包的本质依然是模块，包也可用于包含包pip,如安装了一个包后，可在 lib、site-packages目录下找到这个包文件夹，文件夹里可能还会包含子包文件夹

#定义包
'''
1.创建一个文件夹，该文件夹的名字就是该包的包名
2.在该文件夹内添加一个 __init__.py 文件即可
'''

#例如：创建一个包文件夹、其内的 __init__.py 文件内容如下
'''
这是学习包的第一个示例

print('this is first_package')
'''

#包被导入后，会在包目录下生成一个 __pycache__ 文件夹，并在该文件夹内为包生成一个 __init__.cpython-python版本号.pyc的文件
#导入包就相当于导入该包下的 __init__.py 文件，完全可在 __init__.py 文件中定义变量、函数、类等程序单元
#__init__.py 文件的主要作用就是导入该包内的其他模块



#导入包内成员(下面会叙述此方法的弊端，引入包内 __init__.py 文件的作用)
'''
#导入 fk_package 包，实际上就是导入包下的 __init__.py 文件
import fk_package

#导入fk_package包下的print_shape模块，实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape   #程序访问print_shape.py的程序单元需要添加 fk_package.print_shape 前缀 

#导入 fk_package 包下的billing模块，实际上就是导入 fk_package 目录下的 billing.py 
from fk_package import billing  #程序访问 billing.py 的程序单元，需要添加 billing前缀

#导入 fk_package 包下的 arithmetic_chart 模块，实际上就是导入 fk_package 目录下的 arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)  #访问fk_package包下print_shape模块内的print_blank_triangle方法
im = billing.Item(4.5)  #访问fk_package包下 billing 模块的 Item 类
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)  #访问  fk_package 包下arithmetic_chart模块的print_multiple_chart方法   

'''

#上面引用包类模块及包类模块的方法的弊端：
'''
1.需要很长的前缀才能调用包内模块中的程序单元
2.包内的 __init__.py 文件的功能完全被忽略了
'''
#故：包内的 __init__.py 文件是用于导入该包内模块的成员，这样即可把模块中的成员导入变成包内成员，使用更方便

#包内的 __init__.py 文件内容如下： 
'''
#从当前包中导入 print_shape 模块
from . import print_shape
#从 .print_shape 模块中导入所有程序单元到 fk_package包 中
from .print_shape import *

#从当前包中导入 billing 模块
from . import billing
#从 .billing模块中导入所有程序单元到 fk_package包 中
from .billing import *

#从当前包中导入 arithmetic_chart 模块
from .import arithmetic_chart
#从.arithmetic_chart 模块中导入所有程序单元到 fk_package包 中
from .arithmetic_chart import *
'''

#通用代码
'''
#从当前包中导入 包内的 模块
from .import 包内的模块名(不带.py后缀)
#从 包内的 模块中导入该模块所有程序单元到 该包名 中
from .要导入的包内模块名 import *
'''

#__init__.py 文件这样操作后，之后使用 fk_package. 前缀就可以使用三个模块内的程序单元

'''
#例如： fk_package_test.py

#导入 fk_package 包,实际上就是导入该包下的 __init__.py 文件
import fk_package
#直接使用 fk_package. 前缀即可调用该包所包含的所有模块内的程序单元
fk_package.print_blank_triangle(5)
im = fk_package.Item(4.5)
print(im)
fk_package.print_multiple_chart(5)
'''

#查看模块内容
'''
1.使用 dir() 函数
2.使用模块本身提供的 __all__ 变量
'''
#使用 dir()函数列出的模块中以下划线__开头的程序单元并不希望被外界使用
#使用for循环的列表推导式或模块的__all__变量(如果定义了)来过滤不显示模块中以下划线开头的程序单元,在 python 交互式模式下使用
'''例如:string模块举例
>>[e for e in dir(string) if not e.startswith('__')]
或 
>>string.__all__
'''

#使用 help() 函数来查看程序单元的帮助信息，在python交互式命令行下
#使用help()函数查看的其实就是程序单元的 __doc__ 属性值
#例如：使用help()函数来查看string模块下capwords()函数的作用
'''
>>help(string)
>> help(string.capwords)
>>print(string.capwords.__doc__)
>>import string
>>print(string.capwords('adds:x', sep=':'))
'''

#对模块程序单元的文档信息不详细的，可查看此网址：https://docs.python.org/3/library/index.html

#使用 __file__ 属性查看模块的源文件路径,通过查看源代码来了解模块使用方法
'''在python交互式命令行下
>>import string
>>string.__file__
'''

#有些与底层交互的模块可能是用C语言编写的，而且是C程序编译后的效果，这种模块可能就没有 __file__ 属性

