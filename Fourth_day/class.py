#类的定义：使用class关键字
#类中的方法：通过函数来定义类中的方法
#类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息
class Student(object):  #创建学生类
    #__init__是一个特殊的方法,用于创建对象时进行初始化操作
    #通过这个__init__方法可为学生对象绑定name和age两个属性
    #self只有在类的方法(函数)中才会有，独立的函数或方法是不必带有self的
    #self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    #self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗（为了和其他编程语言统一，减少理解难度），不要搞另类
    #self指的是类实例对象本身,不是类本身   
    def __init__(self, name, age):  
        self.name = name  #Student类中对象的属性name,公开的属性
        self.age = age  #Student类中对象的属性age，公开的属性

    def study(self, course_name):  #定义学习的方法(函数),self在定义类的方法时是必须有的
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):  ##定义看电影的方法(函数),self在定义类的方法时是必须有的
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看动作大电影.' % self.name)


#创建和使用对象：定义好一个类后，通过下面的方式来给类创建对象并给对象发消息
#给学生类创建对象(函数),可使用Student类
def main():
    #创建学生对象并指定姓名和年龄
    stu1 = Student('元芳', 17)  #学生对象属于Student类
    stu2 = Student('元彪', 19)
    #给对象stu1发study消息,即使用Student类中通过函数定义的方法study
    stu1.study('Python程序设计')  #这里的 'Python程序设计' 就赋值给了study函数中的 course_name变量
    #给对象stu2发watch_movie消息
    stu1.watch_movie()  #执行watch_movie方法
    stu2 = Student('王大锤', 20)
    stu2.study('思想品德')  #这里的 '思想品德' 就赋值给了study函数中的 course_name变量
    stu2.watch_movie()

if __name__ == '__main__':
    main()


#创建类中的私有属性：可通过在给属性命名时用两个下划线作为开头
#将类中的属性私有化
class Test:
    
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello') 
    #test.__bar()  #报错:#AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()  #对类的私有化属性,这样引用Test类类中的属性
    #print(test.__foo) #报错AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__foo) #对类的私有化属性,这样引用Test类类中的属性

if __name__ == "__main__":
    main()

#关于类中的私有属性的访问和定义的总结：
"""
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。
这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
"""


#面向对象的三大支柱：封装、继承、多态
"""
封装：隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口
    在类中定义的方法其实就是把数据和对数据的操作封装起来了
    在我们创建了对象之后，只需要给对象发送一个消息（调用方法）就可以执行方法中的代码
    也就是说我们只需要知道方法的名字和传入的参数（方法的外部视图），而不需要知道方法内部的实现细节（方法的内部视图）
"""

#定义一个类描述数字时钟
from time import sleep


class Clock(object):  #定义时钟类
    def __init__(self, hour=0, minute=0, second=0):  #初始化Clock类
        self._hour = hour   #定义小时属性;属性前加单下划线_ 是实际中常用的定义类的私有属性的方法
        self._minute = minute  #定义分钟属性,私有属性
        self._second = second  #定义秒钟属性,私有属性

    def run(self):  #定义秒、分、时指针的走动方法(函数)
        '''走字'''
        self._second += 1  #秒针按+1递增
        if self._second == 60:
            self._second = 0  #当秒针递增到60时,再从0开始
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        return('%02d:%02d:%02d' % (self._hour, self._minute, self._second))  #内容过长可用 \ 分行;02d表示两位数整数

def main():   #主函数,
    clock = Clock(12, 52, 32)  #定义类中函数初始变量
    while True:  #循环走针
        print(clock.show())  #打印当前时间
        sleep(1)  #一秒后开始执行下面的程序
        clock.run()  #开始执行run方法,不会自动停止，除非手动停止Ctrl+c
        
if __name__ == "__main__":
    main()


 #定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):  #初始位置是原点
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self._x = x  #横坐标初始
        self._y = y  #纵坐标初始

    def move_to(self, x, y):  #定义移动点的方法
        """
        移动点的方法

        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self._x = x  #横坐标移动
        self._y = y  #纵坐标移动

    def move_by(self, dx, dy):  #点移动的方法
        """
        计算移动增量方法
        :param dx: 横坐标增量
        :param dy: 纵坐标增量
        """
        self._x += dx
        self._y += dy

    def distance(self, other):
        """
        计算点之间距离的方法
        :param other: 另一个点
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)  #计算点之间的距离

    def __str__(self):  #特殊函数：帮助打印对象中具体的属性值
        return '(%s, %s)' % (str(self._x), str(self._y))  #%s 表示将值格式化为字符串,str就表示字符串


def main():  #main函数，可直接执行
    point1 = Point(1, 2)
    point2 = Point()  #point2在初始点，原点
    print(point1)
    print(point2)
    point2.move_by(-1, 2)  #点移动到的位置
    print(point2)
    print(point1.distance(point2))


if __name__ == "__main__":
    main()



#@property装饰器： 包装getter和setter方法,使得通过它们更安全、方便地访问私有属性
#getter方法(属性的访问器)和setter方法(属性的修改器)可以访问私有属性

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    #访问器-getter方法
    @property
    def name(self):
        return self._name

    #访问器-getter方法
    @property
    def age(self):
        return self._age

    #修改器-setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)


def main():
    person = Person('李东', 18)
    person.play()    #利用了访问器 @property
    person.age = 16  #重新赋值person的age属性,利用了修改器 @age.setter
    person.play()

if __name__ == "__main__":
    main()



#__slots__ 魔法
#在类中定义__solts__变量来限定自定义类型的对象只能绑定某些属性
#__solts__的限定只对当前类的对象生效,对子类并不起作用

class Human(object):
    #限定Person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name', '_age', '_gender')  #__slots__ 限制对象可绑定的属性

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在看动画片' % self._name)
        else:
            print('%s正在看动作片' % self._name)

def main():
    person = Human('马超', 36)
    person.play()
    person._age = 16
    person.play()
    person._gender = '男'

if __name__ == "__main__":
    main()
        
#在类中定义__solts__变量来限定自定义类型的对象只能绑定某些属性
class Human(object):
    #限定Person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name', '_age', '_gender', '_occupation')

    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, age, gender):
        self._age = age
        self._gender = gender

    def play(self):
        if self._age <= 16 and self._gender == '女':
            print('%s是%s,正在看动画片' % (self._name, self._gender))
        else:
            print('%s是%s,正在看动作片' % (self._name, self._gender))

def main():
    person = Human('马超', 36, '男')
    person.play()
    person._age = 16
    person.play()
    person._gender = '女'
    person.play()
    person._occupation = '医生'
    person.play()
    #person._is_gay = True  #报错：AttributeError: 'Human' object has no attribute '_is_gay'
    #证明__slots__的限定生效
    

if __name__ == "__main__":
    main()


#静态方法和类方法
#对象方法：定义的方法都是发送给对象的消息
#静态方法：属于类但不属于类的对象的方法,如：判断三条边能否构成三角形

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):  #初始化Triangle类
        self._a = a
        self._b = b
        self._c = c

    @staticmethod   #静态方法的标志
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b #判断是否能构成三角形，必须都满足

    def perimeter(self):   #计算周长
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2  #周长的一半
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))    #面积的计算方法 

def main():
    a, b, c = 3, 4 ,5
    #静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):  #使用静态方法
        t = Triangle(a, b, c)  #方法1
        print(t.perimeter())  
        #也可以通过类发消息来调用对象方法但是要传入接收消息的对象作为参数
        #print(Triangle.perimeter(t)) #方法2
        print(t.area()) 
        #print(Triangle.area(t))
    else:
        print('无法构成三角形')
    

if __name__ == "__main__":
    main()


#类方法：与静态方法比较类似,类方法的第一个参数约定名为cls,它代表的是当前类相关的信息的对象
#类本身也是一个对象，有的地方也称之为类的元数据对象
#通过cls这个参数我们可以获取和类相关的信息并且可以创建出类的对象

from time import time, localtime, sleep  #从time模块导入函数


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod  #类方法的标志
    def now(cls):
        ctime = localtime(time())  #当前时间
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)  #tm_hour、tm_min、tm_sec是localtime函数自带的

    def run(self):
        """走字"""
        self._second += 1  #赋值second的增加方法
        if self._second == 60:
            self._second = 0   
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main():
    clock = Clock.now()  #使用类方法
    while True:
        print(clock.show())  #使用show方法
        sleep(1)
        clock.run()  #使用走字方法


if __name__ == "__main__":
    main()


"""
#类之间的关系：is-a、has-a和use-a关系
#is-a关系也叫继承或泛化;比如学生和人的关系、手机和电子产品的关系都属于继承关系。
#has-a关系通常称之为关联;比如部门和员工的关系，汽车和引擎的关系都属于关联关系；
# 1、关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
# 2、如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系
#use-a关系通常称之为依赖;比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系

"""
#利用类之间的这些关系，可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，是实现代码复用的重要手段

#类的继承：让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写
#提供继承信息的我们称之为父类，也叫超类或基类；
#得到继承信息的我们称之为子类，也叫派生类或衍生类
#子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力
#里氏替换原则：用子类对象去替换掉一个父类对象的原则

#继承
#继承的案例

class Person(object):  #object是最大的类,父类最好带上
    """人类"""    

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  #访问器-getter方法
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter  #修改器-setter方法
    def age(self, age):
        self._age = age

    def play(self):
        print('%s在玩耍.' % self._name)

    def watch_mv(self):
        if self._age >= 18:
            print('%s在看mv.' % self._name)
        else:
            print('%s在看动画片.' % self._name)

class Student(Person):  #继承Person类,学生类
    """学生类"""

    def __init__(self, name, age, grade):  #加一个属性grade，初始化学生类
        super().__init__(name, age)  #继承父类
        self._grade = grade  #子类也可以有自己的属性,学生的年级属性

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):  #可执行的方法
        print('%s的%s正在学习%s' % (self._grade, self._name, course))

class Teacher(Person):  #继承Persong类,老师类
    """老师类"""

    def __init__(self, name, age, title):  #加一个属性title,初始化老师类
        super().__init__(name, age)
        self._title = title  #老师的职称等级

    @property  
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):  #可执行的方法
        print('%s%s正在讲%s' % (self._name, self._title, course))


def main():
    stu = Student('李磊', 17, '高二')  #定义学生变量各属性,引用学生类
    stu.study('数学')
    stu.watch_mv()
    t = Teacher('王涛', 32, '专家')  #定义老师变量各属性,引用老师类
    t.teach('英语')
    t.watch_mv()


if __name__ == '__main__':
    main()



#方法的重写：子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本,这个动作称为
#通过方法重写可以让父类的同一个行为在子类中拥有不同的实现版本
#多态：当我们调用经过子类重写的方法时，不同的子类对象会表现出不同的行为

#方法的重写和多态的案例
from abc import ABCMeta, abstractmethod  #导入abc模块的元类和包装器
#Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果

class Pet(object, metaclass=ABCMeta):  #抽象类只能被继承,将Pet处理成一个抽象类
    #所谓抽象类就是不能够创建对象的类(即不能实例化)，这种类的存在就是专门为了让其他类去继承它
    """宠物类"""
    def __init__(self, nickname):  #宠物名方法
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):  #宠物抽象方法
        """发出声音"""
        pass  #pass表示方法可在子类重写


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)  #重写抽象类Pet的抽象方法make_voice


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...喵...' % self._nickname)  #重写抽象类Pet的抽象方法make_voice

def main():  
    pets = [Dog('旺财'), Cat('小咪')]
    for pet in pets:  #表现为多态,多种表现形式
        pet.make_voice()

if __name__ == "__main__":
    main()