#函数，定义函数
def factorial(num):   #定义阶乘函数块
    """
    求阶乘  #这是函数的用途
    :param num: 非负整数  #这是函数变量的解释
    :return: num的阶乘  #这是函数的结果
    """

    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))  # m会代替 num
n = int(input('n = '))  # n会代替 num

print(factorial(m) // factorial(n) // factorial(m - n))   #引用函数，直接引用函数名字即可

"""
#Python的math模块中其实已经有一个factorial函数了
如下：直接利用该函数
import math 
a = 5
print(math.factorial(a))
"""


