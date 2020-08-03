#异常类
#Python的所有异常类的基类是 BaseException;
#自定义异常，应该继承 Exception 类
#BaseException的主要子类就是 Exception，不管是系统的异常类，还是用户自定义的异常类，都应该从Exception派生
"""
import sys
try:
    a = int(sys.argv[1])  #argv是sys模块的列表，argv[0]表示程序本身，这里就是这个程序，argv[1]表示提供给程序的第一个参数，以此类推
    b = int(sys.argv[2])
    c = a / b
    print("输入的两个数相除的结果是： ", c)
except IndexError:
    print("索引错误： 运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误：程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")   
except Exception:   #Exception类对应的except块总是放在最后
    print("未知异常")
"""
#所有父类异常的except块都应该在子类异常的except块的后面(即：先处理小异常，再处理大异常)

#多异常捕获：一个except块可以捕获多种类型的异常
#在使用一个except捕获多种类型的异常时，只要将多个异常类括起来，中间用逗号隔开即可 一一其实就是构建多个异常类的元组
"""
import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("你输入的两个数相除的结果是：", c)
except (IndexError, ValueError, ArithmeticError):
    print("程序发生了数组越界、数字格式异常、算数异常之一")
except:  #这种省略异常类的写法也是合法的，表示可捕获所有类型的异常，一般会作为异常捕获的最后一个except块
    print("未知异常")
"""
#访问异常信息：当解释器决定调用某个except块来处理该异常时，会将异常对象赋值给except块后的异常变量，程序即可通过
#该变量来获得异常对象的相关信息
#所有的异常对象都包含了如下几个常用属性和方法：
"""
  args: 该属性返回异常的错误编号和描述字符串(详细信息),是下面2个的总和
  errno: 该属性返回异常的错误编号
  strerror: 该属性返回异常的描述字符串
  with_traceback(): 通过该方法可处理异常的传播轨迹信息,后续详解
"""
"""
def foo():
    try:
        fis = open("eleventh_day1/tmp.txt")
    except Exception as e:  #异常变量定义为 e
        #访问异常的错误编号和描述字符串
        print(e.args)
        #访问异常的错误编号
        print(e.errno)
        #访问异常的描述字符串
        print(e.strerror)

foo()
"""
#即：如果要访问异常对象，只要在单个异常类或异常类元组（多异常捕获）之后使用 as 再加上异常变量即可
#异常详细信息就是程序引发异常后的输出信息

#else块：在的python的异常处理流程中还可添加一个else块，当try块没有出现异常时，程序会执行else块
"""
s = input("请输入整数： ")
try:
    result = 20 /int(s)
    print('20 除以%s的结果是： %g' % (s, result))
except ValueError:
    print('值错误，你必须输入整数')
except ArithmeticError:
    print('算术错误，除数不能是0')
else:  #当try块没有出现异常时，程序会执行else块内的语句
    print('没有出现异常')
"""

#对于大部分场景而言，直接将else块的代码放在try块的代码后面即可
#当try块没有异常，而else块出现异常时，就能体现出else块的作用了
"""
from typing import SupportsBytes


def else_test():
    s = input('请输入整数：')
    result = 20 / int(s)
    print('20 除以%s的结果是：%g' % (s, result))

def right_main():
    try:
        print('try块的代码，没有异常')
    except:
        print('程序出现异常')
    else:  
        #将else_test放在else块中
        else_test()  #程序出现异常时，没有except块来处理异常，会将异常传递给Python解释器，导致程序中止

def wrong_main():
    try:
        print('try块的代码，没有异常')
        #将else_test放在try块的代码的后面
        else_test()  #当程序出现异常时，会被下面的except块捕获，是python正常的异常处理机制的执行流程，程序不会中止
    except:
        print('程序出现异常')

wrong_main()
right_main()
"""
#总结：如果希望某段代码的异常能被后面的except块捕获，那么就应该将这段代码放在try块的代码之后; 如果希望某段代码的异常能向外传播
#(不被except块捕获)，那么就应该将这段代码放在else块中

"""
#使用finally回收资源
#Python完整的异常处理语法结构如下：
try:
    #业务实现代码
    ...
except SubException as e:
    #异常处理块1
    ...
except SubException as e:
    #异常处理块2
    ...
...
else:
    #正常处理块
finally:   #finally块总会被执行
    #资源回收块
    ...

"""
"""
总结：
1、在异常处理语法结构中，只有try块是必需的，except块和finally都是可选的；
2、except和finally块至少出现其中之一，也可以同时出现；
3、可以有多个except块,但捕获父类异常的except块应该位于捕获子类异常的except块的后面；
4、不能只有try块，即没有except块，也没有finally块；
5、多个except块必须位于try块之后,finally块必须位于所有except块之后
"""
"""
import os
def test():
    fis = None
    try:
        fis = open("a.txt")
    except OSError as e:
        print(e.strerror)
        #return语句强制方法返回,也强制方法结束，但在结束方法前，也会先执行完finally块的代码
        return
        #os._exit(1)  #如果在异常处理代码中使用os._exit(1)语句来退出Pyhon解释器，则finally块失去了执行的机会    
    finally:
        #关闭磁盘文件，回收资源
        if fis is not None:
            try:
                #关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally块里的资源回收!")

test()
"""
#注意：调用sys.exit()方法退出程序不能阻止finally块的执行，这是因为sys.exit()方法本身就是通过引发 SystemExit 异常来退出程序的

#不要(尽量避免)在finally块中使用如 return 或 raise 等导致方法中止的语句；
#一旦在 finally 块中使用了 return 或 raise 语句，将会导致 try 块、 except 块中的 return、raise 语句失效
"""
def test():
    try:
        #因为finally块中包含了 return 语句，所以下面的 return 语句失去作用
        return True
    finally:
        return False  #这句return生效

a = test()
print(a)
"""

#异常处理的嵌套：在try块、except块或finally块中包含完整的异常处理流程的情形；异常处理流程代码可以被放在任何可执行代码的地方
#通常没有必要使用超过两层的嵌套异常处理

#自行引发异常：即手动引发异常，使用raise语句完成
#自行引发的异常一般是由于与业务需求不符而产生的异常，必须由程序员来决定引发，系统无法引发这种异常
"""
raise语句用法： 三种用法都是要引发一个异常实例。raise语句每次只能引发一个异常实例
1、raise: 单独一个raise。该语句引发当前上下文中捕获的异常(比如在except块中)，或默认引发RuntimeError异常
2、raise异常类：raise后带一个异常类。该语句引发指定异常类的默认实例
3、raise异常对象：引发指定的异常对象
"""

#不管是系统自动引发的异常，还是程序员手动引发的异常，Python解释器对异常的处理没有任何差别
#手动引发的异常处理方式：1、使用 try...except来捕获它 2、不管它，让异常向上传播，当传播到Python解释器时，程序就会中止
"""
def main():
    try:
        #使用try...except来捕获异常
        #此时即使程序出现异常，也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常：', e)
    #不使用try...except捕获异常，异常会一直向上传播出来导致程序中止
    mtd(3)  #会在控制台输出异常的传播轨迹信息

def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0，不符合要求")

main()
"""

#自定义异常类
#在自定义异常类时基本不需要指定书写更多的代码，只需要指定自定义异常类的父类即可
#自定义异常类都应该继承Exception基类或Exception的子类

#class AuctionException(Exception): pass  #创建AuctionException异常类，不需要类体定义，使用pass语句作为占位符即可

#except和raise同时使用
#当一个异常出现时，单靠某个方法无法完全处理该异常，必须由几个方法协作才可完全处理该异常；
#通过在except块中结合raise语句来完成
"""
class AuctionException(Exception): pass
class AuctionTest:
    def __init__(self, init_price):  #起拍价函数
        self.init_price = init_price
    def bid(self, bid_price):   #竞拍价函数
        d = 0.0
        try:
            d = float(bid_price)  #转换为浮点数
        except Exception as e:
            #此处只是简单地打印异常信息
            print("转换出异常：", e)
            #再次引发自定义异常
            raise AuctionException("竞拍价必须是数值，不能包含其他字符!")
            #raise AuctionException(e)  #或用自定义异常对原始异常进行包装，将原始异常的详细信息直接传播出去；这种方式也称为异常包装和异常转译
        if self.init_price > d:
            #再次引发自定义异常
            raise AuctionException("竞拍价比起拍价低， 不允许竞拍!")
        initPrice = d  #再初始化起拍价为d

def main():
    at = AuctionTest(20.4)  #起拍价函数赋值
    try:
        at.bid("25")    #bid方法的调用者
    except AuctionException as ae:
        #再次捕获到bid()方法中的异常，并对该异常进行处理
        print('main函数捕获的异常:', ae)
main()
"""
"""
实际应用对异常的处理通常分成两个部分：
@1 应用后台需要通过日志来记录异常发生的详细情况
@2 应用还需要根据异常向应用使用者传达某种提示
"""

#raise不带参数，此时raise语句处于except块中，它将会自动引发当前上下文激活的异常；否则，通常默认引发RuntimeError异常
"""
class AuctionException(Exception): pass
class AuctionTest:
    def __init__(self, init_price):  #起拍价函数
        self.init_price = init_price
    def bid(self, bid_price):   #竞拍价函数
        d = 0.0
        try:
            d = float(bid_price)  #转换为浮点数
        except Exception as e:
            #此处只是简单地打印异常信息
            print("转换出异常：", e)
            #再次引发当前激活的异常
            raise  #raise不加参数
        if self.init_price > d:
            #再次引发自定义异常
            raise AuctionException("竞拍价比起拍价低， 不允许竞拍!")
        initPrice = d  #再初始化起拍价为d

def main():
    at = AuctionTest(20.4)  #起拍价函数赋值
    try:
        at.bid("df")    #bid方法的调用者
    except Exception as ae:
        #再次捕获到bid()方法中的异常，并对该异常进行处理
        print('main函数捕获的异常:', type(ae))  #输出bid方法中except捕获到的原始异常
main()
"""

#异常的传播轨迹: 异常对象提供了一个 with_traceback 用于处理异常的传播轨迹，查看异常的传播轨迹可追踪异常触发的源头，也可看到异常一路触发的轨迹
"""
class SelfException(Exception): pass

def main():
    firstMethod()
def firstMethod():
    secondMethod()
def secondMethod():
    thirdMethod()
def thirdMethod():
    raise SelfException("自定义异常信息")
main()
"""
#运行后从输出结果可看到：异常先从 thirdMethod()触发-->secondMethod()-->firstMethod()-->main()-->止，这个过程就是异常的传播轨迹
"""
#只要异常没有被完全捕获（包括异常没有被捕获，或者异常被处理后重新引发了新异常），异常就从发生异常的函数或方法逐渐向外传播，首先传给该函数或方法的调用者，该函
数或方法的调用者再传给其调用者……直至最后传到 Python 解释器，此时 Python 解释器会中止该程序，并打印异常的传播轨迹信息。
"""
#传递到Python解释器输出的，是异常的传播轨迹信息，并不是代表程序有很多错误;一般情况主要看最后一行


#使用traceback(模块)处理Python的异常传播轨迹
"""
traceback模块提供了两个常用方法：
1、traceback.print_exec(): 将异常传播轨迹信息输出到控制台或指定文件中
2、fromat_exec(): 将异常传播轨迹信息转换成字符串
"""
#常用的print_exc()是print_exc([limit[, file]])省略了limit、file两个参数的形式
#print_exc([limit[, file]])的完整形式是print_exception(etype, value, tb[, limit[, file]])
"""
在完整形式中，前面三个参数的含义如下：
etype: 指定异常类型
value: 指定异常值
tb: 指定异常的traceback信息
"""
"""
except块所捕获的异常信息可通过sys对象来获取，其中：
sys.exc_type: 当前except块内的异常类型
sys.exc_value: 当前except块内的异常值
sys.exc_traceback: 当前except块内的异常传播轨迹
"""
#即print_exc([limit[, file]])相当于此形式：print_exception(sys.exc_etype, sys.exc_value, sys.exc_tb[, limit[, file]])
"""
使用 print_exc([limit[, file]])会自动处理当前except块所捕获的异常,设计到2个参数：
limit: 用于限制显示异常传播的层数，比如：函数A调用函数B，函数B发生了异常，若指定limit=1，则只显示函数A
       里面发生的异常。如果不设置limit参数，则默认全部显示
file: 指定将异常传播轨迹信息输出到指定文件中。如果不指定该参数，则默认输出到控制台
"""

"""
#导入traceback模块
import traceback
class SelfException(Exception): pass

def main():
    firstMethod()
def firstMethod():
    secondMethod
def secondMethod():
    thirdMethod
def thirdMethod():
    raise SelfException("自定义异常信息")
try:
    main()
except:
    #捕获异常，并将异常传播信息输出到控制台
    traceback.print_exc()
    #捕获异常，并将异常传播信息输出到指定文件中
    #   traceback.print_exc(file=open('log.txt', 'a'))
"""

#对于完全已知的错误和普通的错误，应该编写处理这种错误的代码，增加程序的健壮性；
#只有对于外部的、不能确定和预知的运行时错误才使用异常
#绝不要使用异常处理来代替正常的业务逻辑判断
#不要使用异常处理来代替正常的程序流程控制
#不要使用过于庞大的try块，应该把大块try块分割成多个可能出现异常的程序段落，放在单独的try块中，分别去捕获异常
#捕获到异常后要处理修复异常，不要忽略捕获到的异常，except块为空不好 


