"""
#递归函数：在一个函数的函数体中调用了函数自身
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n - 1) + fn(n - 2)  #调用了函数自身

print(fn(10))


#形参：位置参数和关键字参数
#关键字参数在赋值时变量带 = 号，和位置参数混用时，必须在位置参数的后面
def girth(width, height):
    print("width: ", width)
    print("height ", height)
    return 2 * (width + height)

print(girth(3.5, 4.8))
print(girth(width = 3.5, height= 4.8))
print(girth(3.5, height = 4.8))
#print(girth(width = 4.2, 5.2))  #报错：SyntaxError: positional argument follows keyword argument 原因是：位置参数必须在关键字参数之前



#函数参数的默认值
def say_hi(name = "李磊", message = "欢迎来到地球"):
    print(name, ",你好")
    print("消息是：", message)

say_hi()
say_hi(name= "王鹏")
say_hi(message= "欢迎来到木星")
#say_hi("欢迎来到木星")  #这样是错误的,如果只传入一个参数，系统会将该参数值传给函数的第一个形参
say_hi("李倩", "欢迎来到火星")
say_hi("李欢", message= "欢迎来到火星")
say_hi(name = "李想", message= "欢迎来到火星")
#say_hi(name= "李欢", "欢迎来到火星") #这样也不对，因为位置参数必须在关键字参数前
#say_hi("欢迎来到冥王星", name= "李林")  #这样交换参数位置不对，报错：say_hi() got multiple values for argument 'name'，因为对name赋值了2次


#定义函数时：将带默认值的参数定义在形参列表的最后
def printTrigangle(char, height = 5):  #定义一个打印三角形的函数；定义了一个默认参数
    for i in range(1, height + 1):
        for j in range(height - i):
            print(' ', end = '')
        for j in range(2 * i - 1):
            print(char, end = '')
        print()

printTrigangle('@', 6)
printTrigangle('#', height = 7)  #默认参数的默认值可以改变,此时使用的时新值
printTrigangle(char = '*')  #此时使用的是默认参数值


#函数中定义参数收集： 个数可变的参数，在形参前面添加一个星号*即可；该参数的多个参数值被当成元组传入函数
def test(a, *books): #个数可变的参数可在形参列表的任意位置
#def test(*books, a): #如果是可变个数参数在前，则后面的参数传入参数值时，必须使用关键字参数,即a=3这样
    print(books)  #该参数被当做元组输入函数
    for b in books:
        print(b)
    print(a)

test(5, 'python', 'java')

#收集关键字参数：会将关键字参数收集成字典；在参数前面添加2个星号*
def test(x, y, z = 3, *books, **scores):  #可以同时给几个参数复制同一个默认值
    print(x, y, z)
    print(books)
    print(scores)

test(1, 2, 3, "python", 'java', 语文=89, 数学=94)  #"python", 'java'被收集成元组，语文=89, 数学=94被收集成字典
test(1, 2, "python", 'java', 语文=89, 数学=94)  #z参数的默认值没发挥作用，python被误解为z参数的值，java单独组成一个元组
test(1, 2, 语文=89, 数学=94)  #z参数的默认值发挥作用：只传入2个位置参数1和2
test(1, 2, 数学=94)  #数学=94单独组成一个字典，输出带一个空元组，因为books参数收集未定义；
test(1, 2, 3)  #books和scores都不定义，输出带一个空元组和一个空字典


#逆向参数收集：把程序已有列表、元组、字典等对象的元素'拆开'后传给函数的参数
def test(name, message):
    print("用户是： ", name)
    print("欢迎消息：", message)

mylist = ['孙悟空', '欢迎来到地球']
test(*mylist)  #对列表、元组参数之前添加一个星号

def foo(name, *nums):
    print("name参数: ", name)
    print("nums参数: ", nums)
my_tuple = (1, 2, 3)
foo('fkit', *my_tuple)   #对列表、元组参数之前添加一个星号;将fkit赋值给name参数,元组的多个元素传给nums参数,nums再将my_tuple的多个元素收集成元组
foo(*my_tuple)  #元组的第一个元组赋值给name参数，其它的元素赋值给nums参数并返回一个元组
foo(my_tuple)  #不使用逆向收集，即不在元组或列表参数前加*,则这个元组都作为name参数赋值，nums则为空

#逆向收集： 字典
def bar(book, price, desc):
    print(book, "这本书的价格是: ", price)
    print('描述信息:', desc)

my_dict = {'price':89, 'book':'python讲义', 'desc':'这是一本好书'}  #key-value对顺序不影响
bar(**my_dict)   #字典逆向收集需要使用两个 **



#函数参数传递的机制：复制传递，不影响本来的参数;示例如下:
def swap(a, b):
    a, b = b, a
    print("在swap函数里，a的值是", \
        a, ",b的值是", b)

a = 6
b = 9
swap(a, b)
print("交换结束后, 变量a的值是", a, ",变量b的值是", b)  



#对字典，函数的参数传递机制会有一个误会，实际是没有改变字典元素的值，只是引用变量指向同一个对象(指针)，
def swap(dw):
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("在swap()函数里， a元素的值是", dw['a'], "b元素的值是", dw['b'])
    #dw = None   #断开指针的引用
        
dw = {'a':6, 'b':9}
swap(dw)  
print("交换后a的值是", dw['a'], "b的值是", dw['b'])  #一种误解


#变量作用域：全局变量、局部变量
#变量和值的关系就像一个看不见的字典：变量名就是字典的key，变量值就是字典的value
#获取指定范围内的 “变量字典的函数：
#locals() ： 获取当前局部范围内所以变量组成的“变量字典”
#globals() : 该函数返回全局范围内所有变量组成的“变量字典”
#vars(object): 获取在指定对象范围内所有变量组成的“变量字典”；如果不传入object参数,vars()和local()的作用完全相同

def test():
    age = 20
    print(age)  #直接访问age局部变量
    print(locals()) #访问函数局部范围内的“变量数组”
    print(locals()['age'])  #通过函数局部范围内的“变量数组”访问age变量
    locals()['age'] = 12 #通过locals函数局部范围内的“变量数组”改变age变量的值
    print('xxx', age)  #再次访问age变量的值
    globals()['x'] = 19  #通过globals函数修改x全局变量


x = 5
y = 20
print(globals())
print(locals())  #在全局范围内使用locals函数,访问的是全局变量的“变量数组”
print(x)  #直接访问x全局变量
print(globals()['x'])   #通过全局变量的“变量数组”对x全局变量赋值
globals()['x'] = 39   #通过globals函数修改x全局变量
print(x)  #输出39
locals()['x'] = 99  #在全局范围内使用 locals 函数对x全局变量赋值
print(x)  #输出 99

"""

"""
#函数中发生的局部变量遮蔽全局变量的情形
#在函数内部对不存在的变量赋值时，默认就是重新定义新的局部变量
#只会发生局部变量在函数内遮蔽全局变量的情况，没有全局变量遮蔽局部变量的情况
name = 'Charlie'
def test():
    #print(name)
    print(globals()['name'])  #globals()方法访问全局变量"变量字典"字典key
    name = '孙悟空'  #在函数中又定义了同全局变量相同的变量；报错：local variable 'name' referenced before assignment

test()
print(name)

#声明全局变量：防止在函数中对全局变量定义导致不可访问全局变量
#global关键字
name = 'Charlie'
def test():
    global name  #global关键字在函数中设置某个变量为全局变量,防止全局变量在函数中被重新定义
    print(name)  #globals()方法访问全局变量"变量字典"字典key
    name = '孙悟空'  #只是重新赋值全局变量

test()
print(name)  #输出局部变量


#局部函数：在函数体内定义的函数

def get_math_func(type, nn):  #定义一个包含3个局部函数的函数：这个函数称为封闭函数
    def square(n):  #定义一个求平方的局部函数
        return n * n
    def cube(n):    #定义一个求立方的局部函数
        return n * n * n
    def factorial(n): #定义一个求阶乘的局部函数
        result = 1
        for i in range(2, n +1):
            result *= i
        return result
    if type == "square":  #赋值type指为指定局部函数的名称
        return square(nn)  #返回对应的局部函数
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)

print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("factorial", 3))


#局部函数内的变量
#nonlocal关键字
def foo():
    name = 'Charile'  #局部变量
    def bar():
        nonlocal name  #加上这行就不会报错
        print(name) #访问bar函数所在的foo函数内的局部变量name
        name = '孙悟空'  #报错：local variable 'name' referenced before assignment
        print(name)  #这里输出的是孙悟空了,因为上面定义了
    bar()

foo()
print(type(foo))   #函数都是fuction对象
"""

"""
#使用函数变量: 将函数赋值给变量
def pow(base, exponent):   #定义一个计算乘方的函数
    result =1
    for i in range(1, exponent +1):
        result *= base
    return result

def area(width, height):  #定义一个计算面积的函数
    return(width * height)

my_func = pow  #将pow函数赋值给变量
print(my_func(3, 4))
my_func = area  #将area函数赋值给变量
print(my_func(5, 6))



#使用函数作为函数形参(参数)： 根据不同函数动态调整代码
def map(data, fn):  #定义一个动态函数，定义函数类型的形参，fn是一个函数；函数的作用是返回一个列表
    result = []   #函数的初始化
    for e in data:
        result.append(fn(e))
    return result  #返回列表

def square(n):  #定义一个计算平方的函数
    return n * n

def cube(n):    #定义一个计算立方的函数
    return n * n * n

def special(n): #定义一个计算阶乘的函数
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

data = [3, 4, 5, 6, 7]  #声明data形参的值在列表中
print(map(data, square))   #赋值一个函数名给函数形参，每次调用对应的函数作为执行代码
print(map(data, cube))
print(map(data, special))
print(type(map))


#使用函数作为返回值：  函数返回另一个函数
def get_math_func(type):   #type赋值哪个函数名get_math_func函数体内就执行哪个函数的函数体
    def square(n):   #局部函数1
        return n * n
    def cube(n):     #局部函数2
        return n * n * n
    def factorial(n):  #局部函数3
        result = 1
        for i in range(2, n + 1):   #阶乘从2开始算
            result *= i
        return result
    if type == "square":  #返回局部函数
        return square
    elif type == "cube":
        return cube
    else:
        return factorial

#调用get_math_func()函数，程序返回一个嵌套函数
math_func = get_math_func("cube")  #赋值cube函数给get_math_func函数的形参type，之后get_math_func函数会执行cube函数的函数体
print(math_func(5))  #这里的5其实是赋值给了cube函数的形参n
math_func = get_math_func("factorial")
print(math_func(3))  #这里的3其实是赋值给了factorial函数的形参n
math_func = get_math_func("square")
print(math_func(6))  #这里的6其实是赋值给了sequare函数的形参n



#局部函数与lambda表达式
#使用lambda表达式来简化局部函数的写法: lambda表达式只能是单行表达式
#lambda表达式必须使用关键字定义：在关键字之后、冒号左边的是参数列表，可以没有参数，也可以有多个参数，多个参数
#需要用逗号 , 隔开，冒号右边是该lambda表达式的返回值
#lambde表达式本质就是匿名的、单行函数体的函数；
#lambda表达式可写成函数的形式，如： lambda x,y: x + y ----> def add(x, y): return x + y
#当函数体只有一行代码时，可以直接把函数体的代码放在与函数头同一行
def get_math_func(type):
    #result=1   #未使用的变量
    #该函数返回的是lambda表达式
    if type == 'square':
        return lambda n: n * n   #计算平方
    elif type == 'cube':
        return lambda n: n * n * n  #计算立方
    else:
        return lambda n: (1 + n) * n / 2   #计算 1+2+...+n的和

math_func = get_math_func("cube")
print(math_func(5))
math_func = get_math_func("square")
print(math_func(6))
math_func = get_math_func("other")
print(math_func(4))

"""

#lambda表达式和系统map函数的使用：
x = map(lambda x: x*x, range(8))  #内置的map函数第一个参数需要传入函数，这里传入的是函数的简化形式，lambda表达式
print([e for e in x])  #for的表达式,列表推导式
y = map(lambda x: x*x if x % 2 == 0 else 0, range(8))
print([e for e in y])