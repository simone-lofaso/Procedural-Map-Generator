#name is temp, feel free to come up with something better. This will include main()

from PIL import Image
import numpy
import tiles 
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
tiles.water(0,0)
tiles.coast(0,1)
tiles.land(0,2)



img.show








