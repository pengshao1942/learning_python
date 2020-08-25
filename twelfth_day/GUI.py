#常用的GUI库：推荐使用PyQt或wsPython，可以跨平台
#系统自带的GUI库：Tkinter，导入tkinter包即可使用
#学习GUI编程的总体步骤分为三步：
'''
1.了解GUI库大致包含哪些组件，相当于熟悉每个积木块到底是些什么东西
2.掌握容器及容器对组件进行布局的方法，就相当于掌握拼图的 "母板",以及母板怎么固定积木块的方法
3.逐个掌握各组件的用法，则相当于深入掌握每个积木块的功能和用法
'''

#Tkinter的GUI组件有两个根父类，且都直接继承了 object 类
'''所有GUI组件都可以直接使用它们的方法
Misc: 是所有组件的根父类
Wm: 主要提供了一些与窗口管理器通信的功能函数
'''

'''
Misc和Wm派生的子类：Tk,代表应用程序的主窗口
BaseWidget是所有组件的基类,且派生了一个子类：Widget
Widget：代表一个通用的GUI组件，Tkinter所有的GUI组件都是Widget的子类
Widget: 有四个父类，除了BaseWidget外，Pack、Place、Grid这三个父类都是布局管理器，负责管理所包含的组件的大小和位置
Widget的子类:即各种 UI 组件，也就是编程的积木块
'''

#示例：创建一个窗口，使用TK
'''
from tkinter import *
#创建Tk对象，Tk代表窗口
root = Tk()
#设置窗口标题
root.title('窗口标题')
#创建Label对象，第一个参数指定将该Label放入root内
w = Label(root, text="Hello Tkinter!")
#调用pack进行布局
w.pack()
#启动主窗口
root.mainloop()
'''

#自动创建Tk对象作为窗口：不直接使用Tk，只要创建Frame的子类，子类就会自动创建Tk对象作为窗口
'''
from tkinter import *

#定义继承Frame的Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        #调用initWidgets()方法初始化界面，方法可以是任意名
        self.initWidgets()  
    def initWidgets(self):
        #创建Label对象，第一个参数指定将该Lable放入root内
        w = Label(self)   # 第一个UI组件
        #创建一个位图
        bm = PhotoImage(file = 'D:\learning_python\\twelfth_day\serial.png')
        #必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm  #w的x属性引用PhotoImage对象保证该对象不会被python内存回收
        #设置显示的图片是bm
        w['image'] = bm  #设置背景图片
        w.pack()  #pack()方法添加UI组件
        #创建Button对象，第一个参数指定将该Button放入root内
        okButton = Button(self, text="确定")  #第二个UI组件，同时以关键字参数的方式配置该组件  @1

        okButton['background'] = 'yellow'  #设置UI背景色，同时以字典语法对该组件进行配置  @2
        #okButton.configure(background='yellow')   #与上一行代码的作用相同
        #在创建Button对象时，就配置它的文本和背景色
        #okButton = Button(self, text="确定", background= 'yellow')  #等同于@1+@2
        okButton.pack()

#创建Application对象
app = Application()
#Frame有一个默认的master属性，该属性值是Tk对象(窗口)
print(type(app.master))
#通过master属性来设置窗口标题
app.master.title('窗口标题')
#启动主窗口的消息循环
app.mainloop()
'''


#帮助：查看某GUI组件所有可配置的选项，通过该组件的构造方法的帮助文档来查看; 
# 以 Button 举例,在交互式窗口输入
'''
>>improt tkinter
>>help(tkinter.Button.__init__)
'''


'''综上：如果程序在创建任意Widget组件时没有指定master属性(即创建Widget组件时第一个参数传入None),那么程序会
自动为该Widget组件创建一个Tk窗口'''


#布局管理器