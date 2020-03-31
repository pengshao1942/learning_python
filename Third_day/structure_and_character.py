def main():
    list1 = [1, 3 ,5 ]
    print(list1)
    list2 = ['hello', 'world'] * 5  #列表乘数字，变成列表的元素按顺序加长组成新的列表
    print(list2)
    print(len(list1))
    print(list1[0])  #打印出列表list1的索引0对应的元素，即第一个元素；索引顺数从0开始，倒数从-1开始
    print(list2[3])
    #print(list2[15])  #IndexError: list index out of range ,超出索引范围
    print(list1[-1])   #列表索引是负数，元素就按倒叙排列;最后一个是-1，依次反增，如：-1，-2，-3
    #print(list1[-6])   ##IndexError: list index out of range ,超出索引范围
    list1[2] = 300  #列表替换元素,会替换当前索引的元素
    print(list1)

    #下面3种都是列表添加元素
    list1.append(200)  #增加元素，在最后面的元素后增加
    print(list1)
    list1.insert(1, 400)  #插入元素，在对应的索引处增加,原先的索引+1，位置往后移动
    print(list1)
    list1 += [1000, 2000]  #即 list1 = list1 + [1000, 2000],按顺序往后增加元素
    print(list1)

    #删除列表单个元素,remove关键字针对的是列表的位置
    list1.remove(3)  #删除对应位置的元素,这个3不是索引，只是单纯的位置，从1开始;删除后这个位置的数字就没有了，其他元素的索引按序移动
    print(list1)
    list1.remove(1)  #删除上面list1结果的第一个元素
    print(list1)
    print(list1[0])
    
    #或用if分支结构删除列表中的元素，if针对的直接是元素的值
    if 400 in list1:   #删除列表list1中元素值为400的元素
        list1.remove(400)  #删除后只剩下[300, 200, 1000, 2000]了
    print(list1)
    
    #或del关键字删除索引处的元素
    del list1[0]  #在删除索引为0的元素，del关键字是针对列表的索引
    print(list1)

    #清空列表元素
    list1.clear()
    print(list1)  #打印出空列表[]，不是空值
    
if __name__ == '__main__':
    main()


#列表的切片操作
def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

	# 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')  #title关键字表示每个元素首字母大写，end=' '表示每个值以空格隔开
    print()

    # 列表切片
    fruits2 = fruits[1:4]  #取fruits列表中索引1到4的元素组成新的列表fruits2;不包含4索引对应的元素
    print(fruits2)

    #fruit3 = fruits  # 如果这样做，则没有复制列表只创建了新的引用
    # 若要复制列表，可以通过完整切片操作来复制列表
    fruits3 = fruits[:]  #完整切片
    print(fruits3)

    fruits4 = fruits[-3:-1]  #反向切片，不包含-1索引对用的元素
    print(fruits4)

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]  #列表反向
    print(fruits5)


if __name__ == '__main__':
    main()


#列表的排序操作
def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1) #sorted函数不加参数对列表list1默认按字母排序生成新的列表list2，但不会改变列表list1
    #函数的设计就应该像sorted函数一样尽可能不产生副作用；sorted函数先会默认按字母排序
    list3 = sorted(list1, reverse=True) #sorted函数的reverse参数，对列表list1按字母排序后再反转生成列表list3
    list4 = sorted(list1, key=len) #sorted函数的key关键字对列表list1按字符串长度生成列表list4
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    list1.sort(reverse=True)  #sort函数的reverse关键字给列表对象发出反向排序消息直接在列表对象上进行反向排序,按字母顺序反向排序
    print(list1)

if __name__ == '__main__':
    main()


#使用列表的生成式语法来创建列表
import sys

def main():
    #用列表的生成表达式语法创建列表容器
    f = [x for x in range(1, 10)]   #列表生成式,range不包含尾长的数
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567'] #列表生成式，每个元素是x + y的值
    print(f)

    #用这种for循环语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  #sys.getsizeof函数是sys模块导入的,查看对象(这里是查看列表)占用内存的字节数:9016字节
    print(f)

    """
    下面的代码创建的不是一个列表而是一个生成器对象
    通过生成器可以获取到数据但它不占用额外的空间存储数据
    每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    """
    f = (x ** 2 for x in range(1, 1000))  #这不是列表，是生成器对象，用()表示，列表用[]表示;这是一种生成器语法
    print(sys.getsizeof(f))  #相比列表只占用112字节的内存空间
    print(f)  #输出<generator object main.<locals>.<genexpr> at 0x000001E152F8FF90> 是生成器结果的简写
    for val in f:
        print(val)  #用for循环打印生成式f的每个值
    

if __name__ == '__main__':  #只有函数内部有可执行的表达式时，才可用main
    main()

#定义斐波拉契数列生成器函数
def fib(n):   #定义斐波拉契数列函数
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  #yield关键字将该函数改造成生成器函数

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()

#使用元组：元组与列表类似，但是元组中的元素不能修改
def main():
    #定义元组
    t = ('shaopeng', 38, True, '四川成都')  #和生成式一样，使用()
    print(t)  #打印元组
    #获取元组中的元素
    print(t[0])
    print(t[3])
    #遍历元组中的值
    for i in t:
        print(i)
    #重新给元组赋值
    #t[0] = '王大锤'  #TypeError,即元素的值不能修改
    t = ('王大锤', 29, True, '四川绵阳')
    print(t)
    #将元组转换成列表
    person = list(t)  #使用list关键字将元组转换成列表,转换后person就是列表了
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    #将列表转换成元组
    fruits_list = ['apple', 'orange', 'pear']  #定义列表fruits_list
    fruits_tuple = tuple(fruits_list) #使用tuple关键字将列表转换成元组
    print(fruits_tuple)

if __name__ == '__main__':
    main()

#使用列表和元组的结论：如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组
#如果一个方法要返回多个值，使用元组也是不错的选择 


#可在ipython中使用%timeit来分析创建同样元素的列表和元组所花费的时间
#%timeit f1 = (1, 2, 3, 'ABC', 'abc')
#%timeit f = [1, 2, 3, 'ABC', 'abc']
#结果是同样元素的元组的创建花费的时间比列表要短的多
import  sys
def main():
    f = [1, 2, 3, 'ABC', 'abc']
    f1 = (1, 2, 3, 'ABC', 'abc')
    print(sys.getsizeof(f))  #比较创建同样元素的元组和列表占用的内存大小
    print(sys.getsizeof(f1))

if __name__ == '__main__':
    main()


#创建集合：集合和数学上的集合一样;不允许有重复元素，而且可以进行交集、并集、差集等运算
def main():
    set1 = {1, 2, 3, 3, 3, 2}  #集合用{}
    print(set1)  #打印集合，打印出来，重复的数字只显示一次，因为集合不允许重复元素
    set2 = set(range(1, 10, 2))  #利用set关键字加range函数将数字转换成集合
    print(set2)
    set1.add(5)  #集合添加一个元素5
    set2.update([11, 12]) #update关键字，集合添加多个元素,或将列表元素添加到集合中
    print(set1)
    print(set2)
    set2.discard(5)  #discard关键字，摘除集合元素5
    print(set2)

    #利用if结构移除元素
    if 3 in set1:
        set1.remove(3)
    print(set1)
    #遍历集合容器
    for x in set2:
        print(x ** 2, end=' ')
    print()  #print不加参数表示换行,即打印一行空行

    #将元组转换为集合
    set3 = set((1, 2, 3, 4, 4, 3, 2, 1)) #set关键字将元组(1, 2, 3, 3, 2, 1)转换成集合
    print(set3.pop())  #pop函数用于移除元组、集合、列表的一个元素(默认是最后一个)，并返回该元素的值
    print(set3)

    #集合的运算：交集、差集、并集、对称差运算;运用运算符或集合对象的方法
    print(set1)
    print(set2)

    print(set1 & set2) #交集符号计算2个集合的交集
    print(set1.intersection(set2)) #intersection函数计算2个集合交集

    print(set1 | set2) #并集符号计算2个集合的并集
    print(set1.union(set2))  #union函数计算2个集合并集

    print(set1 - set2)  #差集符号计算2个集合的差集
    print(set1.difference(set2)) #difference函数计算2个集合的差集

    print(set1 ^ set2) # #返回2个集合中不重复的元素集合
    print(set1.symmetric_difference(set2))  #symmetric_difference函数返回2个集合中不重复的元素集合
    
    #判断子集和超集
    print(set1 <= set2)  #子集符号计算2个集合的子集
    print(set1.issubset(set2))  #issubset函数计算2个集合的子集

    print(set1 >= set2)  #超集符号计算2个集合的超集
    print(set1.issuperset(set2))   #issuperset函数计算2个集合的超集


if __name__ == '__main__':
    main()


#使用字典：可存储任意类型的对象，每个元素由键值对组成，键和值通过冒号分开
def main():
    scores = {'王兴': 95, '李东': 78, '张牛': 82}  #创建字典
    print(scores['王兴']) #通过键获取字典中的对应的值
    for elem in scores:  #对字典进行遍历(遍历的其实是键，再通过键取对应的值)
        print('%s\t--->\t%d' % (elem, scores[elem]))  #\t表示tab键形成的4个空格；多参数的打印方法

    scores['李东'] = 65  #根据键更新字典中键对应的值

    #增加键值对
    scores['诸葛瞻'] = 78  #为字典增加键值对
    scores.update(冷面=67, 方源=75) #用update函数为字典增加多个键值对
    print(scores)

    x = '李东'
    if x in scores:  #if结构查询字典中某个键对应的值，如：x为李东,则会打印出李东这个键对应的值
        print(scores[x])
    #if '李东' in scores:
        #print(scores['李东'])
    print(scores.get('李东')) #用get函数获取字典中键对应的值并打印该值

    #删除字典中的元素
    print(scores.popitem())  #popitem函数默认删除字典中最后的键值对元素，删除后字典就变化了
    print(scores.popitem())  #popitem函数默认删除字典中最后的键值对元素
    print(scores)
    print(scores.pop('李东', 65))  #pop函数删除字典中指定的键值对
    print(scores)

    #清空字典
    scores.clear()  ##clear函数会清空字典
    print(scores.clear()) #print打印清空后的字典，为None
    print(scores)  #打印清空后的字典，是空字典

if __name__ == '__main__':
    main()
    



