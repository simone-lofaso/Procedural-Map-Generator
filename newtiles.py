import math
import random
import numpy


def getLowestEntropy():
    import newwavefunction
    lowestEntropy = 999
    lowestEntropyTile = 999, 999
    for i in range(24):
        for j in range(24):
            if newwavefunction.map[i][j] == 0:
                neighbors = []
                if i + 1 < 24:
                    if newwavefunction.map[i + 1][j] > 0:
                        neighbors.append(newwavefunction.map[i + 1][j])
                if j + 1 < 24:
                    if newwavefunction.map[i][j + 1] > 0:
                        neighbors.append(newwavefunction.map[i][j +1])
                if i - 1 >= 0:
                    if newwavefunction.map[i - 1][j] > 0:
                        neighbors.append(newwavefunction.map[i - 1][j])
                if j - 1 >= 0:
                    if newwavefunction.map[i][j - 1] > 0:
                        neighbors.append(newwavefunction.map[i][j - 1])

    possibleTiles = newwavefunction.mapBool[i][j]
    if numpy.array_equiv(possibleTiles, [True, True, True, True, True]): #will only occur on first pick. Therefore all chances equal
        FLOWER_CHANCE = .20
        ROCK_CHANCE = .20
        WATER_CHANCE = .20
        COAST_CHANCE = .20
        LAND_CHANCE = .20 #technically this number will be a constant so we can get rid of all this math, however keeping us lets us change the weightage of the first tile
        currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE)

    elif numpy.array_equiv(possibleTiles, [True, True, True, True, False]):
        ROCK_CHANCE = .20 #flat percentage as rocks are not affected by grouping. Might want to move this to the top
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        LAND_CHANCE = .1
    return 0

#new choose tile will be VERY simple. Probably just needs to pass in location and then the chances from lowestEntropy
def chooseTile(xIndex, yIndex):
    import newwavefunction
    neighbors = []
    if xIndex + 1 < 24:
        if newwavefunction.map[xIndex + 1][yIndex] > 0:
            neighbors.append(newwavefunction.map[xIndex + 1][yIndex])
    if yIndex + 1 < 24:
        if newwavefunction.map[xIndex][yIndex + 1] > 0:
            neighbors.append(newwavefunction.map[xIndex][yIndex +1])
    if xIndex - 1 >= 0:
        if newwavefunction.map[xIndex - 1][yIndex] > 0:
            neighbors.append(newwavefunction.map[xIndex - 1][yIndex])
    if yIndex - 1 >= 0:
        if newwavefunction.map[xIndex][yIndex - 1] > 0:
            neighbors.append(newwavefunction.map[xIndex][yIndex - 1])
    
    possibleTiles = newwavefunction.mapBool[xIndex][yIndex]

    if numpy.array_equiv(possibleTiles, [True, True, True, True, True]):
        choice = random.randint(1, 5)
        if choice == 1:
            land(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
        elif choice == 3:
            water(xIndex, yIndex)
        elif choice == 4:
            rock(xIndex, yIndex)
        elif choice == 5:
            flower(xIndex, yIndex)

    elif numpy.array_equiv(possibleTiles, [True, True, True, False, True]):
        tileList = [1, 2, 3, 5]
        flowerWeightage = 0
        waterWeightage = 0 #rework these weightage, need possibilty of new tile to be chosen
        coastWeightage = 0
        landWeightage = 0
        for item in neighbors:
            if item == 5: #replace with switch statement if not lazy  
                flowerWeightage += .25
            elif item == 3:
                waterWeightage += .25
            elif item == 2:
                coastWeightage += .25
            else:
                landWeightage += .25
        choice = random.choices(tileList, weights = (landWeightage, coastWeightage, waterWeightage, coastWeightage))
        choice = choice[0]
        if choice == 1:
            land(xIndex, yIndex)
        elif choice == 2:
            coast(xIndex, yIndex)
        elif choice == 3:
            water(xIndex, yIndex)
        elif choice == 5:
            flower(xIndex, yIndex)





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

    newwavefunction.map[xIndex][yIndex] == 5

    newwavefunction.img.save("output2.png")

    
def rock(xIndex, yIndex):
    import newwavefunction
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (128, 132, 135)) 
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (128, 132, 135)) 
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (128, 132, 135)) 
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (128, 132, 135))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (128, 132, 135))

    newwavefunction.img.save("output2.png")

    newwavefunction.map[xIndex][yIndex] == 4

    if xIndex + 1 < 24:
        newwavefunction.mapBool[xIndex + 1][yIndex][4] = False
    if xIndex - 1 >= 0: 
        newwavefunction.mapBool[xIndex - 1][yIndex][4] = False
    if yIndex + 1 < 24:
        newwavefunction.mapBool[xIndex][yIndex + 1][4] = False
    if yIndex - 1 >= 0:
        newwavefunction.mapBool[xIndex][yIndex - 1][4] = False

def water(xIndex, yIndex):
    import newwavefunction
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (56,132,207)) 
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (56,132,207)) 
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (56,132,207)) 
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (56,132,207))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (56,132,207))

    newwavefunction.img.save("output2.png")

    newwavefunction.map[xIndex][yIndex] == 3


def coast(xIndex, yIndex):
    import newwavefunction
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (242,209, 107)) 
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (242,209, 107)) 
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (242,209, 107)) 
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (242,209, 107))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (242,209, 107))

    newwavefunction.img.save("output2.png")

    newwavefunction.map[xIndex][yIndex] == 2


    
def land(xIndex, yIndex):
    import newwavefunction
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6), (0,154,23)) 
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 1, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 2, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 3, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 4, yIndex * 6 + 5), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 1), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 2), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 3), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 4), (0,154,23))
    newwavefunction.img.putpixel((xIndex * 6 + 5, yIndex * 6 + 5), (0,154,23))

    newwavefunction.img.save("output2.png")

    newwavefunction.map[xIndex][yIndex] == 1