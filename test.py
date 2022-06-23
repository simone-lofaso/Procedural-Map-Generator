from PIL import Image
import numpy

a = numpy.zeros((16, 16))
a[3][4] = 4
print(a)

def newImage():
    img = Image.new('RGB', (48,48 ))
    img.putpixel((10,10), (155,155,55))
    img.putpixel((11,10), (155,155,55))
    img.putpixel((10,11), (155,155,55))
    img.putpixel((11,11), (155,155,55))
    img.save('sqr.png')
    return img

wallpaper = newImage()
wallpaper.show()