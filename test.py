from PIL import Image
#Not sure if I want to use numpy to make matrix or natively do it. numpy allows various functions but i dont think we'll need em
#no import required
#matrix = [[0]*5 for i in range(5)]
#import required

#import numpy
#numpy.zeros((5, 5))

#might want to add a way to "animate" the drawing of the pixel. Would be super slow but it wil look pretty
def newImage():
    img = Image.new('RGB', (100, 100))
    img.putpixel((30,60), (155,155,55))
    img.save('sqr.png')
    return img

wallpaper = newImage()
wallpaper.show()