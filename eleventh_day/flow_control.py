#流程控制

"""
age = input("输入年龄： ")
age1 = int(age)
if age1 >= 23:
    print('年龄大于18')
elif 18 <= age1 <= 22:
    print("年龄在18到22之间")
else:
    print("年龄不够")


a = 4
if a > 4:
    a -= 1
    print("a =4")
else:
    print("a不大于4")
print(type(a))


a = '' #或 [] {} "" ''
if a:
    print("a不是空字符串")
else:
    print("a是空字符串")


#断言：关键字是 assert
age = input("请输入一个整数： ")
s_age = int(age)
assert 18 < s_age < 40  #断言的条件
print("年龄在18到20岁之间")  #否则不在这个断言的条件内就会报错：AssertionError


#while循环
count_i = 0  #初始化语句或变量
while count_i < 10:  #循环条件
    print("count: ", count_i)  #循环体
    count_i += 1   #迭代语句
print("循环结束")  #不符合循环条件了，结束循环

#使用while循环变量列表或元组中的元素
list1 = ['a', 'b', 'c', 'd', 'e', 1, 2, 3]
i = 0  #初始化语句或变量
while i < len(list1):  #循环条件
    print(list1[i])  #循环体
    i += 1   #迭代语句


#用while循环对一个整数列表的元素进行分类： 分3类
int_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
#定义三个空列表，用于存放分类的整数;即while循环前的初始化
a = []  
b = []
c = []

while len(int_list) > 0:
    last_num = int_list.pop()  #每次取列表的最后一个元素
    if last_num % 3 == 0:   #第一类：能整除3的放在一个列表中
        a.append(last_num)  
    elif last_num % 3 == 1: #第二类：能除3余1的放在一个列表中
        b.append(last_num)
    else:
        c.append(last_num)  #第三类：其它的，即不满足前面2个条件的
print(a)
print(b)
print(c)    


#for-in循环：
Jc = input("请输入想计算的阶乘： ")  
mx = int(Jc)  #字符串整数化
result = 1 #初始化
for i in range(1, mx + 1):  #遍历范围来计算阶乘，如3的阶乘：1x2x3
    result *= i
print(result)


#for-in循环遍历列表和元组
list1 = [1, 2, 'aa']
for i in list1:
    print("元素是：", i)

list2 = [1, 2, 'aa', 'dfdsf', 'crazy', 4, 5.2]
my_sum = 0   #初始化
my_count = 0  #初始化
for i in list2:
    if isinstance(i, int) or isinstance(i, float):  #isinstance()方法，判断一个元素或变量是否是某个类型
        print(i)
        my_sum += i   #累加
        my_count += 1  #个数每次加1
print("总和: ", my_sum)
print(my_count)
print("平均数：", my_sum / my_count)  #总和除以元素的个数就是平均数


#for-in循环通过索引遍历列表的元素
list2 = [1, 2, 'aa', 'dfdsf', 'crazy', 4, 5.2]

for i in range(0, len(list2)):
        print('第%d个元素是%s：' % (i, list2[i]))



#for-in循环遍历字典
dict1 = {'ni':2, 'hao':3, 'ma':4}
for key, value in dict1.items():  #定义2个变量，因为字典的items方法返回的是key-value对列表
    print('key:', key)
    print('value:', value)
print('------------')  #打印分隔符
for key in dict1.keys():
    print('key:', key)
    print('value:', dict1[key])
print('------------')
for value in dict1.values():
    print('value:', value)


#实现一个程序：统计一个列表中各元素出现的次数
list2 = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
dict1 = {} #初始化，定义一个空字典
#dict1 = dict()  #不为dict函数传入任何参数，也是定义一个空字典
for num in list2:  #num是列表中的元素
    if num in dict1:  #num也是字典中的key
        dict1[num] += 1
    else:
        dict1[num] = 1  #出现的次数就是字典中key对应的value


for num, count in dict1.items():
    print('%s出现的次数是：%d' % (num, count))
print(dict1)  #打印出形成的字典



#在while循环中使用else
count1 = 0
while count1 < 5:
    print('count1 小于5', count1)
    count1 += 1
#else:   #使用else块，作用不大，主要是使得python代码更优雅
#    print('count1 大于或等于5', count1)
print('count1 大于或等于5', count1)

#在for-in循环中使用else
list1 = [1, 2, 'aa']
for i in list1:
    print("元素是：", i)
#else:  #访问循环计数器i的值，用else块依然是最后一个元素
#    print('else块： ', i)


#嵌套循环
for i in range(0, 5):  #外层循环
    j = 0   #内层循环的初始化
    while j < 3:  #内层循环
        j += 1
        print("i的值为：%d, j的值为: %d" % (i, j))
        

#for表达式：即列表推导式
a = range(0, 5)  #利用区间生成列表
b = [x * x for x in a if x % 2 == 0]  # a必须是可迭代的对象,即元组或列表、区间等;可对x加循环条件
print(b)


#for表达式：即生成器推导式
a = range(0, 5)  #利用区间生成列表
b = (x * x for x in a if x % 2 == 0)
print(type(b))  #结果是一个生成式,类型：generator
print(b)

#生成式也可以使用for-in循环遍历
for i in b:
    print(i, end='\t')


#for表达式使用多个循环，就像for-in的嵌套循环
list1 = [(x, y) for x in range(0, 5) for y in range(4)]  #迭代的次数则是 x * y
print(list1)  #生成的表达式的元素个数是 x * y
#或更多
list2 = [(x, y, z) for x in range(0, 5) for y in range(4) for z in range(3)]
print(list2)  #生成的表达式的元素个数是 x * y * z

"""
"""
#实例：将两个列表中可整除的元素配对在一起
list_a = [30, 12, 15, 66, 34]
list_b = [3, 5, 7, 11]
b = [(x, y) for x in list_a for y in list_b if x % y == 0]
print(b)
"""

"""
#zip()函数实现并行遍历多个列表或元组或区间
a = ['a', 'b', 'c', 'd']
b = [1, 2 ,3]
c = [x for x in zip(a, b)]
print(c)  #zip函数可把2个以上的列表压缩成一个可迭代zip对象,以最短的列表为准生成新的列表;该列表的元素是原列表元素组成的元组
print(type(c))


#reversed函数实现列表或元组或区间的反向遍历
a = range(10)  #或列表或元组，甚至字符串(字符串也是序列)
b = 'dfdfdsa'
print([x  for x in reversed(a)])  #反向遍历，并不会改变原来的列表或元组或区间
print(a)
print([y for y in reversed(b)])


#sorted函数：接收一个可迭代对象，返回一个对元素排序的列表;不支持列表中的元素是数字和字符的混合
a = ['dd', 'ss', 'aa', 'vv']  #列表中的元素只能是单一类型的
print(sorted(a))
b = [1, 2, 3, 2.3]
print(sorted(b))
print(sorted(b, reverse=True))  #sorted支持参数reverse,默认是False，如果是True，则表示反向排序
c = ['aa', 'c', 'ddd', 'dfdsfds', 'aasd']
print(sorted(c, key=len))  #sorted支持参数key，该参数指定一个函数来生成排序的关键指，如 len ，按元素的长度排序


#break关键字结束循环
for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:  #结束循环的条件
        break  #结束循环，else块也不执行了
    else:
        print('else块')



#使用break跳出内层循环和外层循环：使用2次break
exit_list = False
#外层循环
for i in range(0, 10):
    for j in range(0,5):
        print("i的值为：%d, j的值为：%d" % (i, j))
        if j == 2:
            exit_list = True  #先定义bool类型的变量来标志是否跳出外循环；这里即是当j == 2时，程序将 exit_list设定为True
            break #跳出内层循环
    if exit_list:  #如果exit_list为True,就跳出外层循环
    #if i == 3:
        break


#continue： 忽略当次(条件满足时)循环的语句，即在continue关键字后且还在循环中的语句
for i in range(0, 3):
    print("i的值是：%d" % i)
    if i == 1:  #当 i == 1时，continue关键字后的语句"continue后的输出语句" 不输出了
        continue
    print("continue后的输出语句")  #循环的剩下语句



#return： 结束一个函数(方法)：因循环大多数都在函数中，故结束了函数，相当于就结束了循环
def test():
    #外层循环
    for i in range(10):
        for j in range(10):
            print("i的值是：%d, j的值是： %d" % (i, j))
            if j == 1:
                return
            print("return后的输出语句")

test()

"""
"""
#绕圈圈：
#python创建二维列表
SIZE = 7
array = [[0] * SIZE]
for i in range(SIZE - 1):
    array += [[0] * SIZE]
orient = 0
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    if j + k == SIZE - 1:
        if j > k:
            orient = 1
        else:
            orient = 2
    elif (k == j) and (k >= SIZE /2):
        orient = 3
    elif (j == k -1) and (k <= SIZE /2):
        orient = 0
    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        k -= 1
    elif orient == 3:
        j -= 1
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d' % array[i][j], end = " ")
    print("")

"""

"""
#控制台超时购物系统
repository = dict()
shop_list = []

def init_repository():
    goods1 = ('10001', 'Python讲义', 88.0)
    goods2 = ('10002', 'Java讲义', 69.0)
    goods3 = ('10003', 'Ruby讲义', 59.0)
    goods4 = ('10004', 'Swift讲义', 109.0)
    goods5 = ('10005', 'Android讲义', 108.0)
    goods6 = ('10006', 'ios讲义', 77.0)
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6

def show_goods():
    print("欢迎光临!")
    print("商品清单如下：")
    print("%13s%40s%10s" % ("条码", "商品名称", "单价"))
    for goods in repository.values():
        print("%15s%40s%12s" % goods)

def show_list():
    print("=" * 100)
    if not shop_list:
        print("还未购买商品")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        sum = 0
        for i, item in enumerate(shop_list):  
            #enumerate是列举、枚举的意思
            #enumerate参数为可遍历/可迭代的对象(如列表、字符串)
            #enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用
            id = i + 1
            code = item[0]
            name = repository[code][1]
            price = repository[code][2]
            number = item[1]
            amount = price * number
            sum = sum + amount
            line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
            (id, code, name, price, number, amount)
            print( line )
        print("-" * 100)
        print("                         总计：", sum)
    print("=" * 100)

def add():
    code = input("请输入商品的条码：\n")
    if code not in repository:
        print("条码错误，请重新输入：")
        return
    #goods = repository[code]
    number = input("请输入购买数量：\n")
    shop_list.append([code, int(number)])


def edit():
    id = input("请输入要修改的购物明细项的ID：\n")
    index = int(id) - 1
    item = shop_list[index]
    number = input("请输入新的购买数量: \n")
    item[1] = int(number)

def delete():
    id = input("请输入要删除的购物明细项的ID： ")
    index = int(id) - 1
    del shop_list[index]

def payment():
    show_list()
    print('\n' * 3)
    print("欢迎下次光临")
    import os
    os._exit(0)

cmd_dict = {'a':add, 'e':edit, 'd':delete, 'p':payment, 's':show_goods}

def show_command():
    cmd = input("请输入操作指令： \n" + 
        "   添加(a) 修改(e) 删除(d) 结算(p) 超市商品(s)\n")
    if  cmd not in cmd_dict:
        print("不要玩，好不好!")
    else:
        cmd_dict[cmd]()

init_repository()
show_goods()
while True:
    show_list
    show_command()


"""

a = enumerate(range(10))
print(a)