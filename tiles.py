import math
import random
import numpy

WATER_CHANCE = .33
COAST_CHANCE = .33
LAND_CHANCE = .34

#  1 = water
#  2 = coast
#  3 = land


if __name__ == "__main__":
    print("run wavefunctionalgo.py ya doofus")
    quit

#IF WE WANT TO ADD RULES THAT MAKE WATER CLUMP UP MORE, WE WOULD CHANGE THIS METHOD
def chooseTile(xIndex, yIndex):
    """ Chooses tile based on possible tiles
    

    Parameters:
        xIndex: the x Index of the current tile
        yIndex: the Y Index of the current tile
    """
    import wavefunctionalgo
    possibleTiles = wavefunctionalgo.mapBool[xIndex][yIndex]
    print(possibleTiles)
    if numpy.array_equiv([True, True, True], possibleTiles):
        tiles = [1,2,3]
        choice = random.choices(tiles, weights = (WATER_CHANCE, COAST_CHANCE, LAND_CHANCE))
        choice = choice[0] #random.choices returns single element list, so I get the only element from it
        if choice == 1: #not a switch statement because this was developed on python 3.9 (they came in 3.10)
            water(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
        elif choice ==  3:
            land(xIndex, yIndex)
    elif numpy.array_equiv([True, True, False], possibleTiles):
        tiles = [1,2]
        choice = random.choices(tiles, weights = (WATER_CHANCE, COAST_CHANCE))
        choice = choice[0]
        if choice == 1:
            water(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
    elif numpy.array_equiv([False, True, False], possibleTiles):
        coast(xIndex, yIndex)
    elif numpy.array_equiv([False, True, True], possibleTiles):
        tiles = [2,3]
        choice = random.choices(tiles, weights = (COAST_CHANCE, LAND_CHANCE))
        choice = choice[0]
        if choice == 2:
            coast(xIndex, yIndex)
        elif choice == 3:
            land(xIndex, yIndex)
    
#so i wanna make water and land clump together instead of being the way they are
#so probablt the best way of doing that is, if water is touching tile to be chosen, it uses a different weightage 
def getLowestEntropy():
    """Gets lowest entropy tile of map. If map is filled, then it will terminate the program.

    Returns:
        Tuple of x and y coordinates of the tile with lowest entropy. 
    
    """

    import wavefunctionalgo
    lowestEntropy = 999
    lowestEntropyTile = 999, 999
    for i in range(16):
        for j in range(16):
            if wavefunctionalgo.map[i][j] == 0:
                possibleTiles = wavefunctionalgo.mapBool[i][j]
                if numpy.array_equiv([True, True, True], possibleTiles): 
                    currentEntropy = - (WATER_CHANCE * math.log(WATER_CHANCE) + COAST_CHANCE * math.log(COAST_CHANCE) + LAND_CHANCE * math.log(LAND_CHANCE))
                elif numpy.array_equiv([True, True, False], possibleTiles):
                    currentEntropy = - (WATER_CHANCE * math.log(WATER_CHANCE) + COAST_CHANCE * math.log(COAST_CHANCE))
                elif numpy.array_equiv([False, True, True], possibleTiles):
                    currentEntropy = - (COAST_CHANCE * math.log(COAST_CHANCE) + LAND_CHANCE * math.log(LAND_CHANCE))
                elif numpy.array_equiv([False, True, False], possibleTiles):
                    currentEntropy = - (COAST_CHANCE * math.log(COAST_CHANCE))
                if currentEntropy < lowestEntropy:
                    lowestEntropy = currentEntropy
                    lowestEntropyTile = i, j
    if lowestEntropy == 999:
        print("Grid is full")
        quit()         
    return lowestEntropyTile

def water(xIndex , yIndex):
    """Draws and saves water tile to image. Also propagates information to mapBool that surrounding tiles cannot be land
    
    Parameters:
        xIndex: the x Index of the matrix 
        yIndex: the y Index of the matrix
    """
    import wavefunctionalgo #avoids circular import
    wavefunctionalgo.img.putpixel((xIndex * 4, yIndex * 4), (28,163,236)) 
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

    if xIndex + 1 < 16: #tiles surrounding cant be land
        wavefunctionalgo.mapBool[xIndex + 1][yIndex] = [True, True, False] 
    if xIndex - 1 >= 0:
        wavefunctionalgo.mapBool[xIndex - 1][yIndex] = [True, True, False]
    if yIndex + 1 < 16:
        wavefunctionalgo.mapBool[xIndex][yIndex + 1] = [True, True, False]
    if yIndex - 1 >= 0:
        wavefunctionalgo.mapBool[xIndex][yIndex - 1] = [True, True, False]

def coast(xIndex, yIndex):
    """Draws and saves coast tile to image. No propagation here because coast can be next to water and land.
    
    Parameters:
        xIndex: the x Index of the matrix 
        yIndex: the y Index of the matrix
    """
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

    #No mapbool here since adjacent pieces can be either coast or water

def land(xIndex, yIndex):
    """Draws and saves land tile to image. Also propagates information to mapBool that surrounding tiles cannot be water
    
    Parameters:
        xIndex: the x Index of the matrix 
        yIndex: the y Index of the matrix
    """
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

    if xIndex + 1 < 16:#tiles surrounding cannot be water
        wavefunctionalgo.mapBool[xIndex + 1][yIndex] = [False, True, True] 
    if xIndex - 1 >= 0:
        wavefunctionalgo.mapBool[xIndex - 1][yIndex] = [False, True, True]
    if yIndex + 1 < 16:
        wavefunctionalgo.mapBool[xIndex][yIndex + 1] = [False, True, True]
    if yIndex - 1 >= 0:
        wavefunctionalgo.mapBool[xIndex][yIndex - 1] = [False, True, True]