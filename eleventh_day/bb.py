#引用自定义的模块：模块以及放在 lib\site-packages 目录下
import print_shape1
print(print_shape1.__doc__)
print_shape1.my_list[1]  #访问模块中的变量
print_shape1.print_triangle(5)  #引用模块中的print_triangle()方法
print_shape1.test_print_triangle() #引用模块中的test_print_triangle()方法