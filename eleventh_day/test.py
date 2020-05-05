"""
list(range(0, 10))
print(list)
"""
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
"""
"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
"""
"""
while True:
    pass

def initlog(*args):
    pass
"""

"""
def fib(n):
    """  """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f = fib(100)
print(f)
"""
"""
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'none'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
"""
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
"""

"""
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
"""
"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot would 't'", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(voltage=5.0, action='dead') 
"""
"""
def make_incrementor(n):
    return lambda x: x + n
"""
"""
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
"""

'''
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
'''

"""
#列表
a = [1, 2, 5, 3, 1]
#a.append(3)  #结尾追加
#a[len(a):] = [3]  #等同于 a.append(3)
#   print(a)
L = [4, 5, 6]
#a.extend(L)
#a[len(a):] = L

#a.insert(1, 5)  #在索引1前插入元素5;print(a.insert(1, 5))返回None
#a.insert(len(a), 6) #在列表长度后插入元素6，相当于 a.append(6)
#a.remove(1)  #删除一个存在于列表中的第一个匹配元素，不存在则报错;print(a.remove(1))返回None
#a.pop(0)  #删除列表指定位置(索引)处的元素
#print(a.pop())  #a.pop() 返回列表的最后一个元素
#a.clear() #从列表中删除所有元素，返回 []
#del a[:]  #等同于 a.clear()
#print(a.index(2)) #返回列表中第一 值未2 的元素的索引值
#print(a.count(1))  #返回元素1在列表中出现的次数
#a.sort() #对列表中的元素排序,print(a)返回排序后的列表;print(a.sort())返回None
#a.reverse() #倒叙排列列表中的元素，只是单纯的倒过来，不按任何规则
#a.copy() #复制列表,浅拷贝
#a[:]  #等同于复制列表

#在 python 中对所有可变的数据类型不打印返回值，返回None

print(a)
"""

"""
#把列表当作堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())  #释放列表最顶端(最大索引)的元素;释放后就相当于从列表中删除了这个元素
print(stack)  
"""

"""
#列表当作队列使用：队列是特定的数据结构，最先进入的元素最先释放

from collections import deque  #定义队列的函数


queue = deque(['Eric', 'John', 'Machael'])
queue.append('Terry')
queue.append('Grame')
queue.popleft()  #移除队列最左边的一个元素
#print(queue.popleft())  #打印从队列最左边移除的元素
print(queue)
"""

"""
#列表推导式lamba：从序列中创建列表

squares = []  #创建一个空列表
#方法1
for x in range(10):  #此方法在循环结束后变量x依然存在，占用内存
    squares.append(x**2)

#方法2
squares = list(map(lambda x: x**2, range(10)))  #无副作用，等价于下一条

#方法3：列表推导式生成列表，更简单
squares = [x**2 for x in range(10)]  #等价于上一条;列表推导式，返回结果是一个列表

print(squares)  
"""

"""
b = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(b)

d = [(x, x**2) for x in range(6)]
print(d)

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
"""

"""
#列表推导式可使用复杂的表达式和嵌套函数
from math import pi

x = [str(round(pi, i)) for i in range(1, 6)]  #pi保留1到5个小数位四舍五入后的结果字符串化后组成列表x
print(x)
"""

'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12, 13],
]
'''

#print([[row[i] for row in matrix] for i in range(4)])

"""
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)   
"""

"""
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
"""

#print(list(zip(*matrix)))  #zip()函数

"""
a = [1, 2, 'c', 'd', 3, 5, 8]
del a[0]  #删除列表a索引为0的元素；列表会变化
del a[2:4]  #删除列表中索引在2到4(不包括4)的元素，即删除索引为2和3对应的元素
del a[:]  #情况列表元素
print(a)
"""

"""
#元组:元组元素不可变
empty = ()  #空元组
print(len(empty))

empty1 = ('nih',)  #单个元素的元组,元组可加或不加括号,建议加

print(empty1)
"""

#集合：集合是一个无序不重复元素的集
#大括号{}或 set() 函数可以用来创建集合
#创建空集合：必须使用 set()
#{}可用来创建空字典
#a = set()
#print(a)
#b = {}
#print(b)
basket = {'apple', 'orange', 'apple', 'pear', 'banana', 'orange'}
print(basket)  #打印集合时，重复元素会只显示一次

