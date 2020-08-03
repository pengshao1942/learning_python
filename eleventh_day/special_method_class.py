#重写 __repr__() 方法：
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
#创建一个Item对象，将之赋值给im变量
im = Item('鼠标', 29.8)
#打印im所引用的Item对象
print(im)
#下面的代码等同于上面的print(im)
print(im.__repr__)
"""

#__repr__() 是Pyhton类中的一个特殊方法，object类已提供了该方法，所有的Python类都是object类的子类
# 故所有的Python对象都具有 __repr__() 方法

#当程序需要将任何对象与字符串进行连接时，都可先调用 __repr__() 方法将对象转换成字符串，然后将两个
#字符串连接在一起,如下：
# im_str = im.__repr__() + ""

#自定义类实现 "自我描述" 的功能，必须重写 __repr__() 方法
# __repr__() 方法是一个 "自我描述" 的方法，用来告诉外界该对象具有的状态信息
"""
class Apple:
    #实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    #重写__repr__()方法，用于实现Apple对象的 "自我描述"
    def __repr__(self):
        return "Apple[color=" + self.color + ", weight= "+ str(self.weight) + "]"  #对象的自我描述信息

a = Apple("红色", 5.68)
#打印Apple对象
print(a)
"""
#输出内容：Apple[color=红色, weight= 5.68]
#重写__repr__()方法总是返回该对象的所有令人感兴趣的信息所组成的字符串，通常返回如下形式的字符串：
#类名[field1=值1, field2=值2, ...]


#析构方法： __del__()
#与 __init__ 方法对应的是 __del__() 方法，__init__() 方法用于初始化Python对象,而 __del__() 方法则用于销毁Python对象
#在任何Python对象将要被系统回收之时，系统都会自动调用该对象的 __del__() 方法
#Python通过对象的引用计数为2，当程序中不再有变量引用该对象(引用计数为0)，表明程序不再需要该对象，因此Python就会回收该对象
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    #定义析构函数
    def __del__(self):
        print('del删除对象')

#创建一个Item对象，将之赋值给im变量
im = Item('鼠标', 29.8)
x = im    #引用对象，引用计数加1
#打印im所引用的Item对象
del im  #回收对象，等到程序执行完才回收；若注释掉 x = im ，则不需要等到程序结束就回收im对象，因为引用计数为0了
print('--------------------')
"""

#如果父类提供了 __del__() 方法，则系统重写 __del__() 方法时必须显示调用父类的 __del__() 方法，以保证合理地回收父类实例的部分属性


# __dir__() 方法：用于列出该对象内部的所有属性（包括方法）名，该方法将会返回包含所有属性(方法)名的序列
#当程序对某个对象执行dir(object)函数时，实际上就是将该对象的 __dir__() 方法返回值进行排序，然后包装成列表
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info():
        pass

#创建一个Item对象，将之赋值给 im 变量
im = Item('鼠标', 29.8)
print(im.__dir__()) #返回所有属性(包括方法)组成的列表
print(dir(im))  #返回所有属性(包括方法)排序之后的列表；dir(object) 方法
"""

#__dict__属性：用于查看对象内部存储的所有属性名和属性值组成的字典，通常程序直接使用该属性即可
#使用 __dict__ 属性既可查看对象的所有内部状态，也可通过字典语法来访问或修改指定属性的值
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

im = Item('鼠标', 29.8)  #返回字典,由对象内的属性名和属性值组成的dict(字典)对象
print(im.__dict__)
#通过__dict__访问price属性
print(im.__dict__['price'])  #访问字典属性，输出键对应的值,字典键值的访问方法
#通过__dict__访问name属性
print(im.__dict__['name'])  #输出name键对应的值
im.__dict__['name'] = '键盘'  #对__dict__获取到的键重新赋值(修改)，字典键值的修改
print(im.name)
im.__dict__['price'] = '32.8'  #对__dict__获取到的键重新赋值(修改)
print(im.price)
"""


"""
__getattribute__(self, name): 当程序访问对象的name属性时被自动调用
__getattr__(self, name): 当程序访问对象的name属性 '且该属性不存在时' 被自动调用
__setattr__(self, name, value): 当程序对对象的name属性赋值时被自动调用
__delattr__(self, name): 当程序删除对象的name属性时被自动调用
"""
#通过重写上面的方法，可以为Python类 "合成" 属性----当属性不存在时，程序会委托给上面的方法来实现 "合成" 属性
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):
        print('----设置%s属性----' % name)
        if name == 'size':
            self.width, self.height = value  #赋值
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        print('----读取%s属性----' % name)
        if name == 'size':
            return self.width, self.height  #返回字典
        else:
            raise AttributeError
    def __delattr__(self, name):
        print('----删除%s属性----' % name)
        if name == 'size':
            self.__dict__['width'] = 0  #赋值
            self.__dict__['height'] = 0

rect = Rectangle(3, 4)
print(rect.size)
rect.size = 6, 8
print(rect.width)
del rect.size
print(rect.size)
"""

#在读取、设置属性之前进行某种拦截处理(比如检查数据是否合法之类的)，也可通过重写 __setattr__()或 __getattribute__()方法来实现
"""
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #重写_setattr__()方法对设置的属性值进行检查
    def __setattr__(self, name, value):
        #如果正在设置name属性
        if name == 'name':  
            if 2 < len(value) <= 8 or len(value) > 8:
                self.__dict__['name'] = value   #满足条件则设置属性
            else:
                raise ValueError('name的长度必须在2~8之间')
        elif name == 'age':
            if 10 < value < 60:
                self.__dict__['age'] = value   #满足条件则设置属性
            else:
                raise ValueError('age值必须在10~60之间')

u = User('fkit', 24)
print(u.name)
print(u.age)
u.name = 'fk'  #引发异常
#u.age = 5 #引发异常
"""

#与反射相关的属性和方法:动态判断或设置某个属性值
#程序在运行过程中要动态判断是否包含某个属性(包括方法)，甚至要动态设置某个属性值，可通过Python的反射支持来实现
"""
hasattr(object, name): 检查obj对象是否包含名为name的属性或方法
getattr(object, name[, default]): 获取object对象中名为name的属性或方法
setattr(object, name, value,/): 将obj对象的name属性设为value
"""
"""
class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times
    def info():  #由于inof是方法，故下面的代码(self)会提示: name 'info' is no defined
        print("一条简单的评论，内容是%s" % self.detail)  

c = Comment('疯狂Python讲义很不错', 20)
#判断是否包含指定的属性或方法
print(hasattr(c, 'detail'))  #True,判断是否包含指定的属性
print(hasattr(c, 'view_times')) #True
print(hasattr(c, 'info')) #True,判断是否包含指定的方法info
# 获取指定属性的属性值
print(getattr(c, 'detail'))  #'疯狂Python讲义很不错'
print(getattr(c, 'view_times')) #20
#由于inof是方法，故下面的代码会提示: name 'info' is no defined
#print(getattr(c, info, '默认值'))

#为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
#输出重新设置后的属性值
print(c.detail)
print(c.view_times)

#设置不存在的属性，即为对象添加属性
setattr(c, 'test', '新增的测试属性')
print(c.test)
"""
#setattr()函数还可对方法进行配置
#hasattr()函数即可判断属性，也可判断方法，但getattr则只能获取属性的属性值

#__call__属性：程序可通过判断该属性(或方法)是否包含 __call__ 属性来确定它是否可调用
"""
class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
    def validLogin(self):  #方法
        print('验证%s的登录' % self.name)

u = User('crazyit', 'leegang')
#判断u.name 是否包含 __call__ 方法，即判断它是否可调用,包含__call__方法就可调用，否则不可以调用；输出值为布尔值(True或False)
print(hasattr(u.name, '__call__'))  #False
#判断u.passwd是否包含__call__方法，即判断它是否可调用
print(hasattr(u.passwd, '__call__'))  #False
#判断u.validLogin是否包含__call__方法，即判断它(方法)是否可调用
print(hasattr(u.validLogin, '__call__')) #True，hasattr()函数判断是否包含方法
"""

#一个函数(甚至对象)之所以能执行，关键就在于__call__()方法。x(arg1, arg2, ...)实际上是x.__call__(arg1, arg2, ...)的快捷写法
#为自定义类添加__call__方法，使得该类的实例也变成可调用的

"""
#定义Role类
class Role:
    def __init__(self, name):  #初始化方法
        self.name = name
    #定义 __call__方法
    def __call__(self):
        print('执行Role对象')

r = Role('管理员')
#直接调用Role对象，就是调用该对象的 __call__ 方法
r()  #使用调用函数的语法来调用对象  

def foo():
    print('---foo函数---')
#示范通过两种方式来调用foo()函数,输出完全相同
foo()  
foo.__call__()
"""

#与序列(列表、元组、字典)相关的特殊方法
"""
__len__(self): 该方法的返回值决定序列中元素的个数
__getitem__(self, key):该方法获取指定索引对应的元素。该方法的key应该是整数值或slice对象，否则该方法会引发KeyError异常
__contains__(self, item):该方法判断序列是否包含指定元素
__setitem__(self, key, value):该方法设置指定索引对应的元素。该方法的key应该是整数值或slice对象，否则该方法会引发KeyError异常
__delitem__(self, key): 该方法删除指定索引对应的元素
"""
#如果程序要实现 '不可变' 序列(程序只能获取序列中的元素，不能修改)，只要实现上面前3个方法就行;
#如果程序要实现 '可变' 序列(程序即能获取序列中的元素，也可修改)，则需要实现上面5个方法;

#案例：实现一个字符串序列，在该字符串序列中默认每个字符串的长度都是3，该序列的元素按 AAA、AAB、AAC......这种格式排列
"""
def check_key(key):
    '''
    该函数将会负责检查序列的索引，该索引必须是整数值，否则引发TypeError异常
    且程序要求索引必须为非负整数值，否则引发IndexError异常
    '''
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 26 ** 3:
        raise IndexError('索引值不能超过%d' % 26 ** 3)

class StringSeq:
    def __init__(self):
        #用于存储被修改的数据
        self.__changed = {}
        #用于存储已删除元素的索引
        self.__deleted = []
    def __len__(self):   #该方法返回序列中元素的个数
        return 26 ** 3

    def __getitem__(self, key):  #该方法获取指定索引对应的元素
        '''
        根据索引获取序列中元素
        '''
        check_key(key)   #方法中引用check_key()方法
        #如果在self.__changed中找到修改后的数据，则打印出该索引对应的元素
        if key in self.__changed:
            return self.__changed[key]
        #如果key在self.__deleted中，说明该元素已被删除，打印None
        if key in self.__deleted:
            return None
        #否则根据计算规则返回序列元素
        three = key // (26 * 26)
        two = ( key - three * 26 * 26) // 26
        one = key % 26
        return chr(65 + three) + chr(65 + two) + chr(65 + one) #chr()函数返回一个对应的字符，()内的数字可以是10或16进制形式的数字

    def __setitem__(self, key, value):  #该方法设置指定索引对应的元素
        '''
        根据索引修改序列中元素
        '''
        check_key(key)
        #将修改的元素以key-value对的形式保存在__changed中
        self.__changed[key] = value

    def __delitem__(self, key):  #该方法删除指定索引对应的元素
        '''
        根据索引删除序列中元素
        '''
        check_key(key)
        #如果__deleted列表中没有包含被删除的key,则添加被删除的key
        if key not in self.__deleted:
            self.__deleted.append(key)
        #如果___changed中包含被删除的key,则删除它
        if key in self.__changed:
            del self.__changed[key]

#创建序列
sq = StringSeq()
#获取序列的长度，实际上就是返回__len__()方法的返回值
print(len(sq))
print(sq[26*26])  # 'BAA'
#打印修改之前的sq[1]
print(sq[1]) # 'AAB'
#修改sq[1]元素
sq[1] = 'fkit'
#打印修改之后的sq[1]
print(sq[1]) # 'fkit'
#删除sq[1]
del sq[1]
print(sq[1]) #None
#再次对sq[1]赋值
sq[1] = 'crazyit'
print(sq[1])  # crazyit
"""

#迭代器
#可迭代的对象都属于迭代器： 列表、元组、字典等
#实现迭代器的方法：实现如下两个方法即可
"""
__iter__(self):该方法返回一个迭代器(iterator),迭代器必须包含一个__next__()方法，该方法返回迭代器的下一个元素
__reversed__(self):该方法主要为内建的reversed()反转函数提供支持，当程序调用reversed()函数对指定迭代器执行反转时，实际上是由该方法实现的
"""
"""
#迭代器案例：斐波拉契数列
class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len
    #定义迭代器所需的__next__方法(迭代器必须包含该方法)
    def __next__(self):
        #如果__len__属性为0，结束迭代
        if self.__len == 0:
            raise StopIteration  #异常：结束迭代
        #完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        #数列长度减1
        self.__len -= 1
        return self.first
    #定义__iter__方法，该方法返回迭代器
    def __iter__(self):
        return self
#创建Fibs对象
fibs = Fibs(10)
#获取迭代器的下一个元素
print(next(fibs))  #next()函数实际就是通过迭代器的__next__()方法实现的
#使用for循环遍历迭代器
for el in fibs:
    print(el, end=' ')

#将列表转换为迭代器，使用内置的iter()函数将列表、元组等转换成迭代器
my_iter = iter([2, 'fkit', 4])
#依次获取迭代器的下一个元素
print(my_iter.__next__())   #打印2
print(my_iter.__next__())   #打印 fkit
"""


#扩展列表、元组和字典
#开发一个新的字典类：可根据value来获取key
"""
#定义ValueDict类，继承dict类
class ValueDict(dict):
    #定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类的构造函数
        super().__init__(*args, **kwargs)
    #新增getkeys方法
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val:
                result.append(key)
        return result

my_dict = ValueDict(语文 = 92, 数学 = 89, 英语 = 92)
# 获取92对应的所有key，调用 getkeys()方法
print(my_dict.getkeys(92))
my_dict['编程'] = 92
print(my_dict.getkeys(92))
"""

#生成器：和迭代器的功能相似，也提供 __next__() 方法
#生成器和迭代器的区别在于：迭代器通常是先定义一个迭代器类，然后通过创建实例来创建迭代器；而生成器则是先定义一个包含yield语句的函数，然后通过调用该函数来创建生成器
'''
创建生成器需要两步:
1、定义一个包含yield语句的函数
2、调用第1步创建的函数得到生成器
'''

'''
#使用生成器定义一个差值递增的数列
def test(val, step):
    print("--------函数开始执行------")
    cur = 0
    #遍历 0~val
    for i in range(val):
        #cur添加 i*step
        cur += i * step
        yield cur  #包含yield语句
        #print(cur, end=' ')
t = test(10, 2)
#print("============")
print(next(t))  #0,生成器被 "冻结" 在yield处,在python2中应该写成 print(t.next())
print(next(t))  #2，生成器被再次 "冻结" 在yield处
'''

#调用yield语句的函数并不会立即执行，只是返回一个生成器。只有当程序通过next()函数调用生成器或遍历生成器时，函数才会真正执行
#使用for循环来遍历生成器
'''
for ele in t:
    print(ele, end=' ')
#再次创建生成器
t = test(10, 1)
#将生成器转换成列表
print(list(t))
#再次创建生成器
t = test(10, 3)
#将生成器转换成元组
print(tuple(t))
'''

#Python主要提供了两种方式来创建生成器：
#1、使用for循环的生成器推导式
#2、使用带yield语句的生成器函数

#使用生成器的好处：生成器是Python的一个特色功能
'''
1、减少代码执行的次数，每次调用next()时才执行一次循环
2、当函数要返回的数据量大时，节省内存开销
3、使用生成器使代码更加简洁
'''

#生成器的方法
#生成器的send()方法，用于获取生成器所生成的下一个值，与next()函数的功能非常相似；
#send()方法可接收一个参数，该参数值会被发送给生成器函数
'''
外部程序通过send()方法发送数据
生成器函数使用yield语句接收数据
'''
'''
#案例：向生成器发送数据，该程序会一次生成每个整数的平方值，但外部程序可以向生成器发送数据，当生成器接收到外部数据之后会生成外部数据的平方值
def square_gen(val):
    i = 0
    out_val = None
    while True:
        #使用yield语句生成值，使用out_val接收send()方法发送的参数值
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        #如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数值
        if out_val is not None:
            print("====%d" % out_val)
        i += 1
sg = square_gen(5)
#第一次调用send()方法获取值，只能传入None作为参数
print(sg.send(None))
print(next(sg)) #生成器不能获取第一次调用send()方法发送的参数值 
print('-----------------')
#调用send()方法获取生成器的下一个值，参数9会被发送给生成器
print(sg.send(9))
#再次调用next()函数获取生成器的下一个值
print(next(sg))

#close(): 该方法用于停止生成器
#throw()：该方法用于在生成器内部(yield语句内)引发一个异常
#让生成器引发异常
#sg.throw(ValueError)
#关闭生成器，示范close()方法
sg.close()
print(next(sg))   #打印StopIteration
'''


#运算符重载的特殊方法
#运算符的方法类似如下：例如加法,add替换为其他运算符的字段即可
#object.__add__(self, other) 和一个带r的版本：object.__radd__(self, other)，自定义类的对象可以出现在对应运算符的右边
#可为自定义类提供对应的运算符方法：
'''
#例如：定义一个类Rectangle，对两个Rectangle执行加法运算
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSite(self, size):
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property定义属性
    size = property(getSize, setSite)
    #定义__add__方法，该对象可执行"+"运算
    def __add__(self, other):   #为Rectangle提供__add__方法
        #要求参与"+"运算的另一个操作数必须是Rectangle(判断)
        if not isinstance(other, Rectangle):
            raise TypeError('+运算要求目标是Rectangle')
        return Rectangle(self.width + other.width, self.height + other.height)
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
#对两个Rectangle执行加法运算
r = r1 + r2
print(r)  #Rectangle(width=7, height=9)
#当程序执行运算时，Python首选会尝试使用 __add__方法进行计算，如果没有提供__add__方法，还会尝试调用__radd__方法
'''

#如果自定义类提供了__rxxx__()方法，那么自定义类的对象就可以出现在对应运算符的右边
'''
#案例：为Rectangle类定义一个__radd__方法
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property定义属性
    size = property(getSize, setSize)

    #定义__iadd__方法,该对象可出现在 "+" 的右边
    def __iadd__(self, other):
    #要求参与 "+=" 运算的另一个操作数必须是数值
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('+=运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)

r = Rectangle(4, 5)
#r有__iadd__方法，因此它支持"+="运算，即自定义的类可出现在运算符右边
r += 2  
print(r)  #输出：<__main__.Rectangle object at 0x0000027D6B136880>
'''

#与比较运算符相关的特殊方法
#object.__lt__(self, other): 为 "<" 运算符提供支持；其他比较运算符类似，替换lt即可
#对于同一个类的实例比较大小而言：只要实现其中三个方法即可
'''
#案例：基于面积比较大小  object.__ge__(self, other)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property定义属性
    size = property(getSize, setSize)
    #定义__gt__方法，该对象可支持 ">" 和 "<"比较
    def __gt__(self, other):
        #要求参与 ">" 比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>比较要求目标是是Rectangle')
        return True if self.width * self.height > other.width * other.height else False  #三目运算符写法
    #定义__eq__方法，该对象可支持 "==" 和 "!=" 比较
    def __eq__(self, other):
            #要求参与 "==" 比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('==比较要求目标是Rectangle')
        return True if self.width * self.height == other.width * other.height else False
        #定义__ge__方法，该对象可支持 ">=" 和 "<=" 比较
    def __ge__(self, other):
        #要求参与 ">=" 比较的另一个操作数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>=比较要求目标是Rectangle')
        return True if self.width * self.height >= other.width * other.height else False
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)
print(r1 >= r2)
print(r1 <= r2)
print(r1 < r2)
print(r1 == r2)
print(r1 != r2)
'''

#与单目运算符相关的特殊方法：单目求正、单目求负、单目取反
#object.__neg__(self): 为单目求负(-)运算符提供支持；其他运算符替换 neg 关键字 即可

#案例：自定义一个类实现__neg__()方法,用于控制将矩形的宽、高交换
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSize(self, size):  #计算面积
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property定义属性
    size = property(getSize, setSize)
    #定义__neg__方法，该对象可执行求负(-)运算
    def __neg__(self):
        self.width, self.height = self.height, self.width
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)

r = Rectangle(4, 5)
#对Rectangle执行求负运算
-r
print(r)
'''

#与类型转换相关的特殊方法
#object.__str__(self)：对应于调用内置的str()函数将该对象转换成字符串；其他类型转换类似
'''
#案例：自定义一个Rectangle类，为该类提供了一个__init__()方法，可用int()函数将Rectangle对象转换成整数
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property插件
    size = property(getSize, setSize)
    #定义__init__方法，程序可调用init()函数将该对象转换成整数
    def __int__(self):  #或 def __str__(self): 等其他类型转换的方法
        return int(self.width * self.height) #return str(self.width * self.height)
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)

r = Rectangle(4, 5)
print(int(r))  #调用int()函数将Rectangle结果转化成整数，实际上就是返回该矩形的面积
'''


#与常见的内建函数相关的特殊方法
#object.__format__(self, format_spec): 对应于调用内置的format()函数将对象转换成格式化字符串
#其他内建函数如：hash、abs、round、trunc、floor、ceil
#trunc方法比int方法更底层

'''
#案例：自定义一个类Rectangle，为该类定义一个__round__()方法，程序就可以调用round()函数对Rectangle对象执行四舍五入取整
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size
    #定义getSize()函数
    def getSize(self):
        return self.width, self.height
    #使用property插件
    size = property(getSize, setSize)
    #定义__round__方法，程序可调用round()函数将该对象执行四舍五入取整
    def __round__(self, ndigits=0):
        self.width, self.height = round(self.width, ndigits), round(self.height, ndigits)
        return self
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)

r = Rectangle(4.68, 5.52)
#对Rectangle对象执行四舍五入取整,(默认保留一位小数)
result = round(r, 1)
print(r)
print(result) 
'''































