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
'''

#如果某个参数本身包含了空格，则应该将该参数用双引号（""）括起来

'''
#动态修改模块加载路径: 通过 sys.path 属性来实现
import sys
#动态添加 D:\learning_python\Eighth_day\ 路径作为模块加载路径，比添加环境变量更方便
sys.path.append('D:\learning_python\Eighth_day')  #注意这里最后的\不要，不然会转译后面的 '
#加载D:\learning_python\eight\路径下的hello模块
import hello
'''


#os模块：代表了程序所在的操作系统，主要用于获取程序运行所在操作系统的相关信息
#在python交互式解释器中：__all__变量代表了该模块开放的公开接口，并不是所有模块都有__all__变量
'''
>>import os
>>os.__all__
'''

#os模块中常用的属性和函数：
'''
os.name: 返回导入依赖模块的操作系统名称，通常可返回'posix'、'nt'、'java'等值其中之一;nt表示windows系统
os.environ: 返回在当前系统上所有环境变量组成的字典
os.fsencode(filename): 该函数对类路径(path-like)的文件名进行编码
os.PathLike: 是一个类，代表一个类路径(path-like)对象
os.getenv(key, default=None): 获取指定环境变量的值
os.getlogin(): 返回当前系统的登陆用户名。与该函数对应的还有os.getuid()、os.getgroups()、os.getgid()等函数，
                用于获取用户ID、用户组、组ID等，这些函数通常只在Unix类系统上有效
os.getpid(): 获取当前进程ID
os.getppid()：获取当前进程的父进程ID
os.putenv(key, value): 该函数用于设置环境变量
os.cpu_count(): 返回当前系统的CPU数量
os.sep： 返回路径分隔符
os.pathsep: 返回当前系统上多条路径之间的分隔符。windows上是 ;   Unix类系统上是 :
os.linesep: 返回当前系统的换行符。 windows上是 "\r\n"，在Unix类系统上是 "\n" ，Mac OS X系统上是 "\r"
os.urandom(size): 返回适合作为加密使用的、最多由N个字节组成的bytes对象。该函数通过操作系统特定的随即性来源返回随即字节，
                  该随即字节通常是不可预测的,适用于绝大部分加密场景
os._exit(n)：用于强制退出Python解释器,将其放在try块中可以阻止finally块的执行
'''

'''
#示例：演示os模块中部分函数的用法
import os
from os import pathsep
print(os.name)
print(os.getenv('PYTHONPATH'))
print(os.getlogin())
print(os.getpid())
print(os.getppid())
print(os.cpu_count())
print(os.sep)
print(os.pathsep)
print(os.linesep)
print(os.urandom(3))
print(os._exit(n))  #n代表数字
'''

#os模块与进程管理相关的函数：
'''
os.abort():生成一个SIGABRT 信号给当前进程。在unix系统上，默认行为是生成内核转储；在windows系统上，进程立即返回退出代码3
os.execl(path, arg0, arg1, ...): 该函数还有一系列功能类似的函数，比如os.execle()、os.execlp()等
            ，这些函数都是使用参数列表arg0, arg1, ...来执行path所代表的执行文件的
os.forkpty(): fork 一个子进程
os.kill(pid, sig): 将sig信号发送到pid对应的过程，用于结束该进程
os.killpg(pgid, sig):将sig信号发送到pgid对应的进程组
os.popen(cmd, mode='r', buffering=-1):用于向cmd命令打开读写管道(当mode为r时为只读管道，当mode为rw时为读写管道)，
           ，buggering缓存参数与内置的open()函数有相同的含义。该函数返回的文件对象用于读写字符串，而不是字节
os.spawnl(mode, path, ...):该函数还有一系列功能类似的函数，比如 os.spawnle()、os.spawnlp()等，这些函数都用于在新进程中执行新程序
os.startfile(path[, operation]): 对指定文件使用该文件关联的工具执行operation对应的操作，如果不指定operation操作，则默认执行打开(open)操作。
      operation参数必须是有效的命令行操作项目，比如open(打开)、edit(编辑)、print(打印)等
os.system(command): 运行操作系统上的指定命令
'''

'''
#示例：演示os模块中与进程管理相关的函数的功能
import os
os.system('cmd')
#使用nodepad打开excel文件
os.startfile('D:\learning_python\eleventh_day\abc.xls')
#os.spawnl(os.P_NOWAIT, 'D:\Typora\Typora.exe', ' ')
os.system('cmd')
'''

#