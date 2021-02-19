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
'''
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
'''


#Place布局管理器：绝对布局，要求程序显式指定每个组件的绝对位置或相对于其他组件的位置
#使用Place布局，调用相应组件的place()方法即可。
#place()方法的常用选项：
'''
x：指定组件的 X 坐标。x为0代表位于最左边,单位为像素(pixel)
y: 指定组件的 Y 坐标。y为0代表位于最右边,单位为像素(pixel)
relx: 指定组件的X坐标，以父容器总宽度为单位1，该值应该在0.0~1.0之间，其中0.0代表位于窗口最左边，1.0代表位于
        窗口最右边，0.5代表位于窗口中间
rely: 指定组件的Y坐标，以父容器总高度为单位1，该值应该在0.0~1.0之间，其中0.0代表位于窗口最上边，1.0代表位于
        窗口最下边，0.5代表位于窗口中间
width: 指定组件的高度，以 pixel 为单位
height: 指定组件的高度，以 pixel为单位
relwidth: 指定组件的宽度，以父容器总宽度为单位1，该值应该在0.1~1.0之间，其中1.0代表整个窗口宽度，0.5代表窗口的一半宽度
relheight: 指定组件的高度，以父容器总高度为单位1，该值应该在0.1~1.0之间，其中1.0代表整个窗口高度，0.5代表窗口的一半高度
bordermode: 该属性支持 "inside" 或 "outside" 属性值，用于指定当设置组件的宽度、高度时是否计算该组件的边框宽度
'''

#Tkinter容器的坐标系统的原点(0,0)在左上角，其中X轴向右延伸，Y轴向下延伸
#通过x指定的坐标值越大，该组件就越靠右，通过y指定的坐标值越大，该组件就越靠下

#示例：使用Place布局管理器，动态计算各Label的大小和位置，并通过place()方法设置各Label的大小和位置
'''
from random import randrange
from tkinter import *
import random
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #定义字符串元组
        books = ('疯狂Python讲义', '疯狂Swift讲义', '疯狂Kotlin讲义',\
            '疯狂Java讲义', '疯狂RUby讲义')
        for i in range(len(books)):
            #生成三个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            #将元组中的三个随机数格式化成十六进制数，转换成颜色格式；即随机生成颜色
            bg_color = "#%02x%02x%02x" % tuple(ct)
            #创建Label,设置背景色和前景色
            lb = Label(root, text = books[i], fg = 'White' if grayness < 125 else 'Black', bg = bg_color)
            #使用place()设置该Lable的大小和位置
            lb.place(x = 20, y = 36 + i*36, width=180, height=30)  #调用place()方法执行Place布局

root = Tk()
root.title("Place布局")
#设置窗口的大小和位置
#widthxheight+x_offset+y_offset
root.geometry("250x250+30+30")  #设置窗口的大小和位置，查看帮助：help(tkinter.Tk.geometry)
App(root)
root.mainloop()
'''


#事件处理：即点击按钮可影响用户的操作，点击按钮有响应
#简单的事件处理通过 command 选项来绑定，该选项绑定为一个函数或方法，当用户单击指定按钮时，通过该command选项绑定的函数或方法就会被触发

#示例：为按钮的command绑定事件处理方法
'''
from tkinter import *
import random

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.label = Label(self.master, width=30)
        self.label['font'] = ('Courier', 20)
        self.label['bg'] = 'white'
        self.label.pack()
        bn = Button(self.master, text='点击', command=self.change)  #command的使用
        bn.pack()
    def change(self):
        self.label['text'] = '欢迎学习Python'
        #生成三个随机数
        ct = [random.randrange(256) for x in range(3)]
        grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
        #将元组中的三个随机数格式化成十六进制数，转换成颜色格式
        bg_color = "#%02x%02x%02x" % tuple(ct)
        self.label['bg'] = bg_color
        self.label['fg'] = 'black' if grayness > 125 else 'white'
root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()
'''


#事件绑定：除了按钮单击的事件处理，更灵活的事件绑定方式，如：鼠标移动、按键事件等
#所有Widget组件都提供了一个bind()方法，该方法可以为"任意"事件绑定事件处理方法
#show()方法是显示
#示例：为按钮的单击、双击事件绑定事件处理方法

'''
from tkinter import *
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.show = Label(self.master, width=30, bg='white', font=('times', 20))
        self.show.pack()
        bn = Button(self.master, text='单击我或双击我')
        bn.pack(fill=BOTH, expand=YES)
        #为左键单击事件绑定处理方法
        bn.bind('<Button-1>', self.one) #<Button-1> 代表鼠标左键单击事件
        #为左键双击事件绑定处理方法
        bn.bind('<Double-1>', self.double) #<Double-1> 代表鼠标左键双击事件
    def one(self, event):
        self.show['text'] = "左键单击：%s" % event.widget['text']
    def double(self, event):
        print("左键双击，退出程序:", event.widget['text'])
        import sys; sys.exit()

root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()
'''


#代表tkinter事件的字符串大致遵循如下格式：
'''<modifier-type-detail>
其中type 是事件字符串的关键部分，用于描述事件的种类，比如鼠标、键盘事件等
modifier 则代表事件的修饰部分，比如单击、双击等
detail 用于指定事件的详情，比如指定鼠标左键、右键、滚轮等
'''
#tkinter支持的鼠标、键盘事件按：左、中、右、上、下 来实现
'''如： 鼠标的单击事件：<Button-1> --> <Button-5>
        按住鼠标的移动事件：<B1-Motion> --> <B3-Motion>
        鼠标按键的释放事件：<ButtonRelease-1> --> <ButtonRelease-3>
        用户双击某个鼠标键的事件：<Double-1> --> <Double-5>
        鼠标进入组件的事件：<Enter>   不是按下回车键事件，按下回车键的事件是 <Return>
        鼠标移出事件：<Leave>
        组件及其包含的子组件获得焦点：<FocusIn>
        组件及其包含的子组件失去焦点：<FocusOut>
        可以为键盘上所有非数字和字母的按键绑定事件处理方法：Shift_L、Ctrl_L、Alt_L、Prior(Page Up键)、Next(Page Down键)等
        <Key>  键盘上任意键的单击事件，程序可通过event获取用户单击了哪个键
        a  键盘上指定键被单击的事件。比如 a 代表a键被单击，b代表b键被单击....
        <Shift-Up> 在Shift键被按下时按Up键。还可组合Alt和Control;类似的还有：<Shift-Left>、<Shift-Down>等
        <Configure> 组件大小、位置改变的事件。组件改变之后的大小、位置可通过 event 的 width、height、x、y获取
'''

#示例：为鼠标移动事件绑定事件处理方法
'''
from tkinter import *

class App:
    def __init__(self, master):  #定义主容器
        self.master = master
        self.initWidgets()

    def initWidgets(self):  #初始化容器
        lb = Label(self.master, width=40, height=3)
        lb.config(bg='lightgreen', font=('Times', 20))
        #为鼠标移动事件绑定事件处理方法
        lb.bind('<Motion>', self.motion)
        #为按住左键时的鼠标移动事件绑定事件处理方法
        lb.bind('<B1-Motion>', self.press_motion)
        lb.pack()
        self.show = Label(self.master, width=38, height=1)
        self.show.config(bg='white', font=('Courier New', 20))
        self.show.pack()

    def motion(self, event):  #定义motion方法
        self.show['text'] = "鼠标移动到： (%s %s)" % (event.x, event.y)
        return

    def press_motion(self, event):  #定义press_motion方法
        self.show['text'] = "按住鼠标的位置为：(%s %s)" % (event.x, event.y)
        return

root = Tk()
root.title("鼠标事件")
App(root)
root.mainloop()
'''


#改进型计算器，可以实现简单的计算功能

'''
from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None   #定义表达式初始值

    def initWidgets(self):
        #创建一个输入组件
        self.show = Label(relief=SUNKEN, font=('Courier New', 24), width=25, bg='white', anchor=E)
        #对该输入组件使用Pack()布局，放在容器顶部
        self.show.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        names = ("0", "1", "2", "3"
            , "4", "5", "6", "7", "8", "9"
            , "+", "-", "*", "/", ".", "=")
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
            #为鼠标左键的单击事件绑定事件处理方法
            b.bind('<Button-1>', self.click)
            #为鼠标左键的双击事件绑定事件处理方法
            if b['text'] == '=': 
                b.bind('<Double-1>', self.clean)

    def click(self, event):  #创建click方法
        #如果用户单击的是数字键或点号
        if(event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8'\
            , '9', '.')):
            self.show['text'] = self.show['text'] + event.widget['text']
        #如果用户单击了运算符
        elif(event.widget['text'] in ('+', '-', '*', '/')):
            #如果当前表达式为None，则直接用show组件的内容和运算符进行连接
            if self.expr is None:
                self.expr = self.show['text'] + event.widget['text']
            #如果当前表达式不为None，则用表达式、show组件的内容和运算符进行连接
            else:
                self.expr = self.expr + self.show['text'] + event.widget['text']
            self.show['text'] = ''
        elif(event.widget['text'] == '=' and self.expr is not None):
            self.expr = self.expr + self.show['text']
            print(self.expr)
            #使用eval函数计算表达式的值
            self.show['text'] = str(eval(self.expr))
            self.expr = None

    #当双击 "=" 按钮时，程序清空计算结果，将表达式设为None
    def clean(self, event):   #创建clean方法
        self.expr = None      #清空表达式
        self.show['text'] = ''

root = Tk()
root.title("计算器")
App(root)
root.mainloop()
'''



#Tkinter常用组件
#ttk组件：作为一个模块放在tkinter包下，相比GUI组件更美化，功能更强大；导入即可使用

#示例：使用ttk组件
'''
from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
#下面被注释的是使用Listbox，即直接使用tkinter组件的代码；没注释的是使用ttk组件的代码
    def initWidgets(self):

        #ttk使用Combobox取代了Listbox
        cb = ttk.Combobox(self.master, font=24)
        #为Combobox设置列表项
        cb['values'] = ('Python', 'Swift', 'Kotlin')

        #cb = Listbox(self.master, font=24)  #列表项
        #为Listbox设置列表项
        #for s in ('Python', 'Swift', 'Kotlin'):
        #    cb.insert(END, s)

        cb.pack(side=LEFT, fill=X, expand=YES)

        f = ttk.Frame(self.master)
        #f = Frame(self.master)

        f.pack(side=RIGHT, fill=BOTH, expand=YES)

        lab = ttk.Label(self.master, text='我的标签', font=24)
        #lab = Label(self.master, text='我的标签', font=24)

        lab.pack(side=TOP, fill=BOTH, expand=YES)

        bn = ttk.Button(self.master, text='我的按钮')
        #bn = Button(self.master, text='我的按钮')
        bn.pack()

root = Tk()
root.title('简单事件处理')
App(root)
root.mainloop()
'''
#ttk组件版本风格更接近现代，更接近Windows7以上版本的风格，更美观，就是ttk组件的优势



#Variable类: 将很多GUI组件与变量进行双向绑定，执行这种双向绑定后编程非常方便
'''
>如果程序改变变量的值，GUI组件的显示内容或值会随之改变
>当GUI组件的内容发生改变时(比如用户输入)，变量的值也会随之改变
'''
#为了让Tkinter组件与变量进行双向绑定，只要为这些组件指定variable(通常绑定组件的value)、textvariable(通常绑定组件显示的文本)等属性即可
#Tkinter不允许将组件和普通变量进行绑定，只能和tkinter包下Variable类的子类进行绑定

#Variable类的子类包含如下几个子类：
'''
StringVar(): 用于包装str值的变量
IntVar(): 用于包装整型值的变量
DoubleVar(): 用于包装浮点值的变量
BooleanVar(): 用于包装bool值的变量
'''

#对于Variable变量：要设置其保存的变量值，则使用它的set()方法；要得到其保存的变量值，则使用它的get()方法

#示例：将Entry组件与StringVar 进行双向绑定,达到既可通过StringVar改变Entry输入框显示的内容，也可通过该StringVar获取Entry输入框中的内容

'''
from tkinter import *
#导入ttk
from tkinter import ttk
from tkinter import font

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.st = StringVar()   #StringVar()用于包装str值的变量
        #创建Label组件Entry(即输入框),将其textvariable绑定到self.st变量
        ttk.Entry(self.master, textvariable=self.st, width=24, font=('StSong', 20, 'bold'),
        foreground='red').pack(fill=BOTH, expand=YES)
        #创建Frame作为容器
        f = Frame(self.master)
        f.pack()
        #创建两个按钮，将其放入Frame中
        ttk.Button(f, text='改变', command=self.change).pack(side=LEFT)
        ttk,Button(f, text='获取', command=self.get).pack(side=LEFT)

    def change(self):  
        books = ('疯狂Python讲义', '疯狂Kotlin讲义', '疯狂Swift讲义')
        import random
        #改变self.st变量的值，与之绑定的Entry的内容随之改变
        self.st.set(books[random.randint(0, 2)])  #variable的set()方法设置其保存的变量值

    def get(self):   #定义variable的get()方法
        from tkinter import messagebox
        #获取self.st变量的值，实际上就是获取与之绑定的Entry中的内容
        #并使用消息框显示self.st变量的值
        messagebox.showinfo(title='输入内容', message=self.st.get())

root = Tk()
root.title("Variable测试")
App(root)
root.mainloop()
'''



#使用compound选项：当需要为按钮(Button)或Label等组件同时指定text和image两个选项(默认image会覆盖text)，且需要组件能同时显示文本和图片时，可通过compound选项进行控制
#compound选项支持如下属性：
'''
None: 图片覆盖文字
LEFT常量(值为'left'字符串)：图片在左，文本在右
RIGHT常量(值为'right'字符串)：图片在右，文本在左
TOP常量(值为'right'字符串): 图片在上，文本在下
BOTTOM常量(值为'bottom'字符串)：图片在底，文本在上
CENTER常量(值为'center'字符串)： 文本在图片上方
'''

#示例：使用多个单选钮来控制Label的compound选项

'''
from tkinter import *
#导入ttk
from tkinter import ttk
from tkinter import font

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #创建一个位图
        bm = PhotoImage(file = 'D:\learning_python\\twelfth_day\serial.png')
        #创建一个Entry，同时指定text和image
        self.label = ttk.Label(self.master, text='疯狂体\n系图书',\
            image=bm, font=('Stsong', 20, 'bold'), foreground='red')
        self.label.bm = bm
        #设置Label默认的compound为None
        self.label.pack()
        #创建Frame容器，用于装多个Radiobutton
        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", "CENTER")
        #定义一个StringVar变量，用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        #使用循环创建多个Radionbutton组件
        for val in compounds:
            rb = Radiobutton(f,
                text = val,
                padx = 20,
                variable = self.var,
                command = self.change_compound,
                value=val).pack(side=LEFT, anchor=CENTER)
    #实现change_compound方法，用于动态改变Label的compound选项
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()

root = Tk()
root.title("compound测试")
App(root)
root.mainloop()
'''


#Entry 和 Text 组件







