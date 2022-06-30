#name is temp, feel free to come up with something better. This will include main()

from PIL import Image
import numpy
import tiles 
#map matrix used for positioning and tracking whats done
map = numpy.zeros((16,16))

#map 3d array used for tracking what tiles can be put at that given location. Everything starts as true


mapBool = numpy.array([[[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       [[True,True,True], [True,True,True],[True,True,True],[True,True,True],[True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True], [True,True,True]]
                       ])
                       
img = Image.new('RGB', (64, 64 ))
img.save('output.png')
tiles.water(0,0)
tiles.coast(0,1)
tiles.land(0,2)



img.show








