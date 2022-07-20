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


               
img = Image.new('RGB', (64, 64 ))
img.save('output.png')
img.show

#time.sleep(5) #for me to record it runnin
done = False #will be true if no zeroes remaining

while not done:
    xIndex, yIndex = tiles.getLowestEntropy()
    print(xIndex, yIndex)
    tiles.chooseTile(xIndex, yIndex)
    #img.show
    #time.sleep(0.5)

img.show
   














