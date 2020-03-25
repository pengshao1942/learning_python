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

