'''
这是我们编写的第一个模块，该模块包含以下内容
my_book: 字符串变量
say_hi: 简单的函数
User: 代表用户的类
'''
print('这是module 1')
my_book = '疯狂Python讲义'
def say_hi(user):
    print('%s,您好，欢迎学习Python' % user)
class User:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('%s正在慢慢地走路' % self.name)
    def __repr__(self):
        return 'User[name=%s]' % self.name
#以下部分是该模块中成员的测试代码
def test_my_book():
    print(my_book)
def test_say_hi():
    say_hi('孙悟空')
    say_hi(User('Charlie'))
def test_User():
    u = User('白骨精')
    u.walk()
    print(u)
#防止调用该模块时执行模块内的测试代码；即只允许 python module1.py 该模块自己才能执行模块内的测试代码
if __name__ == '__main__':
    test_my_book()
    test_say_hi()
    test_User()
