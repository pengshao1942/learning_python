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


#time模块：主要包含各种提供日期、时间功能的类和函数；提供了把日期、时间格式化为字符串的功能，也提供了从字符串恢复日期、时间的功能
'''
import time
print([e for e in dir(time) if not e.startswith('_')])  #查看time模块包含的全部属性和函数
'''

#在time模块内提供了一个time.struct_time类，该类代表一个时间对象，主要包含9个属性，每个属性的信息如下：
'''
字段名      字段含义    值
tm_year     年         如 2017、2018等
tm_mon      月         如2、3等,范围为 1~12
tm_mday     日         如2、3等，范围为 1~31
tm_hour     时         如2、3等，范围为 0~23
tm_min      分         如2、3等，范围为 0~59
tm_sec      秒         如2、3等，范围为 0~59
tm_wday     周         周一为0，范围为 0~6
tm_yday  一年内第几天   如65，范围为1~366
tm_isdst    夏令时     0、1或 -1
'''
#例如：清楚地代表时间
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=2, tm_hour=8, tm_min=0, tm_sec=30, tm_wday=3, tm_yday=1, tm_isdst=0)

#python还可以用一个包含9个元素的元组来代表时间，该元组的9个元素和 struct_time 对象中9个属性的含义是意义对应的
#如： (2018, 5, 2, 8, 0, 30, 3, 1, 0)

#在日期、时间模块内常用的功能函数如下：
'''
time.asctime([t]): 将时间元组或 struct_time 转换为时间字符串。如果不指定参数t,则默认转换当前时间
time.ctime([secs]):将以秒数代表的时间转换为时间字符串
time.gmtime([secs]):将以秒数代表的时间转换为 struct_time 对象。如果不传入参数，则使用当前时间
time.localtime([secs]): 将以秒数代表的时间转换为代表当前时间的 struct_time 对象，如果不传入参数，则使用当前时间
time.mktime(t): 它是localtime的反转函数，用于将 struct_time 对象或元组代表的时间转换为从 1970年1月 1日 0 点整到现在过了多少秒
time.perf_counter(): 返回性能计数器的值。以秒为单位
time.process_time(): 返回当前进程使用 CPU 的时间。以秒为单位
time.sleep(secs): 暂停 secs 秒，什么都不干
time.strftime(format[, t]):将时间元组或struct_time对象格式化为指定格式的时间字符串，如果不指定参数t,则默认转换当前时间
time.strptime(string[, format]):将字符串格式的时间解析成struct_time 对象,与上一个函数互为逆函数
time.time(): 返回从1970年1月1日0点整到现在过了多少秒
time.timezone: 返回本地时区的时间偏移，以秒为单位
time.tzname: 返回本地时区的名字
'''

'''
#示范time模块的功能函数：
import time
#将当前时间转换为时间字符串
print(time.asctime())
#将指定时间转换为时间字符串，时间元组的后面3个元素没有设置
print(time.asctime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))  #2018年2月4日11点8分23秒
#将以秒数代表的时间转换为时间字符串
print(time.ctime(30))
#将以秒数代表的时间转换为struct_time对象
print(time.gmtime(30))
#将当前时间转换为struct_time对象
print(time.gmtime())
#将以秒数代表的时间转换为代表当前时间的 struct_time 对象
print(time.localtime(30))
#将元组格式的时间转换为以秒数代表的时间
print(time.mktime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))  #1517713703.0
#返回性能计数器的值
print(time.perf_counter())
#返回当前进程使用CPU的时间
print(time.process_time())
#time.sleep(10)
#将当前时间转换为指定格式的字符串
print(time.strftime('%Y-%m-%d %H:%M:S'))  #Python支持的时间格式指令和Linux系统一样
st = '2018年3月20日'
#将指定时间字符串恢复成struct_time对象
print(time.time())
#返回本地时区的时间偏移，以秒为单位
print(time.timezone)  #在中国东八区输出-28800
'''


#json模块
#JSON支持
'''
JSON数据结构：
1. 由 key-value 对组成的数据结构。在python中是一种dict对象
2. 有序集合。在python中对应于列表
'''
#JSON语法格式:
'''
object = 
{
    propertyName1 : propertyValue1,
    propertyName2 : propertyValue2,  #必须当后面还有属性定义时才需要逗号
    ...
}
'''
#在使用JSON语法创建JavaScript对象时，属性值可以时普通字符串、基本数据类型、函数、数组甚至另一个使用JSON语法创建的对象
#例如：
'''
person = 
{
    name : 'yeeku',
    gender : 'male',
    // 使用JSON语法为其指定一个属性
    son : {
        name:'tiger',
        grade:1
    },
    // 使用JSON语法为person直接分配一个方法
    info : function()
    {
        console.log("姓名: " + "this.name" + "性别: " + this.sex);
    }
}
'''

#使用 JSON 语法创建数组
#var a = ['yeeku', 'nono']  #以英文方括号 [] 开始，依次放入数组元素，元素之间以英文逗号隔开
'''arr = [value1, value2, ...]'''


#json模块提供对JSON的支持: json模块
'''
        JSON 类型转换 Python 类型的对应关系
JSON类型                       Python类型

对象(object)                   字典(dict)
数组(array)                    列表(list)
字符串(string)                 字符串(str)
整数(number(int))              整数(int)
实数(number(real))             浮点数(float)
true                           True
false                          False
null                           None 
'''

'''
        Python类型转换JSON类型的对应关系
Python类型                      JSON类型

字典(dict)                      对象(object)
列表(list)和元组(tuple)          数组(array)
字符串(str)                     字符串(string)
整型、浮点型，以及整型、浮点型派生的枚举(float, int-& float-derived Enums)   数值型(number)
True                            true
False                           false
None                            null
'''

#json模块中常用的函数和类的功能：
'''
json.dump(obj, fp, ...): 将obj对象转换成JSON字符串输出到fp流中，fp是一个支持 write() 方法的类文件对象
json.dumps(obj, *, ...): 将obj对象转换为JSON字符串，并返回该JSON字符串
json.load(fp, *, ...): 从fp流读取JSON字符串，将其恢复成JSON对象，其中fp是一个支持write()方法的类文件对象
json.loads(s, *, ...)：将JSON字符串s恢复成JSON对象
'''

'''
#示范 dumps() 和 dump() 函数的 encode 操作(将Python对象转换成JSON字符串)
import json
#将python对象转换为JSON字符串(元组会被当成数组)
s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
print(s)  

#将简单的Python字符串转换为JSON字符串
s2 = json.dumps("\"foo\bar")
print(s2) 

#将简单的Python字符串转换为JSON字符串
s3 = json.dumps('\\')
print(s3) 

#将Python的dict对象转换为JSON字符串，并对key排序
s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
print(s4)

#将Python列表转换为JSON字符串
#并指定JSON分隔符：在逗号或冒号之后没有空格(默认有空格)
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))

#在输出的JSON字符串中，在逗号和冒号之后没有空格
print(s5)

#指定indent为4，意味着转换为 JSON 字符串有缩进
s6 = json.dumps({'Python': 5, 'Kotlin': 7}, sort_keys=True, indent=4)
print(s6)

#使用JSONEncoder 的encode方法将 Python 对象转换为 JSON 字符串
s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
print(s7)
f = open('a.json', 'w')

#使用dump()函数将转换得到的JSON字符串输出到文件中
json.dump(['Kotlin', {'Python': 'excellent'}], f)
'''



