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

"""

#对字典，函数的参数传递机制会有一个误会，实际是没有改变字典元素的值，只是引用变量指向同一个对象(指针)，
def swap(dw):
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("在swap()函数里， a元素的值是", dw['a'], "b元素的值是", dw['b'])
    #dw = None   #断开指针的引用
        
dw = {'a':6, 'b':9}
swap(dw)  
print("交换后a的值是", dw['a'], "b的值是", dw['b'])  #一种误解


