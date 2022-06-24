#name is temp, feel free to come up with something better. This will include main()

from PIL import Image
import numpy
import tiles #wont fuckin work


matrix = numpy.zeroes((16,16))
img = Image.new('RGB', (64, 64 ))

def createMatrix():
    """Initial creation of the matrix representing our image. Each index represents a 4x4 pixel tile

    Returns:
        16x16 matrix filled with zeroes
        
    """
    matrix = numpy.zeroes((16,16))
    #matrix[3][4] = 4
    print(matrix)


def newImage():
    """Initial creation of image. Will only be called once

    Returns:
        white image 64x64 pixels
        
    """  
    img = Image.new('RGB', (64, 64 ))
    img.putpixel((10,10), (155,155,55))
    img.putpixel((11,10), (155,155,55))
    img.putpixel((10,11), (155,155,55))
    img.putpixel((11,11), (155,155,55))
    img.save('sqr.png')
    return img


def main():
    
    wallpaper = newImage()
    ##tiles.water(0,0)
    wallpaper.show()
