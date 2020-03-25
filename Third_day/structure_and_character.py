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




