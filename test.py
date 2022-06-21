from PIL import Image

def newImage():
    img = Image.new('RGB', (100, 100))
    img.putpixel((30,60), (155,155,55))
    img.save('sqr.png')

wallpaper = newImage()
wallpaper.show()