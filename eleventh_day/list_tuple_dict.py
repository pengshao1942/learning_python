
'''
a = int(1)
print(type(a))

b = str(2)
print(type(b))  

c = float(1.1)
print(type(c))

d = 1 + 2j
print("d的类型为：", type(d))

#数字转换成字符串的函数：str() 或 repr()
print(repr(b))
'''

"""
a = input("请输入一个数字： ")
print(type(a))
print(a)
b = r'G:\c\fdf'
print(b)
"""

'''
a = int(input("请输入第一个数： "))
b = int(input("请输入第二个数： "))
print("a + b 的和是：", a + b)
print("a 除 b的结果是： ", a / b)
'''

'''
num = (2 + 3 +4) / \
    5
print(num)

b = bytes()
a = bytes('你好', encoding='utf-8')
c = "世界".encode('utf-8')
print(type(b))
print(a)
print(c)

st = c.decode('utf-8')
print(st)
'''

'''
a = int(input("请输入数字a: "))
b = int(input("请输入数字b: "))
print("a + b的和为：%d" % (a + b))
print("a - b的差为：%d" % (a - b))
print("a * b的积为：%d" % (a * b))
'''
'''
str1 = input("输入字符串： ")
str_sub = input("输入子串: ")
print(str1.count(str_sub))
'''

"""会全部替换，不完整
str1 = input("请输入一个字符串： ")
change = input("输入要替换的字符串的索引位置：")
a = str1[int(change)]
change_str = input("请输入要替换后的子串： ")
print(str1.replace(a, change_str))
"""
"""
order_endings = ('st', 'nd', 'rd')\
    + ('th',) * 17 + ('st', 'nd', 'rd')\
        + ('th',) * 7 + ('st',)

print(order_endings)
day = input("输入日期(1-31): ")
day_int = int(day)
print(day + order_endings[day_int -1])


a = ('crazyit', 20, -1.2)
print(20 in a)
print('ra' not in a)


a = (1, 2, 3, 4, 5, 6)
b = ('fd', 'dd', 'dfd', 'CC')
print(max(a), len(a), len(b), max(b), min(a), min(b))


a = 1, 2, 3
print(a)
print(type(a))
print(a[1])

tuple1 = ('fd', 22, 'fc', '22')
e, b, c, d = tuple1
print(e, b, c, d)
print(type(d))


x, y, z = 10, 20, 30  #运用序列的封包和解包机制将多个值赋值给多个变量
print(x, y, z)

x, y, z = z, y, x
print(x, y, z)


*x, y, z = [1, 2, 'fdf', 'sdf']  #去2个元素，剩下的元素已列表方式保存
#x, *y, z = (1, 2, 'fdf', 'sdf')
#x, y, *z = (1, 2, 'fdf', 'sdf')
#x, y, *z = ()
print(x, y, z)
print(type(x))


a = ('fd', 'wo', 'fdd', 22)
b = list(a)  #元组转换为列表，list() 函数
print(b)
c = range(1, 8, 2)
print(c)
print(list(c))


a = [1, 2, 3]
print(type(tuple(a)))  #列表转换为元组 tuple() 函数
b = range(1, 5)
print(type(b))
print(tuple(b))
c = tuple(range(4, 20, 3))
print(c)

a = [1, 2, 3]  
#a.append(1)  #append增加一个元素，append方法是在最后增加
#a.append([1, 2, 4]) #append增加列表，会把增加的列表整体当成一个元素，形成嵌套列表了，元组一样，形成嵌套元组
a.append(('a', 1)) #不用定义了，直接使用append方法即可
print(a)


a = [1, 2, 3]
#a.extend(('1'))   #列表的extend方法增加整数时，用''引起来
a.extend([1, 2, 4])  #extend方法增加列表或元组，会把增加的列表和元素中的元素拆分开来增加到列表中
a.extend(('a', 1))  #不用定义了，直接使用extend方法即可
a.extend(range(3, 6))  #追加区间中的所有元素
print(a)


a = [1, 2 ,3]
a.insert(1, 4)  #insert方法，在列表中间指定位置(索引)前插入元素
a.insert(2, ['f', 'g']) #插入列表，列表被当成一个元素
a.insert(1, ('aa', 'bb')) #插入元组，元组被当成一个元素
print(a)


a = ['aa', 'bb', 'cc', 1, 2, 4 , 6 , 6]
#del a[1]  #del语句删除列表中指定位置(索引)的元素
#del a[1: 3]
#del a[2: -2]
del a[1: 6: 2]
print(a)
print(a[1]) #删除后列表元素索引发生变化

x = 'fsdfd'
del x   #del语句删除普通变量
print(x)  #删除后的变量再打印会引发NameError错误，除非再定义


a = [1, 2, 3, 2, 'dfd', 'ccc', 'ss', '**']
#a.remove(2)  #remove方法直接删除元素，删除了第一个2这个元素
a.remove('s')  #remove方法找不到要删除的元素，会报错ValueError，提示要删除的元素不在列表中
print(a)


a = [1, 2, 3, 2, 'dfd']
a.clear()  #clear方法清空列表中的元素
print(a)  #清空后的列表是空的，打印[]
#b = []  #定义空列表
#c = ()  #定义空元组
#d1 = [  ]  #加多少空格都一样，会自动忽略
#c1 = (   )  #加多少空格都一样，会自动忽略


a = [1, 2, 'sd', 'fd', 'fdf', 'ss']
#a[1] = 'nihao'
#a[0: 2] = ['i', 'a', 'b'] #并不要求赋值的元素个数与原来的个数相等
#a[0: 3: 2] = 'ss'
#a[1: 1] = ['x', 'y']  #对空的切片赋值，就表示插入元素
#a[1: 2] = [] #对切片赋值为空，就表示删除这段切片内(列表)的元素
#a[1: 3] = 'fsdfds' #对切片赋值为字符串时，会自动把字符串拆分成单个字符，即序列，每个字符都是一个元素
#a[1: 3] = 'a'  #对切片赋值单个值，会删除和赋值
a[1: 6: 2] = ['x', 'z', 'a']  #引入切片的步长参数，则需要赋值的列表元素个数和切片内的含的元素个数相同，否则会报错
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#a.pop(1)  #取出列表中指定索引位置的元素;默认取出最后一个元素；取出后列表发生变化；可使用切片
a.pop(-1)
print(a)
b = 'fdsfsd'
print(type(b))
print(b.index('d', 1, 4))


stack = []
stack.append('fkit')  #append()方法代替其它语言的入栈函数push()
stack.append('crazyiy')
stack.append('fdfds')
print(stack)
print(stack.pop()) #第一次执行出栈操作，最后入栈的元素先出，即FILO(First In Last Out)
print(stack)
print(stack.pop())  #再次出栈，一样FILO
print(stack)

list1 = ['a', 2, 't', 'y']
#list1.reverse()  #reverse方法会将列表中的元素倒序排列，即反转
list2 = ['a', '2', 'g']
list2.sort()  #
print(list1)
print(list2)


lengv = ['Python', 'Java', 'Php', 'Perl', 'Ruby', 'Go', 'Javascript', 'shell']
#lengv.sort(key=len)  #指定sort方法的key参数，key为len函数，即长度，按字符长度排序;默认从小到大
lengv.sort(key=len, reverse=True)  #sort的reverse参数,默认是False，即不反转排序，按从小到大排序，指定为True后，就从大到小排序
print(lengv)


dict1 = {'yu':22, 'shu':23, 'she':26}
print(dict1)
print(type(dict1))
empty_dict = {}  #创建空字典,方法1
print(empty_dict)
dict2 = {(1, 2):'list1', (2, 3):'list2'}  #因为字典中的key是不可变类型的，故只能用元组作为字典的key，不能用列表作为自定的key
print(dict2)


table = [('语文',98), ('数学', 108), ('英语',128)]
table1 = (['语文',98], ('数学', 108), ('英语',128))
dict1 = dict(table1)  #用dict函数创建字典，每个元组或列表组成一组key:value,这些列表或元组只能包含2个元素
print(dict1)
dict2 = dict()   #创建空字典，方法2，用dict函数
print(dict2)
dict3 = dict(语文=98, 数学=102)  #使用关键字参数来创建字典时不需要加引号
print(dict3)


sort = {'语文':98}
print(sort['语文'])  #获取字典中的value，使用对应的key
sort['物理'] =  88  #为字典增加key-value对，为不存在的key赋值即可
print(sort)  #增加(赋值)后字典会变化
del sort['语文']   #删除字典中的key，用del语句(不是方法,直接使用),指定key,就会删除对应的value
print(sort)
sort['物理'] - 99
print(sort)
print('物理' in sort)
print('英语' in sort)
print('英语' not in sort)
#sort.clear()   #字典的清空，清空后字典就变为空字典了
#print(sort['化学'])  #用方括号[]访问字典中不存在的key，会引发KeyError错误
print(sort.get('数学')) #用get方法访问字典中不存在的key时不会引发KeyError错误
sort.update({'生物':66}) #update方法，为字典增加或替换key-value对,()里面必须是key-value对,可有多对key-value对
sort.update({'生物':65}) #update方法，更新字典中已存在的key的value
print(sort)
"""
"""
cars = {'本田':'CRV', '丰田':'X-RV', '别克':'昂科威', '大众':'途观'}
ims = cars.items()  #字典的items方法获取字典中所有的key-value对
print(ims)
print(type(ims))  #返回一个dict_items 对象
print(list(ims))  #将dict_items 对象转换成列表
print(list(ims)[1])  #返回索引为1的key-value对

keys = cars.keys() #字典的keys方法获取字典中所有的key
print(keys)  
print(type(keys)) #返回一个 dict_keys 对象
print(list(keys))  #将dict_keys对象转换为列表
print(list(keys)[2])  #访问索引为2的key

vals = cars.values() #字典的items方法获取字典中所有的value
print(vals)
print(type(vals))  #返回一个dict_values 对象
print(list(vals))  #将dict_values对象转换为列表
print(list(vals)[1: 3]) #访问切片为1到3的索引对应的value
#cars.pop('别克')  #pop方法用于取出key对应value并删除该 key-value 对
print(cars.popitem()) #随机弹出字典中的一个key-value对，这里的随机其实是假的，实际是总是弹出最后一个key-value对
k, v = cars.popitem()  #popitem方法实际弹出的是一个元组；可通过序列解包的方式赋值给2个变量
print(k, v)
print(cars)


cars = {'本田':'CRV', '丰田':'X-RV', '别克':'昂科威', '大众':'途观'}
print(cars.setdefault('保时捷', '卡宴'))  #setdefault方法，key不存在则先给这个key一个value，再返回这个key的value
print(cars.setdefault('大众'))  #setdefault方法，key存在则直接返回value
print(cars.setdefault('大众', '途观'))  #同上，default的value存在时可不赋予
print(cars)



a_dict = dict.fromkeys(['a', 'b'])  #formkeys方法一般不使用字典对象调用；而是使用dict类直接调用；使用列表元素作为key创建
print(a_dict)  #fromkeys使用给定的对个key创建字典，如果不传入参数，则这些key默认的value都是None
b_dict = dict.fromkeys((13, 17))  #formkeys方法使用元组元素作为key创建,不设置value，使用默认value未None
print(b_dict)
c_dict = dict.fromkeys(('sd', 'fd'), 'good')  #fromkeys方法使用元组创建字典，设置默认的value为good
print(c_dict)
e_dict = dict.fromkeys(['a', 'b'], 'bad')  #fromkeys方法使用列表创建，设置默认的value为bad
print(e_dict)
"""


#当字符串模板中包含大量的变量需要格式化输出时：用字典
#在字符串模板中使用key：重点，使用字典格式化字符串
"""
temp = '书名是: %(name)s, 价格是: %(price)010.2f, 出版社是: %(publish)s' #字符串模板，key-valeu对应，key已经定义好，value就是对应字典里的key对应的value值
book = {'name':'Python手册', 'price':89.9, 'publish':'电子出版社'}  #定义自定
#使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'Python手册', 'price':79.9, 'publish':'电子出版社'}  
print(temp % book)
"""

"""
a = ('22', 'ss', '33')
print(a * 3)
print(a + ('dfd', 'fdf'))


list1 = [1, 2, 3, 'fd', 'fdf']
list2 = list1.copy()
print(list2)
print(list1)
"""


