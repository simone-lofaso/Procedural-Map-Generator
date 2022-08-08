import numpy
from PIL import Image
import tiles
import time

#matrix used to see if a tile has been placed or not
map = numpy.zeros((24,24))



"""
3d array used for tracking what tiles can be put at that given location. Everything starts as true
#1 is land
#2 is coast
#3 is water
#4 is rock
#5 is flower
"""
mapBool = numpy.array([[[True, True, True, True, True], [True, True, True, True, True] ,[True, True, True, True, True] ,[True, True, True, True, True] ,[True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]], 
                       [[True, True, True, True, True], [True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False],[True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, False], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True] ,[True, True, True, True, True] ,[True, True, True, True, True] ,[True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True ] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True] , [True, True, True, True, True]]
                       ])


               
img = Image.new('RGB', (144, 144))

img.save('output.png')
img.show
time.sleep(2)
while True:
    FLOWER_CHANCE, ROCK_CHANCE, WATER_CHANCE, COAST_CHANCE, LAND_CHANCE, xIndex, yIndex = tiles.getLowestEntropy()
    tiles.chooseTile(xIndex, yIndex, FLOWER_CHANCE, ROCK_CHANCE, WATER_CHANCE, COAST_CHANCE, LAND_CHANCE)
    img.show
    time.sleep(.2)

