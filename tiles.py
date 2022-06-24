#This class will represent our pre-drawn tiles

import drawer

def chooseTile(tile, xIndex, yIndex): #idk if im stupid or not but i cant remember how to only accept ints here
    """ Chooses which tile should be drawn at the given location, then calls the right method to draw the specified tile

    Parameters:
        tile: The tile number designated to be drawn. 1 for water, 2 for blah blah blah


    """
    if (tile == 1): #NOT A GOOD WAY OF DOING THIS but python has no switch statements until 3.10, which doesnt work with numpy right now.
        water(xIndex, yIndex)
    elif (tile == 2):
        coast(xIndex, yIndex)
        



def water(xIndex , yIndex):
    drawer.img.putpixel((xIndex * 4, yIndex * 4), (28,163,236)) #better way to do this?
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4, yIndex * 4 + 3), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 3), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 1, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 1), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 3, yIndex * 4 + 2), (28,163,236))
    drawer.img.putpixel((xIndex * 4 + 2, yIndex * 4 + 3), (28,163,236))

def coast(xIndex, yIndex):
    print("Durr i havent done this yet")