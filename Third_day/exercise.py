#在屏幕上打印跑马灯文字
import os
import time

def main():
    content = '抗击新冠肺炎，打赢这场无硝烟的战争！......'

    while True:
        os.system('cls')  #等于 os.system('clear')，清理屏幕上的输出
        print(content)
        time.sleep(0.2) #休眠200毫秒后继续输出
        content = content[1:] + content[0]   #跑马灯效果

if __name__ == '__main__':
    main()

#生成指定长度的验证码,由数字和字母随机组成
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1  #下标(索引)数量
    code = ''  #初始化值为空
    for _ in range(code_len):  #
        index = random.randint(0, last_pos)  #生成下标(索引)
        code += all_chars[index]  #取对应索引的值

    return code

print(generate_code(4))  #打印生成的验证码


#设计一个函数返回给定文件名的后缀名
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')  #rfind()返回子字符串在字符串中最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1,即find的反函数
    if 0 < pos < len(filename) - 1: #pos是.出现的范围
        index = pos if has_dot else pos + 1  #返回的后缀名是否需要带点
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':   #非main函数的打印
    print(get_suffix('hello.gif'))
    print(get_suffix('hello.jpg'))
    print(get_suffix('hello.c'))

#设计一个函数返回传入的列表中最大和第二大的元素的值
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

if __name__ == '__main__':
    print(max2([1, 2, 3, 4, 5]))

#计算指定的年月日是这一年的第几天
def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True,平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0 #

def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天
    :param year:年
    :param month:月
    :param date:天
    :return：第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], #平年每月天数
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #闰年每月天数
    ][is_leap_year(year)]  #判断每月几天
    total = 0
    for index in range(month -1):
        total += days_of_month[index]  #判断每月的天数
    return total + date  #输出总的天数，就是每月的天数累加

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))

if __name__ == '__main__':  
    main()  #直接打印main函数的结果，就可以这么用

#打印杨辉三角
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row -1][col] + yh[row -1][col -1]
            print(yh[row][col], end=' ')
        print()

if __name__ == '__main__':
    main()


#模拟双色球机选号
from random import randrange, randint, sample   #从random模块导入这三个函数

def display(balls):
    """
    输出列表中的双色球号码
    :param: balls:双色球号码
    :return: ball:号码
    """
    for index, ball in enumerate(balls): #参考enumerate函数用法
        if index == len(balls) -1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]  #定义双色球的红色号码列表
    selected_balls = []  #初始选择的球为空
    selected_balls = sample(red_balls, 6) #参考sample函数用法,表示从red_balls中随机抽取6个不重复元素，并将6个元素以列表形式返回
    selected_balls.sort() #sort函数排序列表
    selected_balls.append(randint(1, 16)) #append函数,在列表/元组等末尾添加新的元素
    return selected_balls

def main():
    n = int(input('机选几注： '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()


#约瑟夫环的问题
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()


#井字棋游戏
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()