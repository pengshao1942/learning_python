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
#json模块的dumps()函数和dump()函数的功能、所支持的选项基本相同
'''
dumps()函数直接返回转换得到的JSON字符串
dump()函数转换得到的JSON字符串输出到文件中
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

#1.使用 json.JSONEncoder对象 的encode方法将 Python 对象转换为 JSON 字符串
s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
print(s7)
f = open('a.json', 'w')

#2.直接使用dump()函数将转换得到的JSON字符串输出到文件中，比 json.JSONEncoder对象 的encode方法 更高级
json.dump(['Kotlin', {'Python': 'excellent'}], f)  #输出到D:\learning_python目录下的a.json文件中
'''

'''
#示范json模块的 loads() 和 load() 函数的 decode 操作(将JSON字符串转换成Python对象)
import json
# 将 JSON 字符串恢复成 Python 列表
result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
print(result1)

#将JSON字符串恢复成Python字符串
result2 = json.loads('"\\"foo\\"bar"')
print(result2)

#定义一个自定义的转换(恢复)函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['image'])
    return dct
#使用自定义的恢复函数
#自定义的恢复函数将real数据转换成复数的实部，将 imag 转换成复数的虚部
result3 = json.loads('{"__complex__": true, "real": 1, "image": 2}', \
    object_hook=as_complex)
print(result3)

f = open('a.json')  #打开文件
#从文件流恢复JSON列表
result4 = json.load(f)
print(result4)
'''

#python支持更多的JSON所不支持的类型，当转换JSON不支持的类型时，直接使用dumps()或dump()函数进行转换，程序会出问题
#此时就需要对JSONEncoder类进行扩展，通过扩展来完成从Python特殊类型到JSON类型的转换

'''
#示例：通过扩展JSONEncoder来实现从Python复数到JSON字符串的转换
import json
#定义 JSONEncoder 的子类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        #如果要转换的对象是复数类型，程序负责处理,将复数转换成python对象
        if isinstance(obj, complex):
            return {"__complex__": 'true', 'real': obj.real, 'img': obj.imag}  #自定义转换
        #对于其他类型，还使用 JSONEncoder默认处理
        else:  
            return json.JSONEncoder.default(self, obj)
       #return json.JSONEncoder.default(self, obj)  #省略else的写法

s1 = json.dumps(2 + 1j, cls = ComplexEncoder)  # 方法1
print(s1)
s2 = ComplexEncoder().encode(2 + 1j)  #方法2
print(s2)
'''

#扩展了JSONEncoder的子类之后，程序有两种方式使用自定义的子类
'''
1.在dumps()或dump()函数中通过cls属性指定使用JSONEncoder的自定义子类
2.直接使用JSONEncoder的自定义子类的encode()方法来执行转换
'''



#正则表达式模块re
'''
import re
print(re.__all__)
print(dir(re))
'''

#re模块中常用的正则表达式函数
'''
re.compile(pattern, flags=0):该函数用于将正则表达式字符串编译成 _sre.SRE_Pattern 对象,该对象代表了正则表达式编译之后在内存中的对象，它可以缓存
        并复用正则表达式字符串。如果程序需要多次使用同一个正则表达式字符串，则可考虑先编译它。该函数的pattern参数就是它所编译的正则表达式字符串，flags
        则代表了正则表达式的匹配旗标
'''

#编译得到的 _sre.SRE_Pattern 对象包含了 re 模块中绝大部分函数对应的方法

'''
#示例：先编译正则表达式，然后调用正则表达式的 search() 方法执行匹配
import re
#先编译正则表达式
p = re.compile('abc')
#调用_sre.SRE_Pattern对象的 search() 方法
p.search("www.abc.com")
#直接用正则表达式匹配目标字符串,此一行效果与上面两行代码结果一样
re.search('abc', 'www.abc.com')
'''

"""
re.match(pattern, string, flags=0): 尝试从字符串的开始位置来匹配正则表达式，如果从开始位置匹配不成功，match()
        函数就返回None。其中pattern参数代表正则表达式；string代表被匹配的字符串；flags则代表正则表达式的匹配旗标。
        该函数返回_sre.SRE_Match对象,该对象包含的span(n)方法用于获取第n+1个组的匹配位置，group(n)方法用于获取第n+1
        个组所匹配的子串，n默认是0，可省略
re.search(pattern, string, flags=0):扫描整个字符串，并返回字符串中第一处匹配pattern的匹配子串。其中pattern参数代表
        正则表达式;string代表被匹配的字符串；flags则代表正则表达式的匹配旗标。该函数也返回 _sre.SRE_Match 对象
"""

#示例：
'''
import re
m1 = re.match('www', 'www.fkit.org')
print(m1.span())
print(m1.group())
print(re.match('fkit', 'www.fkit.com'))

m2 = re.search('www', 'www.fkit.org')
print(m2.span())
print(m2.group())
m3 = re.search('fkit', 'www.fkit.com')
print(m3.span())
print(m3.group())
'''

"""
re.findall(pattern, string, flags=0): 扫描整个字符串，并返回字符串中所有匹配pattern的子串组成的列表。
        其中pattern参数代表正则表达式；string代表被匹配的字符串；flags则代表正则表达式的匹配旗标
re.finditer(pattern, string, flags=0):扫描整个字符串，并返回字符串中所有匹配pattern的子串组成的迭代器，
        迭代器的元素是 _sre.SRE_Match 对象。其中 pattern 参数代表正则表达式;string代表被匹配的字符串;
        flags则代表正则表达式的匹配旗标
区别在于：findall()返回列表；finditer()函数返回迭代器
"""

#案例：
'''
import re
#返回所有匹配pattern的子串组成的列表，忽略大小写
print(re.findall('fkit', 'FkIt is very good, Fkit.org is my favorite', re.I))  #re.I表示忽略大小写

#返回所有匹配pattern的子串组成的迭代器，忽略大小写
it = re.finditer('fkit', 'FkIt is very good, Fkit.org is my favorite', re.I)
for e in it:
    print(str(e.span()) + "-->" + e.group())
'''

"""
re.fullmatch(pattern, string, flags=0): 该函数要求整个字符串能匹配pattern，如果匹配则返回包含匹配信息的 _sre.SRE_Match
        对象；否则返回 None
re.sub(pattern, repl, string, count=0, flags=0): 该函数用于将string字符串中所有匹配pattern的内容替换成repl;
        repl既可是被替换的字符串，也可是一个函数。count 参数控制最多替换多少次，如果指定 count 为0，则表示全部替换
"""

#案例：演示re.sub()函数的简单用法
'''
import re
my_date = '2008-08-18'
#将my_date字符串里的中画线替换成斜线
print(re.sub(r'-', '/', my_date))  # r是原始字符串，可避免对字符串中的特殊字符进行转义
print(re.sub(r'-', '/', my_date, count=1))  #count放在后面
print(re.sub(r'-', '/', my_date, 1))  #可省略count，直接输入count的值,效果同上
'''

#所执行的替换要基于被替换内容进行改变
'''
#案例：将字符串中的每个英文单词都变成一本图书的名字
import re
#在匹配的字符串前后添加内容
def fun(matched):
    # matched就是匹配对象，通过该对象的group()方法可获取被匹配的字符串
    value = " 《疯狂" + (matched.group('lang')) + "讲义》 "  #用到了re.match的group(),组名是lang
    return value
s = 'python很好， kotlin很好'
#对s里面的英文单词(用re.A旗标控制)进行替换
#使用fun函数指定替换的内容
print(re.sub(r'(?P<lang>\w+)', fun, s, flags = re.A))  #r'(?P<lang>\w+)'  是一个正则表达式,前面的组名lang要放在<>内，re.A表示只能匹配ASCII字符，不能匹配汉字
'''


"""
re.split(pattern, string, maxsplit=0, flags=0): 使用pattern对string进行分割，该函数返回分割得到的多个子串组成的列表。其中maxsplit参数控制最多分割几次
"""

'''
#案例：示范split()函数的用法
import re
#使用逗号对字符串进行分割
print(re.split(', ', 'fkit, fkjava, crazyit'))

#指定只分割一次，被切分成两个子串
print(re.split(', ', 'fkit, fkjava, crazyit', 1))  #同样，maxsplit可以省略只输入数字，0表示全部分割

#使用a进行分割
print(re.split('a', 'fkit, fkjava, crazyit'))

#使用x进行分割，没有匹配内容，则不会执行分割
print(re.split('x', 'fkit, fkjava, crazyit'))
'''

"""
re.purge(): 清除正则表达式缓存
re.escape(pattern): 对模式中 '除ASCII字符、数值、下划线_ 之外' 的其他字符进行转义,空格也转义;转义是在前面加一个\
"""

'''
#案例：演示escape()函数的用法
import re
#对模式中的特殊字符进行转义
print(re.escape(r'www.crazyit.or1g is good, i love it!'))
print(re.escape(r'A-Zand0-9?'))
'''

#re模块中还包含两个类，分别是正则表达式对象(具体类型为 _sre.SRE_Pattern)和匹配(Match)对象，其中正则表达式对象就是调用re.compile()函数的返回值。
#该对象的方法与前面re模块中的函数大致对应

'''
#案例：使用正则表达式的方法来执行匹配
import re
#编译得到正则表达式对象
pa = re.compile('fkit')  #后面可多次使用pa对象(它缓存了正则表达式)来执行匹配，而不用 re.
#调用match方法，原本应该从开始位置匹配
#此处指定从索引4的地方开始匹配，可以匹配成功,正好从f开始匹配
print(pa.match('www.fkit.org', 4).span())  #re.match() 的 span()方法

#此处指定从索引4到索引6之间执行匹配，匹配失败，只有fk(不算索引6的字母i)，匹配失败
print(pa.match('www.fkit.org', 4, 6))

#此处指定从索引4到索引8之间执行全匹配，匹配成功，正好匹配到fkit
print(pa.fullmatch('www.fkit.org', 4, 8).span())
'''

'''使用编译正则表达式的好处：使用 complile() 函数编译正则表达式之后，该函数所返回的对象就会缓存该正则表达式，从而可以多次利用
该正则表达式执行匹配。'''

'''re模块中的Match对象(其具体类型为 _sre.SRE_Match)则是match()、search()方法的返回值,该对象中包含了详细的正则表达式匹配信息
,包括正则表达式匹配的位置、正则表达式所匹配的子串'''

"""
_sre.SRE_Match 对象包含了如下方法或属性：
    match.group([group1, ...]):获取该匹配对象中指定组所匹配的字符串
    match.__getitem__(g):这是match.group(g)的简化写法。由于match对象提供了__getitem__()方法，因此程序可使用match[g]来代替match.group(g)
    match.groups(default=None):返回match对象中所有组所匹配的字符串组成的元组
    match.groupdict(default=None):返回match对象中所有组所匹配的字符串组成的字典
    match.start([group]):获取该匹配对象中指定组所匹配的字符串的开始位置
    match.end([group]):获取该匹配对象中指定组所匹配的字符串的结束位置
    match.span([group]):获取该匹配对象中指定组所匹配的字符串的开始位置和结束位置。该方法相当于同时返回start()和end()方法的返回值
"""

#组 是正则表达式中常见的：用圆括号将多个表达式括起来形成组。如果正则表达式中没有圆括号，那么整个表达式就属于一个默认组

'''
#示例：演示正则表达式中组的使用
import re
#在正则表达式中使用组
m = re.search(r'(fkit).(org)', r'www.fkit.org is a good domain')  #r'(fkit).(org)'  是一个正则表达式，包含两个组(fkit)和(org)
print(m.group(0))

#调用的简化方法，底层是调用m.__getitem__(0)
print(m[0])
print(m.span(0))
print(m.group(1))

#调用的简化写法，底层是调用 m.__getitem__(1)
print(m[1])
print(m.span(1))
print(m.group(2))

#调用的简化写法，底层是调用m.__getitem__(2)
print(m[2])
print(m.span(2))
#返回所有组所匹配的字符串组成的元组
print(m.groups())


"""如果在正则表达式中为组指定了名字(用?P<名字>为正则表达式的组指定名字)，就可以调用groupdict()方法来获取所有组所匹配的字符串组成的字典---其中组名作为字典的key
为正则表达式定义了两个组，并为组指定了名字"""

m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)',\
    r"www.fkit.org is a good domain")
print(m2.groupdict())  #返回一个字典，组名为key,组所匹配的子串为value
'''

'''
match.pos: 该属性返回传给正则表达式对象的search()、match()等方法的pos参数
match.endpos: 该属性返回传给正则表达式对象的search()、match()等方法的endpos参数
match.lastindex: 该属性返回最后一个匹配的捕获组的整数索引。如果没有组匹配，该属性返回None。例如用(a)b、((a)(b))或((ab))对字符串'ab'执行匹配，
        该属性都会返回1;但如果使用(a)(b)正则表达式对'ab'执行匹配，则 lastindex 等于2。
match.lastgroup: 该属性返回最后一个匹配的捕获组的名字；如果该组没有名字或根本没有组匹配，该属性返回None
match.re: 该属性返回执行正则表达式匹配时所用的正则表达式
match.string:该属性返回执行正则表达式匹配时所用的字符串
'''








