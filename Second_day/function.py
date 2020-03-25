#函数，定义函数
def factorial(num):   #定义阶乘函数块
    """
    求阶乘  #这是函数的用途
    :param num: 非负整数  #这是函数变量的解释
    :return: num的阶乘  #这是函数的结果
    """

    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))  # m会代替 num
n = int(input('n = '))  # n会代替 num

print(factorial(m) // factorial(n) // factorial(m - n))   #引用函数，直接引用函数名字即可

"""
#Python的math模块中其实已经有一个factorial函数了
如下：直接利用该函数
import math 
a = 5
print(math.factorial(a))
"""


from random import randint

def roll_dice(n=2):   #第一个函数，指定了函数参数的默认值为2

    """
    摇骰子
    ：parm n: 骰子的个数
    ：return：n颗骰子的点数之和
    """

    total = 0 
    for _ in range(n):  # 每个筛子摇出的数字是不一样的
        total += randint(1, 6)   
    return total  #函数的结果

def add(a=0, b=0, c=0):  #第二个函数,函数的三个参数默认值都是0
    return a + b + c  #函数的结果

print(roll_dice())  #没有指定参数，就是默认值n=2
print(add())        #没有指定参数，三个参数都是默认值0
print(roll_dice(3)) #指定参数是3，三个骰子的数字和
print(add(1, 2))  #只指定2个参数，第三个参数就是默认值0
print(add(1, 2, 3))  #三个参数都指定
print(add(2))  #三个参数只指定一个，其他2个都是默认值0


#在不确定参数个数的时候，可使用可变参数来定义函数
#在参数名前面的*表示args是一个可变参数,即参数个数可以是0个或多个参数
def del1(*args):  #定义del1可变参数函数
    total = 0
    for val in args:
        total += val
    return total

print(del1())
print(del1(1))
print(del1(1, 2))
print(del1(1, 2, 3))

"""
用模块管理函数
不同的模块中可以有同名的函数
在使用函数的时候通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的同名函数
"""
from mode1 import foo  #从函数mode1中导入函数foo
foo()

#区分使用哪一个同名函数；导入某个模块为某，相当于给模块别名
import mode1 as m1  #注意，这里是as
import mode2 as m2 
m1.foo()
m2.foo()

"""
如果模块中除了定义了函数之外还有可执行的代码；
最好是将这些执行代码放入如下所示的条件中：
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”
"""
#module3.py   这是module3模块，定义如下：
def foo():
    pass  #可执行块

def bar():
    pass

# __name__ 是Python中一个隐含的变量，它代表了模块的名字
#只有被Python解释器直接执行的模块的名字才是 __main__
if __name__ == '__main__':   #如果模块的名字是 __main__ 说明这个模块可执行
    print('call foo()')
    foo()
    print('call bar()')
    bar()

#此时，导入module3模块时，不会执行模块中if条件成立时的代码，因为模块的名字是module3而不是 __main__

#实现计算求最大公约数和最小公倍数的函数
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)  #函数也可以引用其他函数，即函数嵌套

print(gcd(6, 12))
print(lcm(6, 12))

#if __name__ == '__main__': 的应用
def is_palindrome(num):  #判断是否是回文数的函数
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num  

def is_prime(num):        #判断是不是素数的函数
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('请输入一个正整数： '))   #定义函数因子，且确保是正整数
    if is_palindrome(num) and is_prime(num):  #组合使用函数解决更复杂的问题：判断是否是回文素数
        print('%d是回文素数' % num)
    else:
        print('不是')


#函数的作用域：局部作用域、嵌套作用域、全局作用域、内置作用域
def foo():
    b = 'hello'  #b是foo函数中的局部变量，属于局部作用域，在foo函数外不能访问它；但是b对于在foo函数中的嵌套函数bar函数来说属于嵌套作用域，在bar函数中可以访问b变量

    def bar():  # Python中可以在函数内部再定义函数
        c = True  #c是bar函数中的局部变量，也属于局部作用域，在bar函数外不能访问它
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':  #if分支中定义一个全局变量a
    a = 100  #变量a就是全局变量，属于全局作用域，没有定义在任何一个函数中
    # print(b)  # NameError: name 'b' is not defined
    foo()

# Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索
#"内置作用域" 就是Python内置的那些隐含标识符min、len等都属于内置作用域

#如何通过函数调用来修改全局作用域中变量的值，使用global关键字
def foo():
    global a  #使用global关键字来指示foo函数中的变量a来自于全局作用域
    a = 200
    print(a) #结果是200

if __name__ == '__main__':
    a = 100   #全局作用域a的值,不论值是多少都不影响print(a)的值；如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域
    foo()     #定义foo函数中的变量a并将其置于全局作用域
    print(a)  #结果是200,不论全局作用域a的值是多少，即只认foo函数中global关键字指定的全局变量a

#如何通过函数的调用修改嵌套作用域中的变量，使用nonlocal关键字

"""
尽量减少对全局变量的使用，因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，
除此之外全局变量比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被垃圾回收
减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，
但是如果我们希望将一个局部变量的生命周期延长，使其在函数调用结束后依然可以访问，这时候就需要使用闭包
"""

#结论：之后将Python代码按如下格式书写
def main():   #定义函数
    # Todo: Add your code here
    pass

if __name__ == '__main__':  #使用函数
    main()


