"""
#类的定义：
class Person:
    '这是定义的一个person类'   #类的说明文档
    hair = 'black'  #在类体中定义的变量，称为类变量
    def __init__(self, name = 'Charlie', age=8):   #定义一个构造方法
        #在类方法中定义的变量称为：实例变量
        self.name = name
        self.age = age
    def say(self, content): #在类体中定义的方法，称为类方法(函数)
        print(content)

p = Person()  #将Person对象赋值给变量
print(p.name, p.age)  #访问对象的变量,输出实例变量
p.name = '李刚'
p.say('Python简单易学!')
print(p.name, p.age)

p.skills = ['programming', 'swimming']  #为对象动态增加一个skills实例变量
print(p.skills)

del p.name   #动态为对象删除实例变量
#print(p.name)  #报错：AttributeError: 'Person' object has no attribute 'name'

def info(self):
    print("--info函数---", self)

p.foo = info  #为对象动态增加方法，使用info对p对象的foo方法赋值
p.foo(p)  #必须手动将调用者绑定到第一个参数，程序不会自动将调用者绑定到第一个参数

p.bar = lambda self: print('---lambda表达式--', self)  #动态增加方法,使用lambda表达式
p.bar(p)

def intro_func(self, content):
    print('我是一个人，信息为：%s' % content)

from types import MethodType   #导入MethodType
p.intro = MethodType(intro_func, p)  #
p.intro('生活在别处')


#实例方法和自动绑定self： 一个对象的两个方法之间的依赖
class Dog():
    #定义一个jump()方法
    def jump(self):
        print("正在执行jump()方法")
    #定义一个run()方法，run()方法需要借助jump()方法
    def run(self):
        self.jump  #使用self参数引用调用run()方法的对象，这里self. 不可以省略
        print("正在执行run方法")

#在构造方法中，self参数(第一个参数)代表该构造方法正在初始化的对象
class InConstructor:
    def __init__(self):
        foo = 0  #在构造方法中定义一个foo变量(局部变量)
        #使用self代表该构造方法正在初始化的对象
        self.foo = 6  #将会把该构造方法正在初始化的对象的foo实例变量设为6
#所有使用InConstructor创建的对象的foo实例变量将被设为6
print(InConstructor().foo)



#类也能调用实例方法：
class User:
    def walk(self):
        print(self, "正在慢慢地走")

u = User()  #类赋值给对象
User.walk(u) #类调用实例方法walk
#User.walk('fkit')  #手动为第一个参数绑定参数值


#类方法与静态方法：
class Bird:
    @classmethod  #使用@classmethod修饰的方法是类方法
    def fly(cls):  #类方法的第一个参数名通常建议为cls
        print('类方法fly: ', cls)
    @staticmethod  #使用@staticmethod修饰的方法是静态方法
    def info(p):
        print('静态方法info: ', p)

Bird.fly()  #调用类方法，Bird类会自动绑定到第一个参数cls
Bird.info('crazyit')  #调用静态方法，不会自动绑定，程序必须手动绑定第一个参数p为：crazyit

b = Bird()  #创建类对象
b.fly()   #使用类对象调用fly()类方法，其实还是使用的类调用的类方法
b.info('python') #使用类对象调用info()静态方法，其实还是使用的类调用的静态方法，必须为第一个参数手动绑定，即p绑定python



#函数装饰器： 使用@符合引用已有的函数后，用来修饰其它函数，装饰被修饰的函数；可自定义函数装饰器
#被修饰的函数总是被替换成@符号所引用的函数的返回值
#被修饰的函数会变成什么类型，完全取决于@符号所引用的函数的返回值
def funA(fn):
    print('A')
    fn()
    return 'fkit'

@funA
def funB():
    print('B')
print(funB)

#更复杂的函数装饰器：
def foo(fn):
    #定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        #查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n -1))
    return bar  #foo函数实际是返回bar函数

@foo
def my_test(a):
    print("===my_test函数===", a)
print(my_test) #打印my_test函数，将看到实际上是bar函数
my_test(10)  #实际是调用bar函数
my_test(6, 5)



#通过函数修饰器为函数添加权限检查的功能：
def auth(fn):
    def auth_fn(*args):
        #用一条语句模拟执行权限检查
        print("----模拟执行权限检查----")
        #回调被修饰的目标函数
        fn(*args)
    return auth_fn

@auth
def test(a, b):
    print("执行test函数,参数a: %s, 参数b: %s" % (a, b))

test(20, 15)


#再论类命名空间： lambda表达式在全局函数和类方法(实例方法)中的区别
global_fn = lambda p: print("执行lambda表达式, p参数", p)
class Category:
     cate_fn = lambda p: print("执行lambda表达式，p参数", p)

global_fn('flik') #全局函数调用，为函数参数p传入值flik
c = Category()
c.cate_fn()  #调用类命名空间内的cate_fn，python自动绑定第一个参数


#成员变量: 访问类的变量、修改类的变量
#推荐：使用类名的调用来访问类对象
class Address:
    detail = '广州'   #定义类变量
    post_code = '510660'
    def info(self):  #类方法
        #尝试直接访问类变量
        #print(detail) #报错:name 'detail' is not defined
        print(Address.detail)  #在函数内(类方法内)也必须通过类名的调用来访问类变量
        print(Address.post_code)  #在函数内(类方法内)也必须通过类名的调用来访问类变量

print(Address.detail)   #在全局范围内也必须通过类名的调用来访问Address类的类变量
print(Address.post_code)  #在全局范围内也必须通过类名的调用来访问Address类的类变量
addr = Address()
addr.info()  #第一次调用，输出类变量的初始值

Address.detail = '佛山'  #修改Address类的类变量
Address.post_code = '460110'  #修改Address类的类变量
addr.info()  #第二次调用，输出类变量修改后的值


#也允许使用对象来访问该对象所属类的类变量，但是不推荐
class Record:
    item = '鼠标'
    date = '2016-06-15'
    def info(self):
        print('info方法中： ', self.item)
        print('info方法中：', self.date)

rc = Record()  #创建Record对象rc
print(rc.item)
print(rc.date)
rc.info()  #通过对象调用Record类的info方法，输出类变量的默认值；python自动赋值第一个参数self
Record.item = '键盘'   #修改类的类变量
Record.date = '2016-08-18'
# 调用info()方法
rc.info()  #输出的是修改后的类变量的值


#通过对象对类变量赋值，其实是定义新的实例变量
class Inventory:
    item = '鼠标'
    quantity = 2000
    def change(self, item, quantity):  #实例方法
        #下面的赋值语句不是对类变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity
iv = Inventory()  #创建Inventory对象iv
iv.change('显示器', 500)  #访问对象时给对象定义实例变量
#访问iv的item和quanticy实例变量
print(iv.item)
print(iv.quantity)
#访问Inventory的item和quanticy类变量
print(Inventory.item)
print(Inventory.quantity)

#通过类修改类变量的值
Inventory.item = '类变量item'
Inventory.quantity = '类变量quanticy'
#访问iv对象的item和quanticy实例变量仍然不变,还是上面定义的 iv.change('显示器', 500)
print(iv.item)
print(iv.quantity)
#对一个对象的实例变量进行修改，也不会影响类变量和其它对象的实例变量；输出依然是上面通过类名对类变量所赋的两个值
iv.item = '实例变量item'
iv.quantity = '实例变量quanticy'
print(Inventory.item)
print(Inventory.quantity)


#使用property函数定义属性：
#当为类定义了 getter、setter等访问器方法，则可使用property()函数将它们定义成属性(相当于实例变量)
class Rectangle:
    #定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setsize()函数
    def setsize(self, size):
        self.width, self.height = size
    #定义getsize()函数
    def getsize(self):
        return self.width, self.height
    #定义delsize()函数
    def delsize(self):
        self.width, self.height = 0, 0
    #使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')
#访问size属性的说明文档
print(Rectangle.size.__doc__)
#通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(4, 3)  #定义类Rectangle的对象
#访问rect的size属性
print(rect.size)
#对rect的size属性赋值
rect.size = 9, 7
#访问rect的width、height实例变量
print(rect.width)
print(rect.height)
#删除rect的size属性
del rect.size
#访问rect的width、height实例变量
print(rect.width)
print(rect.height)


#在使用property()函数定义属性时，可根据需要只传入少量的参数
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + ',' + self.last
    def setfullname(self, fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]
    #使用property()函数定义fullname属性,只传入两个参数
    #该属性是一个可读属性,但不能删除
    fullname = property(getfullname, setfullname)
u = User('悟空', '孙')
#访问 fullname 属性
print(u.fullname)
#对fullname属性赋值
u.fullname = '八戒, 猪'
print(u.first)
print(u.last)


#使用@property装饰器来修饰方法，使之成为属性
class Cell:
    #使用@property修饰方法，相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    #为state属性设置setter方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'
    #为is_dead属性设置getter方法
    #只有getter方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'
c = Cell()
#修改state属性
c.state = 'Alive'
#访问state属性
print(c.state)
#访问is_dead属性
print(c.is_dead)


#隐藏和封装：
#封装是将对象的状态信息隐藏在对象内部，不允许外部程序直接访问对象内部信息，而是通过该类所提供的方法来实现对内部信息的操作和访问
#隐藏：python并非真正隐藏类的成员，只是通过将类的成员命名为以双下划线开头的，来打到隐藏
#封装机制演示类： 隐藏成员和方法就是相当于封装了类中的方法和成员
class User:
    def __hide(self):  #以双下划线开头的命名,隐藏方法
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name  
    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3~8之间')
        self.__name = name  #隐藏name成员
    name = property(getname, setname)
    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在18~70之间')
        self.__age = age  #隐藏age成员
    def getage(self):
        return self.__age  
    age = property(getage, setage)
#创建User对象
u = User()
#对name属性赋值，实际上调用setname()方法
#u.name = 'fk'  #引发 ValueError错误: 用户名长度必须在3~8之间，不符合设置名字的长度条件
#u.name = 'fkgg' #符合条件,允许被设置
#print(u.name) #正确输出
#u.age = 17  #引发 ValueError错误: 用户名年龄必须在18~70之间,不符合设置年龄的大小条件
#u.age = 19    #符合条件,允许被设置
#print(u.age)  #正确输出

#直接调用隐藏的__hide()方法会报错
#u.__hide()  #报错：AttributeError: 'User' object has no attribute '__hide'
#正确访问类的隐藏的方法的操作：
#调用隐藏的__hide()方法
u._User__hide()   #在类前面加单下划线即可；正确输出：‘示范隐藏的hide方法’

#python并没有真正的实现隐藏
#通过某些方法可以绕过隐藏和控制
#对隐藏的__name属性赋值: 在类前加单下划线绕过控制
u._User__name = 'fk'
#访问User对象u的name属性，此时实际上访问的是__name实例变量
print(u.name)  #输出fk，绕过了名字长度要在3到8之间的限制，即绕过了setname()方法的控制

#总结： Python类定义的所有成员默认都是公开的，隐藏成员通过在成员名字前面加双下划线__；绕过隐藏，可以通过在对象引用类的前面加单下划线_
#如： 类对象._类名__成员名
"""

"""
#类的继承：子类继承父类
class Fruit:
    def info(self):
        print("我是一个水果! 重%g克" % self.weight)

class Food:
    def taste(self):
        print("不同的食物的口感不同")

#定义Apple类，继承了Fruit类和Food类
class Apple(Fruit, Food):
    pass

#创建Apple对象
a = Apple()
a.weight = 5.6
#调用Apple对象的info()方法
a.info()
#调用Apple对象的taste()方法
a.taste()


#子类继承多个父类时,如果多个父类中有同名的方法，则排在前面的父类的方法会"遮蔽"排在后面的父类中的同名方法
#Python虽支持多继承，但是如非必要，尽量使用单继承，保证编程思路清晰，避免麻烦
class Item:
    def info(self):
        print("Item中方法：", '这是一个商品')

class Product:
    def info(self):
        print("Product中方法：", '这是一个工业产品')

class Mouse(Item, Product):  #哪个父类在前，哪个父类的优先级就高
    pass

m = Mouse()
m.info()  #由于Item父类的排在前面，因此会使用Item父类的info方法，而遮蔽了Product父类的同名方法


#子类重写父类的方法： 当父类的方法不适合被子类继承时，子类需要重写父类的方法
#若鸵鸟是鸟类，但是鸵鸟继承不了鸟类的会飞的方法，故子类鸵鸟需要重写父类的会飞的方法
class Bird:
    #Bird类的fly()方法
    def fly(self):
        print("我在天空里自由的飞翔!")
class Ostrich(Bird):  #鸵鸟子类
    #重写Bird类的fly()方法
    def fly(self):
        print("我只能在地上奔跑...")

os = Ostrich()  #创建Ostrich对象
os.fly()  #输出的就是子类Ostrich重写后的fly()方法


#在子类中调用在父类中被重写的方法： 
#通过使用未绑定方法即可在子类中再次调用父类中被重写的方法： 在子类中的使用形式： 父类名.要调用的父类方法名(父类方法中的变量)，如： BaseClass.foo(self, n1,..., n)
#此种方法在调用被重写的方法时需要显示地绑定第一个参数self
class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')
class SubClass(BaseClass):
    #重写父类的foo方法
    def foo(self):
        print('子类重写父类中的foo方法')
    def bar(self):
        print('执行bar方法')
        #直接执行foo方法,将会调用子类重写之后的foo()方法
        self.foo()
        #使用类名调用实例方法(未绑定方法)调用父类被重写的方法
        BaseClass.foo(self)

sc = SubClass()
sc.bar()



#排在前面的父类的构造方法会优先被使用
class Employee:
    def __init__(self, salary):  #构造方法,也叫初始化方法
        self.salary = salary
    def work(self):
        print('普通员工正在写代码,工资是:', self.salary)

class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一个顾客, 我的爱好是: %s,地址是：%s' % (self.favorite, self.address))

#Manager继承了Employee，Customer
#class Manager(Employee, Customer):
class Manager(Customer, Employee):
    pass

#m = Manager(25000)  #先使用Employee的构造方法,必须显示地赋值
m = Manager('打篮球', '广州')  
#m.work()  #此时Employee的work方法执行不了
m.info()


#使用super函数调用父类的构造方法后使用
#用super()方法重写父类的构造方法，修改上面的程序，使得Customer和Employee类的构造方法都可以在子类中被调用
#子类的构造方法调用父类的构造方法有2中方式：
  #1、使用未绑定方法
  #2、使用super()函数调用父类的构造方法
class Employee:
    def __init__(self, salary):  #构造方法,也叫初始化方法
        self.salary = salary
    def work(self):
        print('普通员工正在写代码,工资是:', self.salary)

class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一个顾客, 我的爱好是: %s,地址是：%s' % (self.favorite, self.address))

#Manager继承了Employee，Customer
class Manager(Employee, Customer):
    #重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')
        #方法1：通过super()函数调用父类的构造方法
        super().__init__(salary)      
#       super(Manager, self).__init__(salary)  #与上一行代码对的效果相同
        #方法2：使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)

#创建Manager对象
m = Manager(25000, 'IT产品', '广州')
#此时2个父类的方法都生效了
m.work()
m.info()



#为类中所有实例都添加方法，使得该方法对所有对象都有效，可通过为类添加方法来实现
#为类添加方法： 通过__slots__属性
class Cat:
    def __init__(self, name):
        self.name = name

def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)

d1 = Cat('Garfield')
d2 = Cat('Kitty')
#d1.walk()  #报错：AttributeError: 'Cat' object has no attribute 'walk'  从Cat类中找不到walk方法
Cat.walk = walk_func  #为Cat动态添加方法，该方法的第一个参数会自动绑定
#d1、d2调用walk()方法
d1.walk()
d2.walk()


#为类添加方法： 通过__slots__属性
class Dog:
    __slots__ = ('walk', 'age', 'name')  #只允许为实例动态添加walk、age、name这三个属性或方法
    def __init__(self, name):
        self.name = name
    def test(self):
        print('预先定义的test方法')
d = Dog('Snoopy')
from types import MethodType
#只允许为实例动态添加walk、age、name这三个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk()
#d.foo = 30
#__slots__属性并不限制通过类来动态添加属性或方法
Dog.bar = lambda self: print('abc')  #通过类来为类动态添加方法
d.bar()
d.test()

#__slots__属性指定的限制只对当前类的实例起作用,对该类派生出来的子类是不起作用的
class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass

gd = GunDog('Puppy')
#完全可以为GunDog实例动态添加属性
gd.speed = 99
print(gd.speed)

"""
"""
#使用type()函数定义类
class Role:
    pass
r = Role()
#查看变量r的类型
print(type(r))  #输出：<class '__main__.Role'>  表示r的类型是一个类
#查看Role类本身的类型
print(type(Role)) #输出：<class 'type'> 表示Role类本身的类型是type


#可以这样理解：程序使用class定义的所有类都是type类的实例；即type类的实例都是类
#当程序使用class定义一个类时，可理解为定义了一个特殊的对象(type类的对象)
#python可以使用type()函数来动态创建类
def fn(self):
    print('fn函数')
#使用type()定义Dog类 ： 该类继承了object类，还未该类定义了一个walk()方法和age类变量
Dog = type('Dog', (object,), dict(walk=fn, age=6))  #继承的类必须写成元组形式，即使只继承一个类，也要写成元组的形式,逗号不能少
#创建Dog对象
d = Dog()
#分别查看d、Dog的类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
"""

"""
#创建一批全部具有某种特征的类：可通过metaclass来实现； 使用metaclass可以在创建类时动态修改类定义
#使用metaclass动态修改类定义,程序需要先定义metaclass,metaclass应该继承type类,并重写__new__()方法

#定义ItemMetaClass,继承type
class ItemMetaClass(type):
    #cls代表被动态修改的类
    #name代表被动态修改的类名
    #bases代表被动态修改的类的所有父类
    #attrs代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        #为该类动态添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)

#metclass使用举例:
#定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount
#定义CellPhone类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')
    def __init__(self, price):
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

b = Book("python讲义", 89)
b.discount = 0.76
#创建Book对象的cal_price方法
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
#创建CellPhone对象的cal_price()方法
print(cp.cal_price())
"""

"""
#多态：对于弱类型语言,同一个变量在调用同一个方法时，完全可能呈现出多种行为(具体呈现出哪种行为由变量所引用的对象来决定)
#Bird类和Dog类有同样的类变量和同名的类方法
class Bird:
    def move(self, field):
        print('鸟在%s上自由地飞翔' % field)

class Dog:
    def move(self, field):
        print('狗在%s上自由地奔跑' % field)

x = Bird()
x.move('天空')
x = Dog()
x.move('草地')
#即，当field变量再调用同一个move方法时，具体呈现出的行为由它所引用的是Bird类还是Dog类的对象来决定输出哪个类中的方法
"""
"""
#多态的应用： 
#定义一个画布类：
class Canvas:
    def draw_pic(self, shape):
        print('--开始绘图--')
        shape.draw(self)   #调用shape参数(类变量)的draw()方法将自己绘制到画布上,这个draw方法在类的对象里必须定义

class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)
class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)
class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)

c = Canvas()
#传入Rectangle参数，绘制矩形
c.draw_pic(Rectangle())
#传入Trigangle参数,绘制三角形
c.draw_pic(Triangle())
#传入Circle参数，绘制圆形
c.draw_pic(Circle())
"""

"""
#检查类型： 提供2个函数来检查类型
#issubclass(cls, class_or_tuple): 检查cls是否为后一个类或元组包含的多个类中任意类的子类
#isinstance(obj, class_or_tuple): 检查obj是否为后一个类或元组包含的多个类中任意类的子类

#定义一个字符串
hello = "Hello"
# "Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例： ', isinstance(hello, str))
# "Hello"是object类的子类的实例，输出True
print('"Hello"是object类的子类的实例： ', isinstance(hello, object))

# str是object类的子类，输出True
print('str是否是object类的子类：', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例： ', isinstance(hello, tuple))
# str不是tuple类的子类,输出False
print('str是否是tuple类的子类： ', issubclass(str, tuple))

#定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例，输出True
print('[2, 4]是否是list类的实例： ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例，输出True
print('[2, 4]是否是object类及其子类的实例： ', isinstance(my_list, object))
# list是object类的子类，输出True
print('list是否是object类的子类： ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例，输出False
print('[2, 4]是否是tuple类的实例： ', isinstance([2, 4], tuple))
# list不是tuple类的子类，输出False
print('list是否是tuple类的子类： ', issubclass(list, tuple))

#isinstance和issubclass两个函数的第二个参数都可使用元组，如下代码：
data = (20, 'fkit')
print('data是否为列表或元组的实例： ', isinstance(data, (list, tuple)))   #输出True
#str不是list或tuple的子类,输出Falsei
print('str是否为list或tuple的子类： ', issubclass(str, (list, tuple)))

#str是list或tuple或object的子类,输出True
print('str是否是list或tuple或object的子类： ', issubclass(str, (list, tuple, object)))

#python为所有类提供了一个 __bases__ 属性：通过该属性可以查看该类的所有直接父类,该属性返回所有直接父类组成的元组
class A:
    pass
class B:
    pass
class C(A, B):
    pass

print('类A的所有父类：', A.__bases__)
print('类B的所有父类：', B.__bases__)
print('类C的所有父类：', C.__bases__)

#python为所有类提供了一个 __subclasses__() 方法：该方法可以查看一个类的所有直接子类，该方法返回该类的所有子类组成的列表
print('类A的所有子类：', A.__subclasses__())   #这里A类只有一个子类C
print('类B的所有子类：', B.__subclasses__())   #这里B类只有一个子类C
"""

"""
#枚举类： 实例有限(对象有限)且固定的类，在python中成为枚举类；如：四季类，只有春夏秋冬4个对象
#定义枚举类的2中方法：
# 直接使用 Enum 列出多个枚举值来创建枚举类
# 通过继承 Enum 基类来派生枚举类

#定义 Season 枚举类
#枚举类的每个成员都有name、value两个属性，name属性值为该枚举类值的变量名,value代表该枚举值的序号(通常从1开始)
from enum import Enum   
Season = Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
#或如下两行:也是一样
#import enum
#Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))

#直接访问指定枚举
print(Season.SPRING)
#访问枚举成员的变量名
print(Season.SPRING.name)
#访问枚举成员的值
print(Season.SPRING.value)

#通过枚举变量名访问枚举对象
print(Season['SUMMER'])   #像通过索引访问列表元素一样，这里用[]把枚举变量名括起来
#通过枚举值访问枚举对象
print(Season(3))  #枚举值从1开始,因为枚举类的第二个参数是元组，所以这里是()

#Python为枚举提供了一个 __members__ 属性，该属性返回一个dict字典，字典包含了该枚举的所有枚举实例
#可通过遍历 __members__ 属性来访问枚举的所有实例：
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)


#定义更复杂的枚举，可通过继承 Enum 来派生枚举类，在这种方式下就可以为枚举类额外定义方法了
import enum
class Orientation(enum.Enum):  #继承Enum基类来派生枚举类
    # 为序列值指定 value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)
print(Orientation.SOUTH)
print(Orientation.SOUTH.value)

#通过枚举变量名访问枚举
print(Orientation['WEST'])
#通过枚举值来访问枚举
print(Orientation('南'))
#调用枚举的info()方法
Orientation.EAST.info()
#遍历Orientation枚举的所有成员: __members__ 属性
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)
"""

"""
#枚举的构造器： 枚举定义构造器，为枚举定义构造器后，在定义枚举实例时必须为构造器参数设置值
import enum
class Gender(enum.Enum):   #基于Enum基类派生出枚举类Gender
    MALE = '男', '阳刚之力'   #定义MALE枚举的枚举值，'男', '阳刚之力'会被封装成元组后传给MALE的value属性
    FEMALE = '女', '柔顺之美' #定义FEMALE枚举的枚举值，枚举的构造器(下行)需要几个参数，此处就必须指定几个字符串
    def __init__(self, cn_name, desc):  #定义枚举的构造器,两个参数就是枚举值
        self._cn_name = cn_name  # 或 self.__cn_name = cn_name
        self._desc = desc  #或  self.__desc = desc
    @property
    def desc(self):
        return self._desc  # return self.__desc
    @property
    def cn_name(self):
        return self._cn_name  #或 return self.__cn_name
#隐藏类的变量,单下划线和双下划线区别： __ 开头的属性只是类中的隐藏属性，实际上可以绕过机制访问到，但是使用 _ 开头的属性就是私有属性了，建议用这种方式定义私有属性

#访问 FEMALE的name(枚举类成员的name属性)
print('FEMALE的name: ', Gender.FEMALE.name)
#访问 FEMALE的value(枚举类成员的value属性)
print('FEMALE的value：', Gender.FEMALE.value)  #返回元组
#访问自定义的 cn_name 属性
print('FEMALE的cn_name: ', Gender.FEMALE.cn_name)
#访问自定义的desc属性
print('FEMALE的desc: ', Gender.FEMALE.desc)
print('MALE的desc: ', Gender.MALE.desc)
"""





