#寻找100到1000之间的水仙花数，用循环最好
"""
import math
from random import randint
x = randint(100, 1000)
a = x // 100   #取百位数字
b = (x - a * 100) // 10   #取十位数字
c = x % 100 % 10   #取各位数字

#if x == a ** 3 + b ** 3 + c ** 3:
print(x, a, b, c)
while False:
    for num in x
"""
for num in range(100, 999):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)


