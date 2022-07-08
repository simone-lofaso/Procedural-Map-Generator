#name is temp, feel free to come up with something better. This will include main()

from PIL import Image
import numpy
import tiles
import time 
#map matrix used for positioning and tracking whats done
map = numpy.zeros((16,16))

#map 3d array used for tracking what tiles can be put at that given location. Everything starts as true

mapBool = numpy.array([[[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]],
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       ])

#NOTES FOR MAIN 

#First, pick random cell
#Then, pick random tile
#pick random tile next to tile, then pick tile there, propogate new constraints to neighboring cells
#find lowest entropy in matrix, basically we want to use mapbool and find the least amount of trues
# https://youtu.be/20KHNA9jTsE?t=435 

                       
img = Image.new('RGB', (64, 64 ))
img.save('output.png')
img.show

#time.sleep(5) #for me to record it runnin
done = False #will be true if no zeroes remaining

while not done:
    xIndex, yIndex = tiles.getLowestEntropy()
    print(xIndex, yIndex)
    tiles.chooseTile(xIndex, yIndex)
    img.show
    #time.sleep(0.5)
    done = True
    for i in range(16): #can probably just make it so if getLowestEntropy() returns default value it stops, saves 1000+ checks
        for j in range(16):
            if map[i][j] != 0:
                done = False














