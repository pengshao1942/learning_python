#导入 fk_package 包，实际上就是导入包下的 __init__.py 文件
import fk_package

#导入fk_package包下的print_shape模块，实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape   #程序访问print_shape.py的程序单元需要添加 fk_package.print_shape 前缀 

#导入 fk_package 包下的billing模块，实际上就是导入 fk_package 目录下的 billing.py 
from fk_package import billing  #程序访问 billing.py 的程序单元，需要添加 billing前缀

#导入 fk_package 包下的 arithmetic_chart 模块，实际上就是导入 fk_package 目录下的 arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)  #访问fk_package包下print_shape模块内的print_blank_triangle方法
im = billing.Item(4.5)  #访问fk_package包下 billing 模块的 Item 类
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)  #访问  fk_package 包下arithmetic_chart模块的print_multiple_chart方法   


