def print_blank_triangle(n):
    '打印一个由星号组成的空心的三角形'
    if n <=0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*', end='')
        if i != n - 1:
            print('*' * (2 * i - 1), end='')
        else:
            print('*' * (2 * i - 1), end='')
        if i != 0:
            print('*')
        else:
            print('')
        
