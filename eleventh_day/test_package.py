#导入 first_package 包(模块)
import first_package

print('============')
print(first_package.__doc__)  #输出包的文档
print(type(first_package))  #输出包的类型
print(first_package)  #打印包本身

#输出如下：
'''
this is first_package
============

这是学习包的第一个示例

<class 'module'>
<module 'first_package' from 'd:\\learning_python\\eleventh_day\\first_package\\__init__.py'>
'''
