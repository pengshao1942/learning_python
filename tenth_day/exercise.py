# Python用Pillow操作图像
# Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作
# 安装Pillow: pip install pillow
# Pillow库中的Image类可读取和处理图像

from PIL import Image   #导入图像处理库

#查看图像格式
image = Image.open('test.JPG')
image.format, image.size, image.mode
image.show()

#裁剪图像
rect = 80, 20, 310, 360
image = Image.open('test.JPG')
image.crop(rect).show()  

#生成缩略图
size = 128, 128  #设定缩略图尺寸
image = Image.open('test.JPG')
image.thumbnail(size)  #生成缩略图
image.show()

#缩放和黏贴图像
image1 = Image.open('test1.PNG')
image2 = Image.open('test.JPG')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

#旋转和翻转
image = Image.open('test.JPG')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

#操作像素
image = Image.open('test.JPG')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

image.show()


#滤镜效果
from PIL import Image, ImageFilter

image = Image.open('test.JPG')
image.filter(ImageFilter.CONTOUR).show()

