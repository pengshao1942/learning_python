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
#os.system('cmd')
#使用nodepad打开excel文件
#os.startfile('D:\learning_python\eleventh_day\1bc.xls')
#打开Xshell工具
os.spawnl(os.P_NOWAIT, 'D:\Xshell 6\Xshell.exe', ' ')
#使用Typora程序打开bb.py文件
os.execl('D:\Typora\Typora.exe', " ", 'README.md', 'i')
'''

#使用os.system()函数来运行程序时，新程序所在的进程会替代原有的进程
#在使用os.execl()函数运行新进程之后，也会取代原有的进程，故将os.execl()放在最后




#random模块：主要包含生成伪随机数的各种功能变量和函数
#交互式解释器中输入：
'''
>>import random
>>random.__all__
'''
'''random模块下常用函数
random.seed(a=None, version=2):指定种子来初始化伪随机数生成器
random.randrange(start, stop[, step]):返回从start开始到stop结束、步长为step的随即数;
     其实就相当于 choice(range(start, stop, step))的效果，只不过实际底层并不生成区间对象
random.randint(a, b):生成一个范围为 a<<N<<b 的随即数。其等同于 randrange(a, b + 1)的效果
random.choice(seq):从seq中随即抽取一个元素，如果seq为空，则引发 IndexError 异常
random.choices(seq, weights=None, *, cum_weights=None, k=1): 从seq序列中抽出k个元素,还可通过weights
    指定各元素被抽取的权重(代表被抽取的可能性高低)
random.shuffle(x[, random]): 对x序列执行洗牌 “随即排列” 操作
random.sample(population, N或k=N): 从population序列中随即抽取k个独立的元素
random.random():生产一个从0.0(包含)到1.0(不包含)之间的伪随机浮点数
random.uniform(a, b):生成一个范围为 a<<N<<b 的随即数
random.expovariate(lambd): 生成呈指数分布的随即数。其中lambd参数(其实应该是lambda,只是lambda是Python关键字,
      所以简写成lambd) 为 1 除以期望平均值。如果 lambd 是正值，则返回的随即数是从0到正无穷大；如果lambd为负值，
      则返回的随机数是从负无穷大到0

'''
'''
#案例：演示random模块中常见函数的功能和用法
import random
#生成范围为0.0<<x<1.0 的伪随机浮点数
print(random.random())
#生成范围为2.5<<x<<10.0 的伪随机浮点数
print(random.uniform(2.5, 10.0))
#生成呈指数分布的伪随机浮点数
print(random.expovariate(1 / 5))
#生成从0 到 9 的伪随机整数
print(random.randrange(10))
#生成从0 到 100 的随机偶数
print(random.randrange(0, 101, 2))
#随机抽取一个元素
print(random.choice(['Python', 'Swift', 'Kotlin']))
book_list = ['Python', 'Swift', 'Kotlin']
#对列表元素进行随机排列
random.shuffle(book_list)
print(book_list)
#随机抽取4个独立的元素,与下面的写法有些许差异
print(random.sample([10, 20, 30, 40, 50], 4))
#随机抽取3个独立的元素
print(random.sample([10, 20, 30, 40, 50], k=3))
'''

'''
#案例：扑克牌抽牌
import random
import collections  #集合模块

#指定随机抽取6个元素，各元素被抽取的权重(概率)不同
print(random.choices(['Python', 'Swift', 'Kotlin'], [5, 3, 2], k=6))  
#[5, 3, 2]中对应['Python', 'Swift', 'Kotlin']中三个元素的抽取权重比例，比例越小被抽中的几率越小
#下面模拟从52张扑克牌中抽取20张
#在被抽到的20张牌中，牌面为10(包括J、Q、K)的牌占多个比例
#生成一个16个tens(代表10)和36个low_cards(代表其他牌)的集合
deck = collections.Counter(tens=16, low_cards=36)
#从52张牌中随即抽取20张
#seen = random.sample(list(deck.elements()), 20)
seen = random.sample(list(deck.elements()), k=20)
#统计tens元素有多少个，再除以20
print(seen.count('tens') / 20)
'''




