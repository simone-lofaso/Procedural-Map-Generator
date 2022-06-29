#This class will represent our pre-drawn tiles
#from PIL import Image
import random

WATER_CHANCE = .25


if __name__ == "__main__":
    print("run drawer.py ya doofus")
    quit

def chooseTile(tile, xIndexDraw, yIndexDraw, xIndex, yIndex):
    """ Chooses which tile should be drawn at the given location, then calls the right method to draw the specified tile.
     Index will respond to four times the location of the index. E.G. Index 0, 4 points to starting pixel 0, 16.
    

    Parameters:
        tile: The tile number designated to be drawn. 1 for water, 2 for blah blah blah
        xIndex: the x Index of the matrix.
        yIndex: the y Index of the matrix. 


    """
    import drawer 
    if drawer.map[xIndex][yIndex] == 1:
        tile = random.randint(0, 3)


    if (tile == 1): #NOT A GOOD WAY OF DOING THIS but python has no switch statements until 3.10, which doesnt work with numpy right now. Maybe think of better way ;)
        water(xIndexDraw, yIndexDraw)
    elif (tile == 2):
        coast(xIndexDraw, yIndexDraw)
        
def getLowestEntropy(xIndex, yIndex):
    #maybe we don't need this until we make it complicated. Drawing a map shouldnt need this
    #will need to check 4 (or 8?) closest tiles. only check if 
    return 0


def water(xIndex , yIndex):
    """Draws and saves water tile to image
    
    Parameters:
        xIndex: the x Index of the matrix
        yIndex: the y Index of the matrix
    """
    import drawer #avoids circular import. is this the best way to do it? Fuck you.
    drawer.img.putpixel((xIndex * 4, yIndex * 4), (28,163,236)) #better way to do this?
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 3), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (28,163,236))
    drawer.img.save("wtf.png")

def coast(xIndex, yIndex):
    print("Durr i havent done this yet")