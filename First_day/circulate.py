
"""
用户身份验证
Version：0.1
Auth: ssp
"""

username = input('请输入用户名： ')
#password = input('请输入口令： ')
#getpass模块的getpass函数：输入口令时，终端中没有回显,即不显示密码
import getpass
password = getpass.getpass('请输入口令： ')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

"""
分段函数求值，if...elif...else... 结构的应用

        3x - 5 (x > 1)
f(x) =  x + 2 (-1 <= x <=1)
        5x + 3 (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x -5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
# %.2f 表示浮点数取2位小数点,类推--> %.3f就表示取小数点3位的浮点数
#和shell脚本的if...else循环不一样，else就是结束，后面不再有fi,再就是if和else、elif后面都带:号


#英制单位与公制单位的换算

value = float(input('请输入长度: '))  # 变量赋值用=
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':  #变量等于用 ==
    print('%f英寸 = %.2f厘米' % (value, value * 2.54))  # %f表示浮点数，% 表示引用value的计算表达式
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %.2f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')

#掷骰子决定做什么事情

from random import randint  #random模块的randint函数生成指定范围的随机数来模拟掷骰子

face = randint(1, 6) #生成1到6范围内的数字
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
else:
    result = '讲冷笑话'
print(result)


#输入三条边，计算能否构成三角形，并计划周长和面积
import math  #math模块

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b + c > a and c + a > b :
    #girth = (a + b + c)
    #print('周长：%f' % (girth))
    print('周长: %.2f' % (a + b + c))
    p = (a + b + c) / 2   ##海伦公式计算三角形面积
    area = math.sqrt(p * (p -a) * (p -b) * (p -c))  #使用math模块的sqrt函数来计算平方根
    print('面积：%.2f' % (area))  #单个%后的表达式引用最好加上()
else:
    print('不能构成三角形')


#个人所得税计算器
salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax)) #内置的abs()函数取绝对值来处理-0的问题

#for循环实现1~100求和
sum = 0  #定义初始值
for x in range(101):  #range类型，range可以用来产生一个不变的数值序列，range的用法同shell
#for x in range(2, 101, 2)  #1到100之间的偶数求和
    sum += x  # += 表示累加
print(sum)

#构造不知道具体循环次数的循环结构
#import random   #导入模块
#answer = random.randint(1, 100)  #模块加函数的使用

from random import randint    #从某个模块导入函数
answer = randint(1, 100)   #函数使用
counter = 0
while True:   #while循环，注意 ：号
    counter += 1
    number = int(input('请输入一个数字：' ))
    if number > answer:
        print('大了点!')
    elif number < answer :
        print('小了点!')
    else:
        print('猜对了!')
        break  #break关键字来提前终止循环，且只能终止它所在的那个循环，这里是终止while循环
print('你一共猜了%d次' % counter)  # %d 表示整数，类似 %f 的意义
if counter > 5:         #单结构if语句，注意 : 号
    print('你的智商不足啊！')
else:
    print('高智商啊!')

#利用循环结构的嵌套来打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j),end='\t')  #一个%d代表后面的一个变量;end='\t'表示换行
    print()  #打印一个空的，形成九九乘法表的层叠

#输入一个数判断是不是素数，素数就是质数
from math import sqrt

Number = int(input('请输入一个正整数: '))
End = int(sqrt(Number)) #开平方根，取整,就可判断是否有其他因子
is_prime = True
for x in range(2, End + 1):  
    if Number % x == 0:  #取余数，是否能被2整除
        is_prime = False
        break
if is_prime and Number != 1:
    print('%d是素数' % Number)
else:
    print('%d不是素数' % Number)

#计算最大公约数和最小公倍数
x = int(input('输入第一个正整数： '))
y = int(input('输入第二个正整数： '))
if x < y:
#if x > y:   #都可以
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:  #计算最大公约数；即同时能被x和y整除
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

#打印各种三角形：朝右的、朝左的、堆积的
row = int(input('请输入行数： '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')  # end='' 表示换行
    print()

for i in range(row):
    for j in range(row):
        if j < row -i -1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row -i -1):
        print(' ', end='')
    for _ in range(2 * i +1):
        print('*', end='')
    print()    

#打印出100到999之间的水仙花数
for num in range(100, 999):
    low = num % 10  #取余数就是最小位数字
    mid = num // 10 % 10  #先取除10的除数，再取除数除以10的余数，得中位数字
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
    
#百钱百鸡:假设公鸡x,母鸡y,鸡仔3x,先用数学的思维写出公式
#3i + 5a + (100-i-a)/3 = 100  ---> 8i + 14a = 200 --> 4i + 7a = 100 

for i in range(0, 100):  # i是公鸡数量
    for a in range(0, 101): # a是母鸡数量
        if 4*i + 7*a == 100 and 100 - i - a >=0:
            print('公鸡',a,'只, 母鸡',i,'只','小鸡',100-i-a,'只')


#找出范围类的完美数：完美数是除自身外其他所有因子的和正好等于这个数本身的数
import math

for num in range(1, 10000):   #定义数字范围
    sum = 0   #定时初始值
    for factor in range(1, int(math.sqrt(num)) + 1):  #定义因子
        if num % factor == 0:  #如果数字能被因子整除
            sum += factor   #则初始值重新赋值为：因子加sum
            if factor > 1 and num / factor != factor:  #如果因子大于1且数字除以因子不等于因子
                sum += num / factor  #则重新复制sum为数字除以因子的结果
    if sum == num:
        print(num)

#求范围内的素数，也就是质数；除了自己和1以外没有其他因子(因数)
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:  #能被因子整除
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')  #每次输出之间空一格

#掷骰子游戏
from random import randint

money = 1000
while money > 0:  #如果资产大于0
    print('你的总资产为：', money)
    needs_go_on = False  #不继续
    while True:
        debt = int(input('请下注： '))  #下注的筹码
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)  #第一次摇出的点数
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 1:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True  # 继续
    
    while needs_go_on:  #如果继续玩
        current = randint(1, 6) + randint(1, 6)  #当前摇出的点数
        print('玩家摇出了%d' % current)
        if current == 7:
            print('庄家胜!')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜!')
            money += debt
            needs_go_on = False
print('你破产了，游戏结束!')


#斐波那契数列：即从0开始，每个数都等于前面2个数之和
#输出斐波拉契数列的前20个数
a, b = 0, 1  #
"""  #方法1
while a < 3000:
    print(a)
    a, b = b, a+b
"""
for _ in range(20):
    (a, b) = (b, a + b) #每个数都等于前面2个数之和
    print(a, end=' ')  # 输出a和空格，循环输出






























