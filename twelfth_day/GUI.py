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



#布局管理器：负责管理各(GUI)组件的大小和位置。且当用户调整了窗口的大小之后，布局管理器还会自动调整窗口中各组件的大小和位置

#Pack布局管理器：当程序向容器中添加组件时，这些组件会依次向后排列，排列方向既可是水平的，也可是垂直的

#示范Pack布局的用法：向窗口中添加三个Label组件
'''
from tkinter import *
#创建窗口并设置窗口标题
root = Tk()
#设置窗口标题
root.title('Pack布局')
for i in range(3):
    lab = Label(root, text="第%d个Label" % (i + 1), bg='#eeeeee')
    #调用pack进行布局(默认的布局)
    lab.pack()  
#启动主窗口的消息循环
root.mainloop()
'''

#通过help(tkinter.Label.pack)命令来查看pack()方法支持的选项
'''
anchor: 当可用空间大于组件所需求的大小时，该选项决定组件被放置在容器的何处。该选项支持9个方位:
        N、E、S、W、NW、NE、SW、SE、CENTER
expand: 该bool值指定当父容器增大时是否拉伸组件
fill: 设置组件是否沿水平或垂直方向填充。支持选项：NONE、X、Y、BOTH 四个值
ipadx: 指定组件在x方向(水平)上的内部留白(padding)
ipadv: 指定组件在y方向(水平)上的内部留白(padding)
padx: 指定组件在x方向(水平)上与其他组件的间距
pady: 指定组件在y方向(水平)上与其他组件的间距
side: 设置组件的添加位置，可以设置为TOP、BOTTOM、LEFT 或 RIGHT四个值的其中之一
'''


#案例：当程序界面比较复杂时，需要使用多个容器(Frame)分开布局，然后再将Frame添加到窗口中
'''
from tkinter import *
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #创建第一个容器
        fm1 = Frame(self.master)
        #该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        #向fm1中添加三个按钮
        #设置按钮从顶部开始排列，且按钮只能在水平(X)方向上填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=YES)

        #创建第二个容器
        fm2 = Frame(self.master)
        #该容器放在左边排列，就会挨着fm1
        fm2.pack(side=LEFT, padx=10, expand=YES)
        #向fm2中添加三个按钮
        #设置按钮从右边开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)

        #创建第三个容器
        fm3 = Frame(self.master)
        #该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        #向fm3中添加三个按钮
        #设置按钮从底部开始排列，且按钮只能在垂直(Y)方向上填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)

root = Tk()  #主窗口
root.title("Pack布局")
display = App(root)
root.mainloop()
'''

#无论多复杂、古怪的界面，大多可分解为水平排列和垂直排列，再使用Pack布局通过多个容器(Frame)进行组合




#Grid布局管理器
'''Grid布局把组件空间分解成一个网格进行维护，即按照行、列的方式排列组件，组件位置由其所在的行号和列号决定;
行号相同而列号不同的几个组件会被依次 上下排列 ，列号相同而行号不同的几个组件会被依次 左右排列 '''

#使用Grid布局的过程就是为各个组件指定行号和列号的过程，不需要为每个网格都指定大小，Grid布局会自动为它们设置合适的大小

#程序调用组件的 grid() 方法就进行 Grid 布局，在调用grid()方法时可传入多个选项，该方法支持的ipadx、ipady、padx、pady与pack()[Pack布局管理器]方法的这些选项相同

#grid()方法额外增加了如下选项：
'''
column: 指定将组件放入哪列。第一列的索引为0
columnspan: 指定组件横跨多少列
row: 指定组件放入哪行。第一行的索引为0
rowspan: 指定组件横跨多少行
sticky: 类似于pack()方法的anchor选项,同样支持9个方向的表示值
'''

#示例：使用Grid布局来实现一个计算器界面
from tkinter import *
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #创建一个输入组件
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)  #指定字体为 Courier New
        #对该输入组件使用Pack布局的pack()方法，Grid布局也有pack()方法，放在容器顶部
        e.pack(side=TOP, pady=10)

        p = Frame(self.master)  #创建Frame容器
        p.pack(side=TOP)
        #定义字符串元组
        names = ("0", "1", "2", "3"
            , "4", "5", "6", "7", "8", "9"
            , "+", "-", "*", "/", ".", "=")
        #遍历字符串元组
        for i in range(len(names)):
            #创建Button,将Button放入p组件(容器)中
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)  #指定字体和字体大小，指定宽度为6
            b.grid(row=i // 4, column=i % 4)
root = Tk()
root.title("Grid布局")
App(root)
#启动主窗口的消息循环
root.mainloop()

