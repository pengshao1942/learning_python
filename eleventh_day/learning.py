"""
#异常检查
try:
    statement(s)   #要检测的语句块
except exception:
    deal_exception_code  #如果在 try 部分引发了 'exception' 异常
except exception2, e:
    deal_exception2_code #如果引发了 'exception' 异常
else:
    no_exception_happend_code #如果没有异常发生
"""
"""
try:
    raise BException()  #抛出异常
except (BException, DException):
    print("D")
except:
    print("处理全部其它异常") #处理全部其它异常
else:
    print("没有异常发生") #没有异常发生
"""

"""
try:
    x = 1 / 0  # 除数为0
except ZeroDivisionError as err: #为异常指定变量err
    print("Exception")
    print(err.args) #打印异常的参数元组
    print(err) #打印参数，因为定义了__str__()
"""

#raise语句用于手动引发一个异常
#语法：raise [Exception [, args [, traceback]]]

"""
#示例：
def diyException(level):
    if level > 0:
        raise Exception("raise exception", level)
    print('我是不会执行的')

try:
    diyException(2)
except Exception as err:
    print(err)
"""

#用户自定义异常：只需要创建一个类，并继承 Exception 类或其子类
#创建一个异常 DiyError 继承自 Python 内置的 RuntimeError，用于在异常触发时输出更多的信息

"""
#自定义异常
class DiyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise DiyError("my diy exception") #触发异常
except DiyError as e:
    print(e)
"""

#默认参数
"""
def def_param_fun(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yes'):
            return True
        if ok in ('n', 'no', 'nop'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def_param_fun('Do you want to quit?', 2, 'please yes or no!')
"""

#可变参数
"""
def variable_fun(kind, *arguments, **keywords):
    print("friend : ", kind, ";")
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
# 函数调用

variable_fun("xiaoming",
             "hello xiaoming", "nice to meet you!",
            mother="xiaoma",
            father="xiaoba",
            son="see you")

#python的解包：序列和字典的解包;序列解包在函数中的应用
list01 = ["hello xiaoming", "nice to meet you!"]
dict01 = {'mother': 'xiaoma', 'father': 'xiaoba', 'son': 'see you'}
variable_fun("xiaoming", *list01, **dict01)
"""

#关键字参数：允许调用函数时传入0个或任意个含参数名的参数，这样可以灵活的去进行参数的调用

"""
#高阶函数
from math import factorial

def high_func(f, arr):
    return [f(x) for x in arr]

def square(n):
    return n ** 2

print(high_func(factorial, list(range(10))))

print(high_func(square, list(range(10))))
"""

