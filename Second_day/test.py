from random import randint

def roll_dice(n=2):   #第一个函数，指定了函数参数的默认值为2
    """
    摇骰子
    ：parm n: 骰子的个数
    ：return：n颗骰子的点数之和
    """

    total = 0 
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):  #第二个函数
    return a + b + c

print(roll_dice())



