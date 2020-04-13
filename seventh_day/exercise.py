#案例1:验证输入用户名和QQ号是否有效并给出对应的提示信息
import re


def main():
    username  = input('请输入用户名： ')
    qq = input('请输入QQ号： ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)  #在正则表达式字符串前面加上 r 表示使用了"原始字符串"的写法
    #所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，说得更直接一点就是字符串中没有所谓的转义字符
    #如果不使用原始字符串就需要将反斜杠写作\\，例如表示数字的\d得书写成\\d，这样不仅写起来不方便，阅读的时候也会很吃力
    # re模块的match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    if not m1:
        print('请输入有效的用户名!')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)  #在正则表达式字符串前面加上 r 表示使用"原始字符串"的写法
    if m1 and m2:
        print('你输入的信息是有效的!')
    else:
        print('None')


if __name__ == "__main__":
    main()


#案例2:从一段文字中提取出国内手机号码。
import re


def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')  #创建正则表达式对象 使用了前瞻(?<=exp)和回顾(?=exp)来保证手机号前后不应该出现数字
    #pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    #更复杂的手机号码正则表达式: re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    
    #定义被正则表达式匹配的字符串
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也不是110或119，王大锤的手机号才是15600998765
    '''   

    mylist = re.findall(pattern, sentence)  #re的findall函数；返回的是一个字符串列表
    print(mylist)
    print('---------华丽的分割线----------')

    #通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):  #re的finditer函数
        print(temp.group())  #在正则表达式中,group()用来提取出分组截获的字符串
    print('---------华丽的分割线----------')

    #通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)  #re的search函数
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())  #关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符,如： end=',' end()表示按行输出


if __name__ == "__main__":
    main()


#案例3:替换字符串中的不良内容
import re


def main():
    sentence = "你丫是傻叉吗? 我操你大爷的. Fuck you."
    """
    说明： re模块的正则表达式相关函数中都有一个flags参数，它代表了正则表达式的匹配标记，可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。
    如果需要为flags参数指定多个值，可以使用按位或运算符进行叠加，如flags=re.I 或 re.M。
    """
    purified = re.sub('[操肏艹]|fuck|shit|傻[比逼叉缺屌吊]|煞笔','*', sentence, flags=re.I)
    print(purified)


if __name__ == "__main__":
    main()


#案例四:拆分长字符串
import re


def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  #输出结果是: ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == "__main__":
    main()