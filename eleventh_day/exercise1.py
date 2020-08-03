"""
#直接选择排序函数实现：
def chosen_sort(list):
    list_len = len(list)  #列表的长度是不变的，只需其中元素顺序变了
    for i in range(0, list_len):  #从第一个元素开始比较
        for j in range(i + 1, list_len):  #从第i+1个元素开始比较
            if list[i] > list[j]:  #比较值大小
                list[i], list[j] = list[j], list[i]  #直接选择的中心点：交换

list1 = [1, 3, 2, 7, 8, 5, 11, 4, -20]
chosen_sort(list1)
print(list1)



#冒泡排序函数实现：
def bubble_sort(list):
    list_len = len(list)
    for i in range(0, list_len - 1):
        for j in range(i + 1, list_len):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]  #冒泡排序中心点也是交换，只不过是前一个和后一个元素交换

#list1 = [1, 3, 2, 7, 8, 5, 11, 4, -20]
list1 = [3, 6, 1, 8, 5, 0, -20, 100, 50, 200, -32, 123]
bubble_sort(list1)
print(list1)

#求阶乘函数
def fn(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(fn(5))


#求1~n之间每个数的立方和的函数
def cube_sum(n):
    if n < 1:
        exit()   #判断是否为正整数
    result = 0   #求和用sum代替： sum =0 
    for i in range(1, n + 1):
        result += i * i  * i  #可简写为 i ** 3，用幂运算代替
    return result  #代替：return sum

n = int(input("请输入数字:"))  #可用输入代替传函数形参
#result = cube_sum(n)
#print("1～%d的立方和是%d" % (n, result))
print(cube_sum(n))
"""

#去除给定列表中重复元素并输出去重后的列表的函数：
def leave_list(list):
    #result = list
    for i in list:
        count = list.count(i)
        if count > 1:
            list.remove(i)
    return list

list1 = ['aa', 'aa', 1, 1, 2, 3, 5, 'ss', 5, 'ss']
print(leave_list(list1))
        
            