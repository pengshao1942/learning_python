'''
#Python引用，有一个常量池
for constant in range(300):
    if constant is not range(300)[constant]:
        print("常量池最大值为：", (constant - 1))
        break

a = [1, 2]
print(id(a+[1]))
'''
'''
#str.format方法的使用案例
print('{}网址： "{}!"'.format('Python技术', 'www.justdopython.com'))

#数字用于指向传入对象在format中的位置，类似索引
print('{0} 和 {1} 和 {2}'.format('Hello', 'World!', '?'))  

#str.format使用了关键字参数,值会指向使用了该名字的参数
print('{name}网址： {website}'.format(name='Python技术', website='www.justdopython.com'))  

#str.format 位置和关键字参数任意结合使用: 关键字参数不能在位置参数的前面，反之亦然
print('电商网站有：{0} {1} {name}'.format('淘宝', '拼多多', name='python'))

#用 ** 标志将字典{'key1': 'hello'; 'key2': 'world'}以关键字参数的方式传入
#repr() 函数产生一个解释器易读的表达形式，str() 函数返回一个用户易读的表达形式
print("str() 'key1': 'hello'; 'key2': 'world'".format('test1', 'test2'))

#字段名后允许可选的格式和指令，如格式化PI为浮点数，保留三位小数位
import math
print('The value of PI is approximately {0:.3f}'.format(math.pi))

#在字段后加一个整数会限定该字段的最小宽度,如：限定第一个值宽度最小为10,第二个值最小宽度为10，格式化为整数最大无上限
table = {'Sjoredfs': 123, 'Jack': 456, 'Dcab': 789}
for name, phone in table.items():print('{0:10} ==> {1:10d}'.format(name, phone))  #for循环的一种写法，直接:接print

#将一个很长的格式化字符串传入字典，用中括号[]访问它的键
table2 = {'ddsds': 123, 'mkdmk': 456, 'klldkd': 78945646132132}
print('mkdmk: {0[mkdmk]:d}; ddsds:{0[ddsds]:d}; klldkd: {0[klldkd]:d}'.format(table2))

#用 ** 标志将字典以关键字参数的方式传入,如将table3字段以关键字参数的方式传入
table3 = {'sss': 123, 'dda': 456, 'aaa': 7897897894511512}
print('dda: {dda:d}; sss: {sss:d}; aaa: {aaa:d}'.format(**table3))
'''

#文件的操作
#input() 读取键盘的输入，如： a = input("请输入： ")
#文件的读写：
#open()函数返回文件对象，语法：open(filename, mode)

'''
#文件可使用绝对路径或相对路径，windows下的\必须写成/
f = open('eleventh_day/tmp.txt', 'r')
#read() 是读取文件中的字符,()内的数字是表示读取几个字符，换行符\n占一个字符
#str = f.read(2)  
#readline() 读取一行，换行符为 \n
#str = f.readline()
#readlines()读取文件中的所有行，默认会将换行符\n也显示出来
str = f.readlines()
print(str)
f.close()  #打开后一定要记得关闭文件，否则会长期不能释放内存
'''
'''
#write(string)  将string的内容写入文件,会直接覆盖文件的原始内容
f = open('eleventh_day/tmp.txt', 'w')
num = f.write('Hello Python')  #定义写入的字符数
print(num)  
f.close
'''
'''
#seek(offset,from_what) 改变当前文件的位置
#offset 移动距离；from_what 起始位置，0 表示开头，1 表示当前位置，2 表示结尾，默认值为 0 ，即开头。
f = open('eleventh_day/tmp.txt', 'rb+')
f.write(b'012345679abcd')
f.seek(5)  #移动到文件的第6个字节，n + 1
print(f.read()) #第6个字节之前的就不显示了
'''
'''
#tell() 返回文件对象当前所处的位置(用了seek()之后才会生效)，从文件开头算起的字节数
f = open('eleventh_day/tmp.txt', 'r')
f.seek(6)
print(f.tell())  
'''
'''
#用完文件后关闭: 调用close()来手动关闭或使用with关键字(with...as f)处理文件对象，使用完后自动关闭
with open('eleventh_day/tmp.txt', 'r') as f:
    read_data = f.read()
print(f.closed)  #f.closed 是一个布尔属性
print(f.close)  #f.close  关闭文件
'''

'''
a = '12343gdf'
b = '123'
c = 'abcddf'
#isalnum()方法检测一个字符串是否只由字母和数字组成
print(a.isalnum())   
#isnumeric()方法检测一个字符串是否仅仅包含数字
print(a.isnumeric()) 
print(b.isnumeric())
#isalpha()方法检测一个字符串是否仅仅包含字母
print(a.isalpha()) 
print(c.isalpha())
'''
'''

#string模块
#python string 模块
import string

#string.ascii_lowercase  输出所有的小写字母
#string.ascii_uppercase  输出所有的大写字母
#string.ascii_letters  输出所有的大小写字母
#string.digits  输出0-9的数字
#string.hexdigits 输出十六进制的字符
#string.printable  输出所有的大小写，数字，特殊字符
alphabet = list(string.ascii_lowercase)  #list()方法可定义列表
print(alphabet)
b = string.hexdigits
print(b)
'''

#序列化
'''
import json
data = {'id':1, 'name':'john', 'age':12}
with open('t.json', 'w') as f:
    json.dump(data, f)  #从文件中写入内容并序列化未json格式

with open('eleventh_day/t.json', 'r') as f:
    d = json.load(f)    #从文件中读取含json格式的数据并反序列化
print(d)

str1 = '12322324'
print(json.loads(str1))  #字符串序列化

print(json.dumps(data))  #将对象序列化
'''

