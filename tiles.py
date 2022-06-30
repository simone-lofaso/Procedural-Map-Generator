#This class will represent our pre-drawn tiles
#from PIL import Image
import random

#format CURRENTTILE_NEXT_TILE CHANCE
#ex: water_ coast_chance is the chance if the current tile is water for the next tile to be coast
WATER_WATER_CHANCE = .75
WATER_COAST_CHANCE = .25
COAST_LAND_CHACE = .75 #incease to increase thickness of coast (i think)
#these are not done yet. will need each relation for possible tiles touchin
#also the values are placeholder, feel free to change if you want to


if __name__ == "__main__":
    print("run drawer.py ya doofus")
    quit

def chooseTile(xIndexDraw, yIndexDraw, xIndex, yIndex): #need more clear param names
    """ Chooses which tile should be drawn at the given location, then calls the right method to draw the specified tile.
     Index will respond to four times the location of the index. E.G. Index 0, 4 points to starting pixel 0, 16.
    

    Parameters:
        xIndex: the x Index of the current tile
        yIndex: the Y Index of the current tile
        xIndexDraw: the X index of the new tile to be drawn
        yIndexDraw: the Y index of the new tile to be drawn


    """
    import drawer #want to figure out how to import this at the top 
    currentTile = drawer.map[xIndex][yIndex]
    """
    if currentTile == 1: #we can change this to pythons equivalent of a switch statement if we update numpy and python to 3.10, but idk if im lazy enough
        #use random generator 
        #chance for tiles next to water
    elif currentTile == 2:
        #chance for tiles next to coast
    elif currentTile == 3:
        #chance for tiles next to land
    

    if (tile == 1): #NOT A GOOD WAY OF DOING THIS but python has no switch statements until 3.10, which doesnt work with numpy right now. Maybe think of better way ;)
        water(xIndexDraw, yIndexDraw)
    elif (tile == 2):
        coast(xIndexDraw, yIndexDraw)
    elif (tile == 3):
        land(xIndexDraw, yIndexDraw)
    """
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
    drawer.img.save("output.png")

def coast(xIndex, yIndex):
    import drawer
    drawer.img.putpixel((xIndex * 4, yIndex * 4), (242,209, 107)) #better way to do this?
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4), (242,209, 107))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 1), (242,209, 107))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 2), (242,209, 107))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 3), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (242,209, 107))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (242,209, 107))
    drawer.img.save("output.png")

def land(xIndex, yIndex):
    import drawer
    drawer.img.putpixel((xIndex * 4, yIndex * 4), (0,154,23)) #better way to do this?
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4), (0,154,23))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 1), (0,154,23))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 2), (0,154,23))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 3), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (0,154,23))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (0,154,23))
    drawer.img.save("output.png")