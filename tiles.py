#This class will represent our pre-drawn tiles
#from PIL import Image
from asyncio.windows_events import NULL
import random

#format CURRENTTILE_NEXT_TILE CHANCE
#ex: water_ coast_chance is the chance if the current tile is water for the next tile to be coast
#these are all placeholder values, feel free to change
WATER_WATER_CHANCE = .75
WATER_COAST_CHANCE = .25
COAST_LAND_CHANCE = .75
COAST_COAST_CHANCE = .1 #incease to increase thickness of coast (i think)
COAST_WATER_CHANCE = .15
LAND_COAST_CHANCE = .25
LAND_LAND_CHANCE = .75
#these are not done yet. will need each relation for possible tiles touchin
#also the values are placeholder, feel free to change if you want to

#  1 = water
#  2 = coast
#  3 = land


if __name__ == "__main__":
    print("run wavefunctionalgo.py ya doofus")
    quit


#NEED TO IMPLEMENT CHECKING WITH BOOLEAN 3D ARRAY!!!!!!!!! DO NOT FORGET!!!
def chooseTile(xIndexDraw, yIndexDraw, xIndex, yIndex): #need more clear param names
    """ Chooses which tile should be drawn at the given location, then calls the right method to draw the specified tile.
     Index will respond to four times the location of the index. E.G. Index 0, 4 points to starting pixel 0, 16.
    

    Parameters:
        xIndex: the x Index of the current tile
        yIndex: the Y Index of the current tile
        xIndexDraw: the X index of the new tile to be drawn
        yIndexDraw: the Y index of the new tile to be drawn
    """
    import wavefunctionalgo #want to figure out how to import this at the top 
    currentTile = wavefunctionalgo.map[xIndex][yIndex]
    tiles = [1,2,3]
    
    if currentTile == 1: #we can change this to pythons equivalent of a switch statement if we update numpy and python to 3.10, but idk if im lazy enough
                         #chance for tiles next to water
        choice = random.choices(tiles, weights = (WATER_WATER_CHANCE, WATER_COAST_CHANCE, 0))
        if (choice == 1):
            water(xIndexDraw, yIndexDraw)
        elif (choice == 2): #might switch to else?
            coast(xIndexDraw, yIndexDraw)
    elif currentTile == 2: #tiles next to coast
        choice = random.choices(tiles, weights = (COAST_WATER_CHANCE, COAST_COAST_CHANCE, COAST_LAND_CHANCE,))
        if (choice == 1):
            water(xIndexDraw, yIndexDraw)
        elif (choice == 2):
            coast(xIndexDraw, yIndexDraw)
        elif (choice == 3):
            land(xIndexDraw, yIndexDraw)
    elif currentTile == 3: #chance for tiles next to land
        choice = random.choices(tiles, weight = (0, LAND_COAST_CHANCE, LAND_LAND_CHANCE))
        if (choice == 2):
            coast(xIndexDraw, yIndexDraw)
        elif (choice == 3):
            land(xIndexDraw, yIndexDraw)
    

    
    

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
    import wavefunctionalgo #avoids circular import. is this the best way to do it? Fuck you.
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4), (28,163,236)) #better way to do this?
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 1), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 2), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 3), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (28,163,236))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (28,163,236))
    wavefunctionalgo.img.save("output.png")

    wavefunctionalgo.map[xIndex][yIndex] = 1

def coast(xIndex, yIndex):
    import wavefunctionalgo
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4), (242,209, 107)) #better way to do this?
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 1), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 2), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 3), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (242,209, 107))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (242,209, 107))
    wavefunctionalgo.img.save("output.png")

    wavefunctionalgo.map[xIndex][yIndex] = 2

def land(xIndex, yIndex):
    import wavefunctionalgo
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4), (0,154,23)) #better way to do this?
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 1), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 2), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4 + 3), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 1), (0,154,23))
    wavefunctionalgo.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 3), (0,154,23))
    wavefunctionalgo.img.save("output.png")

    wavefunctionalgo.map[xIndex][yIndex] = 3