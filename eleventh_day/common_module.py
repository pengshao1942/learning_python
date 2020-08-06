#python的常见内置模块

# sys 模块：代表了python解释器，主要用于获取和python解释器相关的信息
# sys 模块没有 __all__ 变量，列出 sys 模块的全部程序单元：
'''
>>import sys
>>[e for e in dir(sys) if not e.startswith('__')]
'''

#sys模块中常用的属性和函数
'''
sys.argv: 获取运行Python程序的命令行参数。sys.argv[0] 通常就是指该Python程序
sys.argv[1]代表为Python程序提供的第一个参数,sys.argv[2]代表为Python程序提供的第二个参数
#python python程序  参数1  参数2 
sys.byteorder:显示本地字节序的指示符。如果本地字节序是大端模式，则该属性返回big;否则返回little
sys.copyright:该属性返回与Python解释器有关的版权信息
sys.executable:该属性返回Python解释器在磁盘上的存储路径
sys.exit(): 通过引发SystemExit 异常来退出程序。将其放在 try 块中不能阻止 finally 块的执行
sys.flags:该只读属性返回运行Python命令时指定的旗标
sys.getfilesystemencoding():返回在当前系统中保存文件所用的字符集
sys.getrefcount(object):返回指定对象的引用计数。当object对象的引用计数为0时，系统会回收该对象
sys.getrecursionlimit():返回Python解释器当前支持的递归深度。该属性可通过 setrecursionlimit() 方法重新设置
sys.getswitchinterval():返回在当前Python解释器中线程切换的时间间隔。该属性可通过setswitchinterval()函数改变
sys.implementation: 返回当前Python解释器的实现
sys.maxsize:返回Python整数支持的最大值。在32位平台上，该属性值为2**31-1，在64位平台上，该属性值为 2**63 -1
sys.modules: 返回模块名和载入模块对应关系的字典
sys.path:该属性指定Python查找模块的路径列表。可通过修改该属性来动态增加Python加载模块的路径
sys.platform: 返回Python解释器所在平台的标识符
sys.stdin:返回系统的标准输入流------一个类文件对象
sys.stdout:返回系统的标准输出流-----一个类文件对象
sys.stderr:返回系统的错误输出流-----一个类文件对象
sys.version:返回当前Python解释器的版本信息
sys.winver:返回当前Python解释器的主版本号
'''

#示例：使用sys模块中的程序单元
import sys
print(sys.byteorder)
print(sys.copyright)
print(sys.executable)
print(sys.argv[0])
print(sys.winver)
print(sys.platform)

from sys import argv
#输出argv列表的长度
print(len(argv))
#遍历argv列表的每一个元素
for arg in argv:
    print(arg)

#如果某个参数本身包含了空格，则应该将该参数用双引号（""）括起来

#动态修改模块加载路径

