import math
import random
import numpy

#all possible done
#FLOWER
#no flower done  [True, True, True, True, False]
#no water, no flower done [True, True, False, True, False]
#no land, no flower [False, True, True, True, False]
#no land, no water, no rock, no flower [False, True, False, False, False]

#ROCK DONE
#no rock done   [True, True, True, False, True]
#no rock, no flower done [True, True, True, False, False]
#no rock, no land, done  [False, True, True, True, False, True]
#no rock, no land, done no flower [False, True, True, False, False]
#no rock, no water done [True, True, False, False, True]
#no rock, no water, no flower done [True, True, False, False, False]

#WATER


#LAND
#No land, No rock[False, True, True, False, True]
#No land, no water [False, True, False, True, True]
#No land, no water, no rock #[False, True, False, False, True]
#No land, no water, no flower #[False, True, False, True, False]


def getLowestEntropy():
    """
    Gets lowest entropy of all tiles on the board. Used to find the next piece to fill

    
    
    """
    import newwavefunction
    lowestEntropy = 999
    lowestEntropyTile = 999, 999
    FLOWER_CHANCE = 0
    ROCK_CHANCE = 0
    WATER_CHANCE = 0
    COAST_CHANCE = 0
    LAND_CHANCE = 0
    
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
    if numpy.array_equiv(possibleTiles, [True, True, True, True, True]): #will only occur on first pick. Therefore all chances equal. Switch statement could also be used here
        FLOWER_CHANCE = .20 
        ROCK_CHANCE = .20 
        WATER_CHANCE = .20
        COAST_CHANCE = .20
        LAND_CHANCE = .20 #technically this number will be a constant so we can get rid of all this math, however keeping us lets us change the weightage of the first tile
    
    #Entropy when flower is impossible 
    elif numpy.array_equiv(possibleTiles, [True, True, True, True, False]):
        ROCK_CHANCE = .20 #flat percentage as rocks are not affected by grouping. Might want to move this to the top
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 3: #water
                WATER_CHANCE += .125
            elif tile == 2: #coast
                COAST_CHANCE += .125
            elif tile == 1:
                LAND_CHANCE += .125
    
    #Entropy when rock is impossible           
    elif numpy.array_equiv(possibleTiles, [True, True, True, False, True]):
        FLOWER_CHANCE = .1
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .15
            elif tile == 3:
                WATER_CHANCE += .15
            elif tile == 2:
                COAST_CHANCE += .15
            elif tile == 1:
                LAND_CHANCE += .15

    #Entropy when flower and rock are impossible
    elif numpy.array_equiv(possibleTiles, [True, True, True, False, False]):
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 3:
                WATER_CHANCE += .175
            elif tile == 2:
                COAST_CHANCE += .175
            elif tile == 1:
                LAND_CHANCE += .175
    #Entropy when land and rock are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, True, True, False, True]):
        FLOWER_CHANCE = .1 
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .175
            elif tile == 3:
                WATER_CHANCE += .175
            elif tile == 2:
                COAST_CHANCE += .175
       
    #Entropy when rock, land, and flower are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, True, False, False]):
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 3:
                WATER_CHANCE += .2
            elif tile == 2:
                COAST_CHANCE += .2
    
    #Entropy when rock and water are impossible
    elif numpy.array_equiv(possibleTiles, [True, True, False, False, True]):
        FLOWER_CHANCE = .1
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .175
            elif tile == 2:
                COAST_CHANCE += .175
            elif tile == 1:
                LAND_CHANCE += .175
    
    #Entropy when rock, water, and flower are impossible
    elif numpy.array_equiv(possibleTiles, [True, True, False, False, False]):
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 2:
                COAST_CHANCE += .2
            elif tile == 1:
                LAND_CHANCE += .2
     
    #Entropy when flower and water are impossible
    elif numpy.array_equiv(possibleTiles, [True, True, False, True, False]):
        ROCK_CHANCE = .2
        COAST_CHANCE = .1
        LAND_CHANCE = .1
        for tile in neighbors:
            if tile == 2:
                COAST_CHANCE += .15
            elif tile == 1:
                LAND_CHANCE += .15
    
    #Entropy when water, rock, land, and flower are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, False, False, False]):
        COAST_CHANCE = 1
        
#LAND
#No land, No rock done[False, True, True, False, True]
#No land, no water done [False, True, False, True, True]
#No land, no water, no rock done [False, True, False, False, True]
#No land, no water, no flower done [False, True, False, True, False]

#adding percentage will be percentage left from flat chance / 4
#flat chance = flower + water + coast = .3
#(1 - .3) / 4 = .175

    #When land and rock are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, True, False, True]):
        FLOWER_CHANCE = .1
        WATER_CHANCE = .1
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .175
            elif tile == 3:
                WATER_CHANCE += .175
            elif tile == 2:
                COAST_CHANCE += .175
                
    #When land and water are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, False, True, True]):
        FLOWER_CHANCE = .1
        ROCK_CHANCE = .2
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .2
            elif tile == 2:
                COAST_CHANCE += .2
                
    #When land, water, and rock are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, False, False, True]):
        FLOWER_CHANCE = .1
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 5:
                FLOWER_CHANCE += .2
            elif tile == 2:
                COAST_CHANCE += .2
                
    #When land, water, and flower are impossible
    elif numpy.array_equiv(possibleTiles, [False, True, False, True, False]):
        ROCK_CHANCE = .2
        COAST_CHANCE = .1
        for tile in neighbors:
            if tile == 2:
                COAST_CHANCE += .175
    
    else:
        print("Error: Scenario unnacounted for")
        print(newwavefunction.mapBool[i][j])            
        
    if (FLOWER_CHANCE == 0 or ROCK_CHANCE == 0 or WATER_CHANCE == 0 or COAST_CHANCE == 0 or LAND_CHANCE == 0):
        currentEntropy = - ( math.log(FLOWER_CHANCE) * FLOWER_CHANCE + math.log(ROCK_CHANCE) * ROCK_CHANCE + math.log(WATER_CHANCE) * WATER_CHANCE + math.log(COAST_CHANCE) * COAST_CHANCE + math.log(LAND_CHANCE) * LAND_CHANCE)    
    else:
        currentEntropy = 999
    
    if currentEntropy == 999:
        print("Map is complete!")
        quit()
        
    return FLOWER_CHANCE, ROCK_CHANCE, WATER_CHANCE, COAST_CHANCE, LAND_CHANCE, i, j

#new choose tile will be VERY simple. Probably just needs to pass in location and then the chances from lowestEntropy
def chooseTile(xIndex, yIndex, FLOWER_CHANCE, ROCK_CHANCE, WATER_CHANCE, COAST_CHANCE, LAND_CHANCE):
    #takes in these params (location and weightage for each tile) and uses method below to randomly pick from list of tiles
    tileList = [1, 2, 3, 4, 5]
    
    
    choice = random.choices(tileList, weights = (LAND_CHANCE, COAST_CHANCE, WATER_CHANCE, ROCK_CHANCE, FLOWER_CHANCE))
    choice = choice[0]

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
    
    if xIndex + 1 < 24:
        newwavefunction.mapBool[xIndex + 1][yIndex][3] = False
    if xIndex - 1 >= 0: 
        newwavefunction.mapBool[xIndex - 1][yIndex][3] = False
    if yIndex + 1 < 24:
        newwavefunction.mapBool[xIndex][yIndex + 1][3] = False
    if yIndex - 1 >= 0:
        newwavefunction.mapBool[xIndex][yIndex - 1][3] = False

    
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
    
    if xIndex + 1 < 24:
        newwavefunction.mapBool[xIndex + 1][yIndex][1] = False
        newwavefunction.mapBool[xIndex + 1][yIndex][5] = False
    if xIndex - 1 >= 0: 
        newwavefunction.mapBool[xIndex - 1][yIndex][1] = False
        newwavefunction.mapBool[xIndex - 1][yIndex][5] = False
    if yIndex + 1 < 24:
        newwavefunction.mapBool[xIndex][yIndex + 1][1] = False
        newwavefunction.mapBool[xIndex][yIndex + 1][5] = False
    if yIndex - 1 >= 0:
        newwavefunction.mapBool[xIndex][yIndex - 1][1] = False
        newwavefunction.mapBool[xIndex][yIndex - 1][5] = False


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
    
    if xIndex + 1 < 24:
        newwavefunction.mapBool[xIndex + 1][yIndex][3] = False
    if xIndex - 1 >= 0: 
        newwavefunction.mapBool[xIndex - 1][yIndex][3] = False
    if yIndex + 1 < 24:
        newwavefunction.mapBool[xIndex][yIndex + 1][3] = False
    if yIndex - 1 >= 0:
        newwavefunction.mapBool[xIndex][yIndex - 1][3] = False

    newwavefunction.map[xIndex][yIndex] == 1