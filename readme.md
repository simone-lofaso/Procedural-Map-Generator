start with basic map

create matrix 16x16 consisting of 0s

create image 64x64

0 on the matrix means empty, wcf has not yet reached this index

1,2,3,4... means wfc has reached this index, each number corresponds to a certain tile
ex: 1 means coast
    2 means water...

pretty easy of doing the animation is call draw on every time a new index is changed, sleep() for a quarter second, maybe less

specifics on filling matrix

pick a random point, pick a random tile
pick a random direction, choose a tile possible based on the other tile
keep doing that, this time based on lowest entropy: try moves dependant on other moves first, look for lowest num of possible moves!
if no possible move, iterate through the matrix until 0 is found, or if no 0 is found, you are done!
