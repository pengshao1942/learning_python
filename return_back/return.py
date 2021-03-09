a_dict = {'语文': 98, '数学': 100, '英语': 120}
print(type(a_dict))
print(a_dict)
empty_dict = {}  #创建空字典
#empty_dict1 = dict()  #用dict()函数创建空字典
veg1 = (('clean', 1.58), ('boold', 1.29), ('aa', 2.19))  #用dict()函数创建字典时，列表或元组只能包含两个元素
dict1 = dict(veg1)
print(dict1)
list1 = [['a', 22], ['b', 33], ['d', 44]]  #用dict()函数创建字典时，列表或元组只能包含两个元素
dict2 = dict(list1)
print(dict2)
dict3 = dict(clean = 1.58, boold = 1.29) #dict指定关键字参数创建字典
print(dict3) 
