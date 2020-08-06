def print_multiple_chart(n):
    '打印乘法口诀表的函数'
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %2d' % ((j + 1), (i + 1), (j + 1) * (i + 1)), end= ' ')
        print('')
    
