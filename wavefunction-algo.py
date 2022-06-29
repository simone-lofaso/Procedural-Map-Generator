#name is temp, feel free to come up with something better. This will include main()

from PIL import Image
import numpy
import tiles 

matrix = numpy.zeros((16,16))
img = Image.new('RGB', (64, 64 ))
img.save('wtf.png')
tiles.water(0,0)

img.show








