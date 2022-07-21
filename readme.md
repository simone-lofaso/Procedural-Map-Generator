new tile: Rock
    Does not together and can touch land but not coast / water

new tile: flower
    Can only occur when surrounded by less than 4 tiles (on the edge of map)
    can touch land, rock, coast, flower (if not edge)

new tile size: 6x6

choose tile function
    get tile to left, if left doesnt work, get tile above, if doesnt work get tile below
    compare size of arrays of number of certain type next to piece
        if 3 land touching, 1 coast touching, 3 is more than 1 so land will be more likely (possibly 3x more likely)
        each tile accounts for 25% weightage, 3 land 1 coast means 75% land, 25% chance coast

#STILL NEED TO UPDATE MAPBOOL SOMEWHERE
determine what can be placed during getLowestEntropy method, then update mapBool

update third array when updating mapbool, for example
if rock is placed, update [xIndex][yIndex][4] to be false for surrounding tiles