#This class will represent our pre-drawn tiles
#from PIL import Image
from asyncio.windows_events import NULL
from cmath import log
import math
import random
from turtle import pos

#format CURRENTTILE_NEXT_TILE CHANCE
#ex: water_ coast_chance is the chance if the current tile is water for the next tile to be coast
#these are all placeholder values, feel free to change
WATER_CHANCE = .4
COAST_CHANCE = .2
LAND_CHANCE = .4
#these are not done yet. will need each relation for possible tiles touchin
#also the values are placeholder, feel free to change if you want to

#  1 = water
#  2 = coast
#  3 = land


if __name__ == "__main__":
    print("run wavefunctionalgo.py ya doofus")
    quit


#NEED TO IMPLEMENT CHECKING WITH BOOLEAN 3D ARRAY!!!!!!!!! DO NOT FORGET!!!
def chooseTile(xIndex, yIndex): #need more clear param names
    """ FINISH DESCRIPTION
    

    Parameters:
        xIndex: the x Index of the current tile
        yIndex: the Y Index of the current tile
    """
    import wavefunctionalgo #want to figure out how to import this at the top 
    possibleTiles = wavefunctionalgo.mapBool[xIndex][yIndex]
    if possibleTiles == [True, True, True]:
        tiles = [1,2,3]
        choice = random.choices(tiles, weights = (WATER_CHANCE, COAST_CHANCE, LAND_CHANCE))
        if choice == 1: #not a switch statement because this was developed on python 3.9 (they came in 3.10)
            water(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
        elif choice ==  3:
            land(xIndex, yIndex)
    elif possibleTiles == [True, True, False]:
        tiles = [1,2]
        choice = random.choices(tiles, weights = (WATER_CHANCE, COAST_CHANCE))
        if choice == 1:
            water(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
    elif possibleTiles == [False, True, False]:
        coast(xIndex, yIndex)
    elif possibleTiles == [False, True, True]:
        tiles = [2,3]
        choice = random.choices(tiles, weights = (COAST_CHANCE, LAND_CHANCE))
        if choice == 2:
            coast(xIndex, yIndex)
        elif choice == 3:
            land(xIndex, yIndex)
    
#iterate through map matrix
#if not 0, get neighboring cell tiles and find entropy using their weightage
#if surrounding bits dont have tiles, use mapBool to determine entropy
#return list of equal entropy (unlikely to be one but), then choose a random one
def getLowestEntropy():
    import wavefunctionalgo
    import random
    lowestEntropy = 999
    currentEntropy = 0
    lowestEntropyTiles = []
    for i in range(16):
        for j in range(16):
            if wavefunctionalgo.map[i][j] != 0: #checking to see if neigboring tile is water. if yes it will be more likely to choose it
                possibleTiles = wavefunctionalgo.mapBool[i][j]
                if possibleTiles == [True, True, True]: 
                    currentEntropy = - (WATER_CHANCE * math.log(WATER_CHANCE) + COAST_CHANCE * math.log(COAST_CHANCE) + LAND_CHANCE * math.log(LAND_CHANCE))
                elif possibleTiles == [True, True, False]:
                    currentEntropy = - (WATER_CHANCE * math.log(WATER_CHANCE) + COAST_CHANCE * math.log(COAST_CHANCE))
                elif possibleTiles == [False, True, True]:
                    currentEntropy = - (COAST_CHANCE * math.log(COAST_CHANCE) + LAND_CHANCE * math.log(LAND_CHANCE))
                elif possibleTiles == [False, True, False]:
                    currentEntropy = - (COAST_CHANCE * math.log(COAST_CHANCE))
                if currentEntropy < lowestEntropy:
                    lowestEntropy = currentEntropy
                    lowestEntropyTiles = []
                if currentEntropy == lowestEntropyTiles:
                    lowestEntropyTiles.append([i, j])

    if lowestEntropyTiles != 1: #can prob clean this up
        i = random.randint(lowestEntropyTiles.len())
        return lowestEntropyTiles[i]
    else: return lowestEntropyTiles[0]

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

    wavefunctionalgo.mapBool[xIndex + 1][yIndex] == [True, True, False] #tiles surrounding cannot be land
    wavefunctionalgo.mapBool[xIndex - 1][yIndex] == [True, True, False]
    wavefunctionalgo.mapBool[xIndex][yIndex + 1] == [True, True, False]
    wavefunctionalgo.mapBool[xIndex][yIndex - 1] == [True, True, False]

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

    #No mapbool here since adjacent peices can be either coast or water

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

    wavefunctionalgo.mapBool[xIndex + 1][yIndex] == [False, True, True] #tiles surrounding cannot be water
    wavefunctionalgo.mapBool[xIndex - 1][yIndex] == [False, True, True]
    wavefunctionalgo.mapBool[xIndex][yIndex + 1] == [False, True, True]
    wavefunctionalgo.mapBool[xIndex][yIndex - 1] == [False, True, True]