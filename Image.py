#change extesnion
from PIL import Image,ImageEnhance,ImageFilter
img1 =Image.open('image2.jpg')
img1.save('image2.png')
#reszing
Max_size = (250,250)
img1.thumbnail(Max_size)
img1.save('thumnail.jpg')
#change list fo photos 
import os
for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item) 
        filename,extension = os.path.splitext(item)
        img1.save(f'{filename}.png')
#sharpness
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(3).save('nisch.jpg')

#colort
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(0).save('nisch-bw.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.4).save('nischbrightness.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.2).save('nischcontrast.jpg')
#img blur
img1.filter(ImageFilter.GaussianBlur(radius=2)).save('blur.jpg')
#0:blurry 1:original 2 3...> more sharpness
