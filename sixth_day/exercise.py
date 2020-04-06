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