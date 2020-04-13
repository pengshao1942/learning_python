#正则表达式:Python通过标准库中的re模块来支持正则表达式操作
#特殊字符需要用转义符号转义：\  如：匹配.  ，写成：\.   ;匹配圆括号 \(\)
#正则表达式入门：https://deerchao.cn/tutorials/regex/regex.htm
#正则表达式测试器：在网络上搜索对应语言的，如Python
#re模块的核心函数：pattern就是正则表达式串;flags=0可以省略
"""
        函数	                                            ··说明
compile(pattern, flags=0)	                    编译正则表达式并返回正则表达式对象
match(pattern, string, flags=0)	                用正则表达式匹配字符串,成功则返回匹配对象,否则返回None，string表示字符串
search(pattern, string, flags=0)	            搜索字符串中第一次出现正则表达式的模式,成功则返回匹配对象,否则返回None
split(pattern, string, maxsplit=0, flags=0)	    用正则表达式指定的模式分隔符拆分字符串并返回列表
sub(pattern, repl, string, count=0, flags=0)	用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数,repl表示替换后的内容，如把屏蔽的内容替换为*
fullmatch(pattern, string, flags=0)	            match函数的完全匹配（从字符串开头到结尾）版本
findall(pattern, string, flags=0)	            查找字符串中所有与正则表达式匹配的模式并返回字符串的列表
finditer(pattern, string, flags=0)	            查找字符串所有与正则表达式匹配的模式并返回一个迭代器
purge()	                                        清除隐式编译的正则表达式的缓存
re.I 或 re.IGNORECASE	                        忽略大小写匹配标记
re.M 或 re.MULTILINE	                        多行匹配标记
"""
#如果一个正则表达式需要重复的使用，那么先通过compile函数编译正则表达式并创建出正则表达式对象无疑是更为明智的选择

#正则表达式的函数的写法：
#1、当初始正则表达式变量不存在,需要定义时,如：pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#2、当初始正则表达式变量已存在，再基于初始正则表达式变量建立变量时,如:m = pattern.search(sentence),此时pattern变量已经存在






