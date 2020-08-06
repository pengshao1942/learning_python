'测试__all__变量的模块' 

def hello():
    print("Hello, Python")
def world():
    print("Python World is funny")
def test():
    print('--test--')

#定义__all__变量，默认只导入hello和world两个程序单元
__all__ = ['hello', 'world']