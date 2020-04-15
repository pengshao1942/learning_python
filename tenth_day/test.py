from PIL import Image, ImageFilter

image = Image.open('test.JPG')

image.filter(ImageFilter.CONTOUR).show()