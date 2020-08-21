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
my_data = '2008-08-18'
#将my_data字符串里的中画线替换成斜线
print(re.sub(r'-', '/', my_data))  # r是原始字符串，可避免对字符串中的特殊字符进行转义
print(re.sub(r'-', '/', my_data, count=1))  #count放在后面
print(re.sub(r'-', '/', my_data, 1))  #可省略count，直接输入count的值,效果同上
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

"""
match.pos: 该属性返回传给正则表达式对象的search()、match()等方法的pos参数
match.endpos: 该属性返回传给正则表达式对象的search()、match()等方法的endpos参数
match.lastindex: 该属性返回最后一个匹配的捕获组的整数索引。如果没有组匹配，该属性返回None。例如用(a)b、((a)(b))或((ab))对字符串'ab'执行匹配，
        该属性都会返回1;但如果使用(a)(b)正则表达式对'ab'执行匹配，则 lastindex 等于2。
match.lastgroup: 该属性返回最后一个匹配的捕获组的名字；如果该组没有名字或根本没有组匹配，该属性返回None
match.re: 该属性返回执行正则表达式匹配时所用的正则表达式
match.string:该属性返回执行正则表达式匹配时所用的字符串
"""

#正则表达式旗标
#正则表达式旗标都使用该模块中的属性来代表：

"""
re.A 或 re.ASCII: 该旗标控制\w, \W, \b, \B, \d, \D, \s 和 \S 只匹配 ASCII 字符，而不匹配所有的Unicode字符。也可以在正则表达式中使用(?a)行内旗标来代表
re.DEBUG: 显示编译正则表达式的 Debug 信息。没有行内旗标
re.I 或 re.IGNORECASE: 使用正则表达式匹配时不区分大小写。对应于正则表达式中的(?i)行内旗标
"""

'''
#案例：
import re
#默认区分大小写，所以无匹配
print(re.findall(r'fkit', 'Fkit is a good domain, FKIT is good'))
#使用re.I指定区分大小写
print(re.findall(r'fkit', 'Fkit is a good domain, FKIT is good', re.I))
'''

"""
re.L 或 re.LOCALE: 根据当前区域设置使用正则表达式匹配时不区分大小写。该旗标只能对 bytes 模式起作用，对应于正则表达式中的(?L)行内旗标
re.M 或 re.MULTILINE: 多行模式的旗标。当指定该旗标后, "^" 能匹配字符串的开头和每行的开头(紧跟在每一个换行符的后面); "$" 能匹配字符串的末尾和每行的末尾(在每一个换行符之前)
        默认情况下，"^" 只匹配字符串的开头， "$" 只匹配字符串的结尾，或者匹配到字符串默认的换行符(如果有)之前。对应于正则表达式中的(?m)行内旗标
re.S 或 s.DOTALL: 让点(.)能匹配包括换行符在内的所有字符，如果不指定该旗标，则点(.)能匹配不包括换行符的所有字符。对应于正则表达式中的(?s)行内旗标
re.U 或 re.Unicode: 该旗标控制\w, \W, \b, \B, \d, \D, \s 和 \S 能匹配所有的Unicode字符。这个旗标在 Python3.x中是多余的，因为Pyhon3.x默认就是
        匹配所有的Unicode字符
re.X 或 re.VERBOSE: 通过该旗标允许 '分行' 书写正则表达式，也允许为正则表达式 '添加注释',从而提高正则表达式的可读性。对应于正则表达式中的(?x)行内旗标
"""

'''
#案例：下面2个正则表达式匹配的结果是一样的
import re
a = re.compile(r"""020  #广州的区号
            \-   #中间的短横线
            \d{8}  #8个数值""", re.X)   #re.X旗标
b = re.compile(r'020\-\d{8}')
print(a.match('020-25456456g'))
print(b.match('020-25456456g'))
'''


#创建正则表达式

#正则表达式所支持的合法字符
"""
x          字符x(x可代表任意合法的字符)
\t         制表符(*\u0009*)
\n         新行(换行)符 (*\u000A*)
\r         回车符(*\u000D*)
\f         换页符(*\u000C*)
\a         报警(bell)符(*\u0007*)
\e         Escape符(*\u001B*)
\cx        x对应的控制符。例如, \cM 匹配 Ctrl+M。 x值必须为A-Z 或 a~z 之一
"""
#  \uhhhh     十六进制值0xhhhh所表示的Unicode字符

#正则表达式的特殊字符：---省略---，匹配特殊字符,在特殊字符前加转义符 \
"""
$          匹配一行的结尾。要匹配 $ 字符本身，请使用 \$
^          匹配一行的开头。要匹配 ^ 字符本身，请使用 \^
()         标记子表达式(也就是组)的开始位置和结束位置。要匹配这些字符，请使用 \( 和 \)
[]         用于确定中括号表达式的开始位置和结束位置。要匹配这些字符,请使用 \[ 和 \]
{}         用于标记前面子表达式的出现频度。要匹配这些字符,请使用 \{ 和 \}
*          指定前面子表达式可以出现零次或多次。要匹配 * 字符本身，请使用 \*
+          指定前面子表达式可以出现一次或多次。要匹配 + 字符本身, 请使用 \+
?          指定前面子表达式可以出现零次或一次。要匹配 ? 字符本身，请使用 \?
.          匹配除换行符 \n 之外的任意单个字符。要匹配 . 字符本身，请使用 \.
\          用于转义下一个字符，或指定八进制、十六进制字符。如果需匹配 \ 字符，请使用 \\
|          指定在两项之间任选一项。如果要匹配 | 字符本身，请使用 \|
"""

#正则表达式支持的预定义字符(也称为通配符)：
"""
.       默认可匹配除换行符之外的任意字符，在使用 re.S 或 s.DOTALL 旗标之后，它还可匹配换行符
\d      匹配 0~9 的所有数字
\D      匹配非数字
\s      匹配所有的空白字符，包括空格、制表符、回车符、换页符、换行符等
\S      匹配所有的非空白字符
\w      匹配所有的单词字符，包括 0~9 的所有数字、26个英文字母和下划线 _
\W      匹配所有的非单词字符
"""

#案例：使用通配符创建更强的正则表达式
'''
>> import re
>> re.fullmatch(r'c\wt', 'cat')
>> re.fullmatch(r'c\wt', 'c9t')
#匹配如 000-000-0000 形式的电话号码
>> re.fullmatch(r'\d\d\d-\d\d\d-\d\d\d\d', '123-456-8888') 
'''

#方括号表达式
"""
表示枚举        例如：[abc],表示a, b, c其中任意一个字符
表示范围        例如：[a-f],表示a~f范围内的任意字符；[\\u0041-\\u0056],表示所有的中文字符
表示求否: ^     例如：[^abc],表示非 a、b、c 的任意字符；[^a-f],表示不是 a~f 范围内的任意字符
"""

#边界匹配符
"""
^               行的开头
$               行的结尾
\b              单词的边界，即只能匹配单词前后的空白
\B              非单词的边界,即只能匹配不在单词前后的空白
\A              只匹配字符串的开头
\Z              只匹配字符串的结尾,仅用于最后的结束符
"""

#子表达式：用圆括号将多个表达式组成
#在圆括号中可以使用 或 运算符(|)
#子表达式(组)支持如下用法：
"""
(exp): 匹配 exp 表达式并捕获成一个自动命名的组，后面可通过 "\I" 引用第一个捕获组所匹配的子串，通过"\2"引用第二个捕获
        组所匹配的子串......依此类推
"""

'''
#例如：
import re
print(re.search(r'Windows (95|98|NT|2000) [\w ]+\1', 'Windows 98 published in 98'))  #\1必须是第一个组匹配的内容，这里是98
#改为如下形式：此时第一个组匹配的是98，\1 应该引用子串98，故该正则表达式无法匹配"Windows 98 published in 95",返回None
print(re.search(r'Windows (95|98|NT|2000) [\w ]+\1', 'Windows 98 published in 95'))
'''

"""
(?P<name>exp): 匹配exp表达式并捕获成命名组，该组的名字为 name.后面可通过(?P=name)来引用前面捕获的组。
        (?P<name>exp)捕获的组指定了名称，后面可通过<?P=name>的方式来引用命名组所匹配的子串
(?P=name): 引用name命名组所匹配的子串
"""

'''
#例如：
import re
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))  #tag是组名,第一个\w+ 是exp,第二个\w+是正则，(?P=tag)用于引用前面的tag组所匹配的子串
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h2>'))  #不能匹配，因为前后2个标签不相同
'''

"""
(?:exp): 匹配exp表达式并且不捕获。这种组与(exp)的区别就在于它是不捕获的，因此不能通过\1、\2等来引用
"""

'''
#例如：
import re
print(re.search(r'Windows (?:95|98|NT|2000) [a-z ]+', 'Windows 98 published in 98'))
#错误的示范:这里不能通过\1、\2等来引用
#print(re.search(r'Windows (?:95|98|NT|2000)[a-z ]+\1', 'Windows 98 published in 98'))  
'''

"""
(?<=exp)：括号中的子模式必须出现在匹配内容的左侧，但exp不作为匹配的一部分
(?=exp): 括号中的子模式必须出现在匹配内容的右侧，但exp不作为匹配的一部分
"""

'''
#例如：获取HTML代码中<h1>元素中的内容
import re
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help! <h1>fkit.org</h1>! technology'))  #
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help! <h1><div>fkit</div></h1>! technology'))
'''

"""
(?<!exp): 括号中的子模式必须不出现在匹配内容的左侧，但exp不作为匹配的一部分。其实它是 (?<=exp) 的逆向表达
(?!exp)：括号中的子模式必须不出现在匹配内容的右侧，但 exp 不作为匹配的一部分。其实它是 (?=exp) 的逆向表达
(?#comment): 注释组。"?#" 后的内容是注释，不影响正则表达式本身,comment可以自定义
"""

'''
#例如：(?#comment) 的应用，匹配注释
import re
print(re.search(r'[a-zA-Z0-9_]{3,}(?#username)@fkit\.org', 'sun@fkit.org'))  #[a-zA-Z0-9_]表示匹配大小写字母数字下划线任意，{3,}表示前面的子表达式匹配3次
'''

"""
(?aiLmsux): 旗标组，用于为整个正则表达式添加行内旗标，可同时指定一个或多个旗标, aiLmsux 每个字母是一个旗标
"""

'''
#例如：
import re
print(re.search(r'(?i)[a-z0-9_]{3,}(?#username)@fkit\.org', 'Sun@FKIT.ORG'))  #(?i)组，i旗标表示匹配结果不区分大小写
'''

"""
(?imsx-imsx:exp): 只对当前组起作用的旗标。只影响组内的子表达式
"""

'''
#例如：
import re
#print(re.search(r'(?i:[a-z0-9_]){3,}@fkit\.org', 'Sun@fkit.org'))  #(?i:[a-z0-9_])是一个组，该组内的表达式不区分大小写,即sun不区分大小写,但组外的fkit还是区分大小写
#print(re.search(r'([a-z0-9_]){3,}@fkit\.org', 'Sun@fkit.org', re.I))   #效果同上，re.I 对应于 旗标：组内(?i)
#如果在旗标前应用 - ，则表示去掉旗标
print(re.search(r'(?-i:[a-z0-9_]){3,}@fkit\.org', 'sun@Fkit.org', re.I))  #re.I表示整个表达式不区分大小写，而 (?-i:exp)由表示去掉re.I,因此组内的表达式还是区分大小写
'''


#正则表达式的 贪婪模式 和 勉强模式
#Python正则表达式支持如下几种频度限定：
"""
*：限定前面的子表达式可出现 0~N 次。例如正则表达式 r'zo*' 能匹配 'z',也能匹配 'zoo'、'zooo'等。* 等价于{0,}
+: 限定前面的子表达式出现 1~N 次。例如正则表达式 r'zo+' 不能匹配 'z' ,可匹配 'zo'、'zoo'、'zooo'等 。+ 等价于 {1,}
?: 限定前面的子表达式出现 0~1 次。例如正则表达式 r'zo?' 能匹配 'z' 和 'zo' 两个字符串。 ? 等价于{0,1}
{n,m}: n和m均为非负整数,其中 n<=m,限定前面的子表达式出现 n~m 次。例如正则表达式 r'fo{1,3}d' 可匹配 'fod'、'food'、'foood'这三个字符串
{n,}: n是一个非负整数,限定前面的子表达式 至少 出现n次。例如正则表达式 r'fo{2,}d' 可匹配 'food'、'foood'、'fooood'等字符串
{,m}: m是一个非负整数，限定前面对的子表达式 至多 出现m次。例如正则表达式 r'fo{,3}d' 可匹配 'fd'、'fod'、'food'、'foood'这四个字符串
{n}: n是一个非负整数,限定前面的子表达式 必须 出现n次。例如正则表达式 r'fo{2}d' 只能匹配 'food' 字符串

"""
#例如：匹配电话号码xxx-xxx-xxxx格式
#r'\d{3}-\d{3}-\d{4}'

#正则表达式的频度限定默认是贪婪模式的：即表达式中的模式会尽可能多地匹配字符

'''
#例如：
import re
print(re.search(r'@.+\.', 'sun@fkit.com.cn'))  #贪婪模式，尽可能多地匹配,只要最后有一个.即可，匹配结果是：@fkit.com.
print(re.search(r'@.+?\.', 'sun@fkit.com.cn')) #勉强模式，尽可能少地匹配。最少是1，故结果为：@fkit.
'''



#容器相关类
#集合和双端队列
#双端队列(deque)的特征是它的两端都可以添加、删除元素，它既可作为栈(stack)使用，也可作为队列(queue)使用
#集合(set)：不记录元素的添加顺序、元素不允许重复、是可变容器，程序可以改变容器中的元素
#frozenset集合：是set的不可变版本，它的元素是不可变的

#print([e for e in dir(set) if not e.startswith('_')])

'''
#案例：演示集合set的用法

#使用花括号构建set集合
c = {'白骨精'}
#添加元素
c.add("孙悟空")
c.add(6)
print("c集合的元素的个数为：" , len(c))

c.remove(6)
#c.remove('nihao')  #移除集合中不存在的元素时，使用集合的remove()方法报KeyErro异常，且程序中止
c.discard('ene')  #移除集合中不存在的元素时，使用集合的discard()方法无异常提示，什么也不做
c.discard('白骨精')
print("c集合现在的元素的个数为：" , len(c))
#判断是否包含指定字符串
print("c集合是否包含'孙悟空'字符串:", ("孙悟空" in c))   #输出True
print("c集合的元素：", c)

#使用 set()函数 (构造器) 来创建 set 集合
books = set()  #set() 表示空集合
books.add("轻量级Java EE企业应用实战")
print("books集合的元素: ", books)

#使用issubset()方法判断是否为子集合
print("books集合是否为c的子集合?", books.issubset(c))
#issubset()方法与<=运算符的效果相同
print("books集合是否为c的子集合?", (books <= c))

#使用issuperset()方法判断是否为父集合
#issubset 和 issuperset 其实就是相互倒过来判断
print("c集合是否完全包含books集合?", (c >= books))
#用c集合减去books集合里的元素，不改变c集合本身
result1 = c - books
print(result1)

#difference()方法也是对集合做减法，与用"="执行运算的效果完全一样
result2 = c.difference(books)
print(result2)
#用c集合减去books集合里的元素，改变c集合本身
c.difference_update(books)
print("c集合的元素: ", c)

#删除c集合里的所有元素
c.clear()
print("c集合的元素: ", c)

#直接创建包含元素的集合
d = {"疯狂Java讲义", '疯狂Python讲义', '疯狂Kotlin讲义'}
print("d集合的元素: ", d)

#计算两个集合的交集,不改变d集合本身
inter1 = d & books
print(inter1)
#intersection()方法也是获取两个集合的交集，与用"&"执行运算的效果完全一样
inter2 = d.intersection(books)
print(inter2)

#计算两个集合的交集，改变d集合本身
d.intersection_update(books)
print("d集合的元素：", d)

#将range对象包装成set集合
e = set(range(5))
f = set(range(3, 7))
print("e集合的元素：", e)
print("f集合的元素：", f)

#对两个集合执行异或运算
xor = e ^ f
print('e和f执行xor的结果：', xor)

#计算两个集合的并集，不改变e集合本身
un = e.union(f)
print('e和f执行并集的结果：', un)

#计算两个集合的并集，改变e集合本身
e.update(f)
print('e集合的元素：', e)
'''

#上面示范了集合支持的几个运算符
"""
<= : 相当于调用 issubset() 方法，判断前面的set集合是否为后面的set集合的子集合
>= : 相当于调用 issuperset() 方法,判断前面的set集合是否为后面的set集合的父集合
- ：相当于调用 difference() 方法，用前面的set集合减去后面的set集合的元素
& ：相当于调用 intersection() 方法,用于获取两个set集合的交集
^ : 计算两个集合异或的结果，就是用两个集合的并集减去交集的元素
"""

#set集合支持进行集合运算来改变集合内的元素
"""
交集运算：intersection() 和 intersection_update(), 前者不改变集合本身，而是返回两个集合的交集；后者会通过
            交集运算改变第一个集合
并集运算：union() 和 update(), 前者不改变集合本身，而是返回两个集合的并集;后者会通过并集运算改变第一个集合
减法运算：difference() 和 difference_update(),前者不改变集合本身,而是返回两个集合做减法的结果；后者改变第一个集合
"""

#frozenset是set的不可变版本，因此set集合中所有能改变集合本身的方法，frozenset都不支持;set集合中不改变集合本身的方法，frozenset都支持
#print([e for e in dir(frozenset) if not e.startswith('_')])   #查看frozenset支持的方法

#frozenset作用主要有两点：
"""
当集合元素不需要改变时，使用 frozenset 代替 set 更安全
当某些 API 需要不可变对象时,必须用frozenset 代替 set。比如 dict 的key必须是不可变对象，因此只能用 frozenset;
再比如set本身的集合元素必须是不可变的，因此 "set不能包含set,set只能包含frozenset"
"""

'''
#案例：set不能包含set,set只能包含frozenset
s = set()
frozen_s = frozenset('Kotlin')  #定义frozenset不可变集合
#为set集合添加frozenset
s.add(frozen_s)
print('s集合的元素: ', s)
sub_s = {'python'}
#为set集合添加普通set集合，程序报错
s.add(sub_s)   #报错：TypeError: unhashable type: 'set'
'''


#栈：是一种特殊的线性表，只允许在一端进行插入、删除操作，这一段被称为栈顶(top)，另一端则被称为栈底(bottom)
#队列：也是一种特殊的线性表,只允许在表的前端(front)进行删除操作，在表的后端(rear)进行插入操作
#进行插入操作的端被称为队尾，进行删除操作的端被称为队头；其内的元素遵循先进先出(FIFO)的规则

#双端队列(deque)： 代表一种特殊的队列，可以在两端同时进行插入、删除操作

#对一个双端队列：如果程序将所有的插入、删除操作都固定在一端进行，那么这个双端队列就变成了栈；如果固定在一端只添加元素，在另一端只删除元素，就变成了队列

#deque 位于 collections 包下
'''
from collections import deque
print([e for e in dir(deque) if not e.startswith('_')])   #查看deque的全部方法,基本都有2个版本的方法
'''

#deque的左边(left)相当于队列头(front)，右边(right)相当于队列尾(rear)
"""
append 和 appendleft: 在deque的右边或左边添加元素，也就是默认在队列尾添加元素
pop 和 popleft: 在deque的右边或左边弹出元素，也就是默认在队列尾部弹出元素
extend 和 extendleft: 在deque的右边或左边添加多个元素，也就是默认在队列尾添加多个元素
"""

#deque中的clear()方法用于清空队列; insert() 方法则是线性表的方法，用于在指定位置插入元素

#案例：把deque当成栈来使用
'''
from collections import deque
stack = deque(('Kotlin', 'Python'))  #创建一个双端队列，deque() 函数
#元素入栈：
stack.append('Erlang')
stack.append('Swift')
print('stack中的元素: ', stack)
#元素出栈，后添加的元素先出栈(栈元素:先入后出)
print(stack.pop())
print(stack.pop())
print(stack)
'''

#案例：把deque当成队列来使用，意味着一端只用来添加元素，另一端只用来删除元素
'''
from collections import deque

q = deque(('Kotlin', 'Python'))
#元素入队列（默认从右边入队）
q.append('Erlang')
q.append('Swift')

print('q中的元素： ', q)
#元素出队列, 先添加的元素先出队列（默认从左边出队）
print(q.popleft())
print(q.popleft())
print(q)
'''


#deque的rotate()方法：将队列的队尾元素移动到队头，使之首尾相连
'''
from collections import deque
q = deque(range(5))
print('q中的元素: ', q)
#执行旋转，使之首尾相连
q.rotate()
print('q中的元素：', q)
#再次执行旋转，使之首尾相连
q.rotate()
print('q中的元素: ', q)
'''



#Python的堆操作：
#小顶堆(大根堆)：正二叉树
#大顶堆(小根堆)：倒二叉树
'''
正二叉树的特点：树中所有节点的值都 小于 其左、右子节点的值，根节点的值最小
倒二叉树的特点：树中所有节点的值都 大于 其左、右子节点的值，根节点的值最大
'''
#小顶堆的任意子树也是小顶堆，大顶堆的任意子树还是大顶堆
#Python对list中的元素进行小顶堆排列： 即每次获取堆中的元素时，总是取得堆中最小的元素
#Python提供的heapq包中有一些函数，当程序用这些函数来操作列表时，该列表就会表现出 "堆" 的行为


'''
import heapq
print([e for e in dir(heapq) if not e.startswith('_')])  #查看heapq包下的全部函数
'''

"""heap代表堆名
heappush(heap, item): 将 item 元素加入堆
heappop(heap): 将堆中最小元素弹出
heapify(heap): 将堆属性应用到列表上
heapreplace(heap, x)：将堆中最小元素弹出，并将元素 x 入堆
merge(*iterables, key=None, reverse=False): 将多个有序的堆合并成一个大的有序堆，然后再输出
heappushpop(n, iterable, key=None): 返回堆中最大的 n 个元素
nsmallest(n, iterable, key=None): 返回堆中最小的 n 个元素
"""

'''
#案例：示范上述函数的用法
from heapq import *
my_data = list(range(10))
my_data.append(0.5)
#此时 my_data 依然是一个 list 列表
print('my_data 的元素：', my_data)

#对my_data应用堆属性
heapify(my_data)
print('应用堆之后my_data的元素: ', my_data)

heappush(my_data, 7.2)
print('添加7.2之后my_data的元素：', my_data)
print('列表中最小的3个元素是:', nsmallest(3, my_data, key=None))

#从堆中弹出最小的元素
print(heappop(my_data))  # 0
print(heappop(my_data)) # 0.5
print('弹出两个元素之后my_data的元素：', my_data)

#弹出最小的元素,压入指定元素
print(heapreplace(my_data, 8.1))
print('执行replace之后my_data的元素: ', my_data)

#获取最大、最小的n个元素
print('my_data中最大的3个元素: ', nlargest(3, my_data))
print('my_data中最小的4个元素: ', nsmallest(4, my_data))
'''



#collections下的容器支持
#ChainMap对象：工具类，使用链的方式将多个dict "链" 在一起，并未真正的合并它们，从而允许程序可直接获取任意一个dict所包含的key对应的value
#ChainMap链接的dict中排在"链"前面的dict中的key具有更高的优先级

'''
#案例：释放ChainMap的用法
from collections import ChainMap   #导入

#定义三个dict对象
a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}

#将三个dict对象链在一起，就像变成了一个大的dict,这里a的优先级最高,c的优先级最低
cm = ChainMap(a, b, c)
print(cm)

#获取Kotlin对应的value
print(cm['Kotlin'])
#获取Python对应value
print(cm['Python'])  #当多个dict中有重复的key时,取优先级最高的dict中的key对应的value
#获取Go对应的value
print(cm['Go'])  
'''

#案例：将局部范围的定义、全局范围的定义、Python内置定义链成一个ChainMap,当程序通过该ChainMap获取变量时,将会按照局部定义、全局定义、内置定义的顺序执行搜索
'''
from collections import ChainMap
import builtins
from time import localtime
my_name = '孙悟空'
def test():
    my_name = 'yeeku'
    #将 locals、globals、builtins 的变量链成ChainMap
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    #访问my_name对应的value,优先使用局部范围的定义
    print(pylookup['my_name'])
    #访问len对应的value,由于在局部范围、全局范围中都找不到，因此访问内置定义的len函数
    print(pylookup['len'])
test()
'''

#案例：示范 优先使用运行程序的指定参数,然后是系统环境变量,最后才使用系统默认值的实现

'''
#改示例文件：ChainMap_test.py
from argparse import Namespace
from collections import ChainMap
import os, argparse
#定义默认参数
defaults = {'color': '蓝色', 'user': 'yeeku'}
#创建程序参数解析器
parser = argparse.ArgumentParser()
#为参数解析器添加-u(--user)和 -C(--color)参数
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
#解析运行程序的参数
Namespace = parser.parse_args
#将程序参数转换成dict
command_line_args = {k:v for k, v in vars(Namespace).items() if v}
#将command_line_args(由程序参数解析而来)、os.environ(环境变量)、defaults链成ChinaMap
combined = ChainMap(command_line_args, os.environ, defaults)
#获取color对应的value
print(combined['color'])
#获取user对应的value
print(combined['user'])
#获取PYTHONPATH对应的value
print(combined['PYTHONPATH'])
#在命令行指定参数的优先级是最高的
#python  ChainMap_test.py -c 红色 -u Charlie    #在命令行执行
#python  ChainMap_test.py #不带参数执行该文件，程序输出的是defaults字典中key对应的值
'''



#Counter对象
#Counter工具类：可以自动统计容器中各元素出现的次数
#Counter本质是一个特殊的dict，它的key都是其所包含的元素，而它的value则记录了该key出现的次数
#通过Counter并不存在的key访问value，将会输出0---代表该key出现了0次
'''可通过任何可迭代对象参数来创建Counter对象，Counter将会自动统计各元素出现的次数，并以元素为key，出现的
次数为value来构建Counter对象'''

#案例：
'''
from collections import Counter
#创建空的Counter对象
c1 = Counter()
#以可迭代对象(字符串)创建Counter对象
c2 = Counter('hannah')
print(c2)
#以可迭代对象(列表)创建Counter对象
c3 = Counter({'Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'})
print(c3)
#以dict来创建Counter对象，dict也是可迭代对象
c4 = Counter({'red': 4, 'blue': 2})
print(c4)
#使用关键字参数的语法创建Counter
c5 = Counter(Python=4, Swift=8)
print(c5)
'''

#Counter继承了dict类，完全可以调用dict所支持的方法
#Counter还提供了如下三个常用的方法：
'''
elements(): 该方法返回该Counter所包含的全部元素组成的迭代器
most_common([n]): 该方法返回Counter中出现最多的n个元素
subtract([iterable-or-mapping]): 该方法计算Counter的减法，其实就是计算减去之后各元素出现的次数
'''

#案例：示范Counter类中上述方法的用法
'''
from collections import Counter
#创建Counter对象
cnt = Counter()
#访问并不存在的key,将输出该key的次数为0
print(cnt['Python'])

for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)
#只访问Counter对象的元素,返回全部元素组成的迭代器
print(list(cnt.elements()))

#将字符串(迭代器)转换成Counter
chr_cnt = Counter('abracadabra')
#获取出现最多的字母 
print(chr_cnt.most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
#用Counter对象执行减法，其实就是减少各元素出现的次数
c.subtract(d)
print(c)

e = Counter({'x': 2, 'y': 3, 'z': -4})
#调用del删除key-value对，会真正删除该key-value对
del e['y']
print(e)

#访问'w'对应的value,'w'没有出现过，因此返回0
print(e['w'])
#删除e['w'],删除该key-value对，删除不存在key-value对，不报错
del e['w']
#再次访问'w'对应的value, 'w'还是没出现，因此返回0
print(e['w'])
'''


'''对Counter对象的其他常用操作：转换成set(集合)、list(列表)、dict(字典)等，还可对Counter执行加、减、交、并运算，对
Counter进行求正、求负运算等'''

'''
加：将两个Counter对象中各key出现的次数相加，且只保留出现次数为正的元素
减：将两个Counter对象中各key出现的次数相加，且只保留出现次数为负的元素
交: 取两个Counter对象中都出现的key且各key对应的次数的最小数
并：取两个Counter对象中各key对应的出现次数的最大数
求正：只保留Counter对象中出现次数为0或正数的key-value对
求负：只保留Counter对象中出现次数为负数的key-value对，并将出现次数改为正数
'''

#案例：示范对Counter对象的上述常用操作
'''
from collections import Counter

#创建Counter对象
c = Counter(Python=4, Swift=2, Kotlin=3, Go=-2)
#统计Counter中所有元素出现次数的总和
print(sum(c.values()))

#将Counter转换为list，只保留各key
print(list(c))
#将Counter转换为set,只保留各key
print(set(c))
#将Counter转换为dict
print(dict(c))
#将Counter转换为list,列表元素都是(元素，出现次数)组
list_of_pairs = c.items()
print(list_of_pairs)
#将列表元素为(元素，出现次数)组的list转换成Counter
c2 = Counter(dict(list_of_pairs))
print(c2)
#获取Counter中最少出现的三个元素
print(c.most_common())
#清空所有key-value对
c.clear()
print(c)
c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)
#对Counter执行加法
print(c + d)
#对Counter执行减法，2个Counter中都有的元素才运算
print(c - d)
Counter({'a': 2})
#对Counter执行交运算
print(c & d)
print(c | d)
print(+c)
print(-d)
'''



#defaultdict对象
#defaultdict是dict的子类，也可被当成dict来使用，dict支持的功能，defaultdict基本都支持
#defalutdict可以提供一个default_factory属性，该属性所指定的函数负责为不存在的key来生成value，故相比dict它可以访问不存在的key

#案例：对比defalutdict 和 dict 在访问不存在的key对应的value时的处理情况
'''
from collections import defaultdict

my_dict = {}
#使用int作为defaultdict的default_factory
#当key不存在时,将会返回int函数的返回值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a'])   #不会报异常，会赋予不存在的key一个value，value是defaultdict(int)返回的值
print(my_dict['a'])  #会报异常
'''

#案例：为defaultdict中不存在的key设置默认的value
#假如程序中包含多个key-value对，有些key是重复的，现需要对这些key-value对进行整理；key对应一个list，该list中包含这组数据中该key对应的所有value

'''
from collections import defaultdict
s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
#创建defaultdict，设置由list函数来生成默认值
d = defaultdict(list)  
for k, v in s:
    #直接访问 defaultdict 中指定的key对应的value即可
    #如果该key不存在，defaultdict会自动为该key生成默认值
    d[k].append(v)
print(list(d.items()))
'''


#namedtuple工厂函数
'''#namedtuple()是一个工厂函数，使用该函数可以创建一个tuple类的子类，该子类可以为tuple的每个元素都指定字段名
,这样程序就可以根据字段名来访问namedtuple的各元素了'''
#如果需要，程序依然可以根据索引来访问 namedduple的各元素

#namedtuple函数的语法格式如下
'''namedtuple(typename, field_name, *, verbose=False, rename=False, module=None)'''

"""各项参数说明
typename: 该参数指定所创建的tuple子类的类名，相当于用户定义了一个子类
field_names: 该参数是一个字符串序列,如['x', 'y'],也可直接使用单个字符串代表所有字段名，多个字段名用空格、逗号隔开。任何有效的Python标识符都可作为字段名
rename: 如果将该参数设为True，那么无效的字段名将会被自动替换为位置名。例如：指定['abc', 'def', 'ghi', 'abc'],它将会被替换为['abc', '_1', 'ghi', '_3'],
            因为def字段名是关键字，而abc字段名重复了
verbose: 如果该参数被设置为True,那么当该子类被创建之后，该类定义就会被立即打印出来
module: 如果设置了该参数，那么该类将位于该模块下，因此该自定义类的 __module__ 属性将被设为该参数值
"""

#示例：使用namedtuple工厂函数来创建命名元组

'''
from collections import namedtuple
#定义命名元组类： Point
Point = namedtuple('Point', ['x', 'y'])
#初始化Point对象，既可用位置参数，也可用命令参数
p = Point(11, y=22)
#像普通元组一样根据索引访问元素
print(p[0] + p[1])
#执行元组解包，按元素的位置解包
a, b = p
print(a, b)
#根据字段名访问各元素
print(p.x + p.y)
print(p)
'''


#命名元素的其他方法和属性：
"""
_make(iterable): 类方法。该方法用于根据序列或可迭代对象创建命名元组对象
_asdict(): 将当前命名元组对象转换为OrderedDict字典
_replace(**kwargs): 替换命令元组中一个或多个字段的值
_source: 该属性返回定义该命名元组的源代码
_fields：该属性返回该命名元组中所有字段名组成的元组
"""

#示例：示范上面方法和属性的用法
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

my_data = ['East', 'North']
#创建命名元组对象
p2 = Point._make(my_data)
print(p2)
#将命名元组对象转换成OrderedDict
print(p2._asdict())
#替换命名元组对象的字段值
p2._replace(y='South')
print(p2)
#输出p2包含的所有字段
print(p2._fields)
#定义一个命名元组类
Color = namedtuple('Color', 'red green blue')
#再定义一个命名元组类，其字段有Point的字段加上Color的字段组成
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
#创建Pixel对象，分别为x、y、red、green、blue字段赋值
pix = Pixel(11, 22, 128, 255, 0)
print(pix)
'''


#OrderedDict对象: 也是dict的子类，它可以 "维护" 添加key-value对的顺序。即先添加的key-value对排在前面，后添加的key-value对排在后面
#即使两个OrderedDict中的key-value对完全相同，但只要它们的顺序不同，程序在判断它们是否相等时也依然会返回false

#示例：
'''
from collections import OrderedDict
#创建OrderedDict对象
dx = OrderedDict(b=5, c=2, a=7)
print(dx)
d = OrderedDict()
#向OrderedDict中添加key-value对
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
#遍历OrderedDict的key-value对
for k, v in d.items():
    print(k, v)

#即使两个OrderedDict中的key-value对完全相同，但只要它们的顺序不同，程序在判断它们是否相等时也依然会返回false
#创建普通的dict(字典)对象
my_data = {'Python': 20, 'Swift': 32, 'Kotlin': 43, 'Go': 25}
#创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
#创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1)
print(d2)
print(d1 == d2)  #返回False
'''

#由于OrderedDict是有序的，提供了两个方法：
"""
popitem(last=True): 默认弹出并返回最右边(最后加入)的key-value对：如果将last参数设为False,则弹出并返回最左边(最先加入)的key-value对
move_to_end(key, last=True):默认将指定的key-value对移动到最右边(最后加入)：如果将last改为False,则将指定的key-value对移动到最左边(最先加入)
"""

'''
from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
#将b对应的key-value对移动到最右边(最后加入)
d.move_to_end('b')
print(d.keys())
#将b对应的key-value对移动到最左边(最先加入)
d.move_to_end('b', last=False)
print(d.keys())
#弹出并返回最右边(最后加入)的key-value对
print(d.popitem(last=False)[0])
'''


#函数相关模块
#itertools 模块的功能函数: 主要包含了一些用于生成迭代器的函数
'''
>>import itertools
>>[e for e in dir(itertools) if not e.startswith('_')]
'''

#itertools模块中三个生成无限迭代器的函数
"""
count(start, [step]): 生成start, start+step, start+2*step, ...的迭代器，其中step默认为1，
        比如使用count(10)生成的迭代器包含：10, 11, 12, 13, 14, ...
cycle(p): 对序列p生成无限循环p0, p1, ..., p0, p1, ...的迭代器。
        比如使用cycle('ABCD')生成的迭代器包含: A,B,C,D,A,B,C,D, ...
repeat(elem [,n]): 生成无限个elem元素重复的迭代器，如果指定了参数n，则只生成n个elem元素。
        比如使用repeat(10, 3)生成的迭代器包含: 10, 10, 10
"""

#示例：使用上面三个函数来生成迭代器
'''
import itertools as it

#使用count(10, 3)生成10、13、16、...的迭代器
for e in it.count(10, 3):
    print(e)
    #用于跳出无限循环
    if e > 20:
        break
print('----------')

my_counter = 0   #定义个数
#cycle用于对序列生成无限循环的迭代器
for e in it.cycle(['Python', 'Kotlin', 'Swift']):
    print(e)
    #用于跳出无限循环
    my_counter += 1
    if my_counter > 7:
        break
print('...........')

#repeat用于生成n个元素重复的迭代器
for e in it.repeat('Python', 3):
    print(e)
'''


#itertools模块中其他常用的迭代器函数：
"""
accumulate(p[,func]): 默认生成根据序列p元素累加的迭代器，如：p0, p0+p1, p0+p1+p2, ... 序列,
        如果指定了func函数，则用func函数来计算下一个元素的值
chain(p, q,...): 将多个序列里的元素 "链" 在一起生成新的序列
compress(data, selectors): 根据selectors序列的值对data序列的元素进行过滤。如果selector[0]为真，
        则保留data[0]；否则不保留；如果selector[1]为真，则保留data[1]......依此类推
dropwhile(pred, seq): 使用pred函数对seq序列进行过滤，从seq中第一个使用pred函数计算为False的元素开始，
        保留从该元素到序列结束的全部元素
takewhile(pred, seq): 该函数和上一个函数恰好相反。使用pred函数对seq序列进行过滤，从seq中第一个使用pred函数计算
        为False的元素开始，去掉从该元素到序列结束的全部元素
filterfalse(pred, seq): 使用pred函数对seq序列进行过滤，保留seq中使用pred计算为True的元素。比如
        filterfalse(lambda x:x%2,range(10)), 得到 0,2,4,6,8
islice(seq, [start,] stop [, step]): 其功能类似于序列的 slice 方法，实际上就是返回 seq[start:stop:step]的结果
startmap(func, seq): 使用func对seq序列的每个元素进行计算，将计算结果作为新的序列元素。当使用func计算序列元素时，
        支持序列解包。比如seq序列的元素长度为3，那么func可以是一个接收三个参数的函数，该函数将会根据这三个参数来计算
        新序列的元素
zip_longest(p, q, ...): 将p、q等序列中的元素按索引合并成元组，这些元组将作为新序列的元素
"""

'''
#示例：上述函数的测试
import itertools as it
#默认使用累加的方式计算下一个元素的值
for e in it.accumulate(range(6)):  #这里p0就是0,p1就是1，一直到p5是5
    print(e, end=', ')
print('\n----------')
#使用 x*y 的方式(即指定了func函数来计算迭代器下一个元素的值
for e in it.accumulate(range(1, 6), lambda x, y: x * y):  #lambda表达式就是func函数的简写
    print(e, end=', ') # 1*1, 2*1, 3*2*1, 4*3*1, 5*4*3*2*1
print('\n-----------')

#将两个序列"链"在一起，生成新的迭代器
for e in it.chain(['a', 'b'], ['Kotlin', 'Swift']):
    print(e, end=', ')
print('\n-----------')

#根据第二个序列来筛选第一个序列的元素
#由于第二个序列只有中间两个元素为1(True)，因此第一个序列只保留中间两个元素
for e in it.compress(['a', 'b', 'Kotlin', 'Swift'], [0, 1, 1, 0]):  #0为False
    print(e, end=', ')
print('\n-----------')

#获取序列中从长度不小于4的元素开始(包括该元素)到结束的所有元素
for e in it.takewhile(lambda x:len(x)<4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n-----------')
#使用pow函数对原序列的元素进行计算，将计算结果作为新序列的元素
for e in it.starmap(pow, [(2, 5), (3, 2), (10, 3)]):   #pow()是求幂函数
    print(e, end=', ')
print('\n----------')

#将'ABCD'、'xy'的元素按索引合并成元组，这些元组将作为新序列的元素
#长度不够的序列元素使用'-'字符代替
for e in it.zip_longest('ABCD', 'xy', fillvalue='-'):  #0-4个索引，只有0,1两个索引匹配
    print(e, end=', ')
'''


#itertools模块中用于生成排列组合的工具函数
"""
product(p, q, ...[repeat=1]):用序列p、q、...中的元素进行排列组合，就相当于使用嵌套循环组合
permutations(p[, r]): 从序列p中取出r个元组组成全排列，将排列得到的元组作为新迭代器的元素
combinations(p, r): 从序列p中取出r个元素组成全组合，元素不允许重复，将组合得到的元组作为新迭代器的元素
combinations_with_replacement(p, r):从序列p中取出r个元素组成全组合，元素允许重复,将组合得到的元组作为新迭代器的元素
"""

#示例：示范4个函数的用法
'''
import itertools as it
#使用两个序列进行排列组合
for e in it.product('AB', 'CD'):
    print(''.join(e), end=', ')  #join方法用于将元素连接成一个字符串
print('\n-----------')
#使用一个序列，重复两次进行全排列
for e in it.product('AB', repeat=2):  #即  'AB' 和 'AB' 中元素两两随机组合
    print(''.join(e), end=', ')
print('\n-----------')
#从序列中取两个元素进行排列
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=', ')
print('\n----------')
#从序列中取两个元素进行组合，元素不允许重复
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=', ')
print('\n----------')
#从序列中取两个元素进行组合，元素允许重复
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=', ')
'''



#functools模块的功能函数：包含了一些函数装饰器和便捷的功能函数
'''查看functools模块的功能函数
>>import functools
>>[e for e in dir(functools) if not e.startswith('_')]
'''

#常用的函数装饰器和功能函数
"""
functools.cmp_to_key(func):将老式的比较函数(func)转换为关键字函数(key function)。
    在Python3中比较大小、排序都是基于关键字函数的，Python3不支持老式的比较函数
@functools.lru_cache(maxsize=128, typed=False):该函数装饰器使用LRU(最近最少使用)缓存算法来缓存相对
    耗时的函数结果，避免传入相同的参数重复计算。同时，缓存并不会无限增长，不用的缓存会被释放。其中maxsize
    参数用于设置缓存占用的最大字节数，typed参数用于设置将不同类型的缓存结果分开存放
@functools.total_ordering: 这个类装饰器(作用类似于函数装饰器，只是它用于修饰类)，用于为类自动生成比较方法。
    通常来说，开发者只要提供__lt__()、__le__()、__gt__()、__ge__()其中之一(最好能提供__eq__()方法)，
    @functools.total_ordering装饰器就会为该类生成剩下的比较方法
functools.partial(func, *args, **keywords):该函数用于为func函数的部分参数指定参数值,从而得到一个转换后的函数，
    程序以后调用转换后的函数时，就可以少传入那些已指定值的参数
functools.partialmethod(func, *args, **keywords): 该函数与上一个函数的含义完全相同，只不过该函数用于为类中的
    方法设置参数值
functools.reduce(function, iterable[, initializer]): 将初始值(默认为0,可由initializer参数指定)、迭代器的当
    前元素传入function函数，将计算出来的函数结果作为下一次计算的初始值、迭代器的下一个元素再次调用function函数
    ......依次类推,直到迭代器的最后一个元素
@functools.singledispatch: 该函数装饰器用于实现函数对多个类型进行重载。比如同样的函数名称，为不同的参数类型提供
    不同的功能实现。该函数的本质就是根据参数类型的变换，将函数转向调用不同的函数
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):对 wrapper 函数进行包装，使之
    看上去就像wrapped(被包装)函数，是函数
@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)：该函数装饰器用于修饰包装函数，使包装函数
    看上去就像wrapped函数，是函数装饰器
@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)： 该函数装饰器用于修饰包装函数,使包装函数
    看上去就像wrapped(被包装)函数
"""

#示例：示范部分函数或函数装饰器的用法
'''
from functools import *

#设初始值(默认为0)为x,当前序列元素为y，将x+y的和作为下一次计算的初始值
print(reduce(lambda x,y: x + y, range(5)))
print(reduce(lambda x,y: x + y, range(6)))

#设初始值为10
print(reduce(lambda x,y: x + y, range(6), 10))
print('--------------------')

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name = %s' % self.name

#定义一个老式的大小比较函数，User的name越长，该User越大
def old_cmp(u1, u2):
    return len(u1.name) - len(u2.name)

my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
#对my_data排序，需要关键字函数(调用cmp_to_key将old_cmp转换为关键字函数)
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('----------------')
@lru_cache(maxsize=32)

def factorial(n):
    print('~~计算%d的阶乘~~' % n)
    if n == 1:
        return  1
    else: 
        return n * factorial(n -1)
#只有这行会计算，然后会缓存5、4、3、2、1的阶乘
print(factorial(5))
print(factorial(3))
print(factorial(5))
print('----------------')
#int函数默认将十进制形式的字符串转换为整数
print(int('12345'))
#为int函数的base参数指定参数值
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制形式的字符串转换成整数'
#相当于执行base为2的int函数,下面2行代码本质一样
print(basetwo('10010'))  
print(int('10010', 2))
'''


"""partialmethod()与partial()函数的作用基本相似，区别是: partial()函数用于为函数的部分参数绑定值；而partialmethod()函数则用于为类中方法的部分参数绑定值"""

#示范partialmethod()函数的用法
from functools import *
class Cell:
    def __init__(self):
        self._alive = False
    # @property装饰器指定该方法可使用属性语法访问
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    #指定set_alive()方法，就是将set_state()方法的state参数指定为True
    set_alive = partialmethod(set_state, True)
    #指定set_dead()方法，就是将set_state()方法的state参数指定为False
    set_dead = partialmethod(set_state, False)

c = Cell()
print(c.alive)
#相当于调用c.set_state(True)
c.set_alive()
print(c.alive)
#相当于调用c.set_state(False)
c.set_dead()
print(c.alive)
















