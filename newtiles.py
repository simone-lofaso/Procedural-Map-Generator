import math
import random
import numpy

def getLowestEntropy():
    return 0

def chooseTile():
    return 0



def flower(xIndex, yIndex):
    import newwavefunction
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (255, 216, 0))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (255, 216, 0))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (255,255,255))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (0,154,23))

    newwavefunction.img.save("output2.png")
    newwavefunction.img.show()
