#python实现文件读写操作
#通过python内置的open函数，文件路径可用绝对路径和相对路径
"""对文件的操作
操作模式        具体含义
'r'             读取(默认)
'w'             写入(会先截断之前的内容)
'x'             写入,如果文件已经存在会产生异常
'a'             追加,将内容写入到已有文件的末尾
'b'             二进制模式
't'             文本模式(默认)
'+'             更新
文件默认编码是None,可通过encoding参数指定编码;编码不对也会导致文件打不开,或报错
"""

#异常机制的使用：在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，
#在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况
def main():
    f = None
    try:  #异常机制,try:....except:....finally:....
        f = open('hello.txt', 'r', encoding='utf-8')  #文件不存在或无法打开会引发异常,报错
        #f = open('/learning_python/sixth_day/hello.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:  #文件不存在的异常
        print('无法打开指定的文件')  #发生此异常时的提示
    except LookupError:  #文件编码不对的异常
        print('指定了未知的编码')  #发生此异常时的提示
    except UnicodeDecodeError:  #未按指定的方式解码时的异常
        print('读取文件时解码错误')  #发生此异常时的提示
    finally:  #释放外部资源的操作
        if f:
            f.close()

if __name__ == "__main__":
    main()


#通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

def main():
    try:
        with open('hello.txt', 'r', encoding='utf-8') as f:  #with关键字
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()



import time


def main():
    # 一次性读取整个文件内容
    with open('hello.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取文件
    with open('hello.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 用readlines方法将文件按行读取到列表中
    with open('hello.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()

#文件的写入
from math import sqrt

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) +1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if number < 100:
                fs_list[0].write(str(number) + '\n')
            elif number < 1000:
                fs_list[1].write(str(number) + '\n')
            else:
                fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close
        print('操作完成!')


if __name__ == "__main__":
    main()


#读写二进制文件
#如：复制图片文件
def main():
    try:
        with open('jpg1.jpg', 'rb' ) as fs1:
            data = fs1.read()
            print(type(data)) # <class 'bytes'>
        with open('jpg2.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序执行结束')


if __name__ == "__main__":
    main()


#读写JSON文件
#序列化
import json  #json模块可以将字典或列表以JSON格式保存到文件中


def main():
    mydict = {
        'name': '马东',
        'age': 32,
        'qq': 9589794,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 220},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)  #dump是json的转换函数,转换成json文件
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == "__main__":
    main()



#反序列化
import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)  #json的loads函数将字符串的内容反序列化成Python对象,即resp.text
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()


"""
json模块主要有四个比较重要的函数，分别是：

dump  - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load  - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""
#从一系列字节中提取数据结构的操作，就是反序列化(deserialization)
#序列化(serialization)是指将数据结构或对象状态转换为可以存储或传输的形式

#在Python中要实现序列化和反序列化除了使用json模块之外
#还可以使用pickle和shelve模块，但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被Python识别

#关于异常的解释和实践:https://segmentfault.com/a/1190000007736783

