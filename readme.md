start with basic map
we should note in readme this is compiled with python 3.9, python 3.10 wont work as of 6/23. numpy doesnt suport 3.10 yet

create matrix 16x16 consisting of 0s

create image 96x96

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

#weightage
each tile has a certain percent of choosing another tile
ex: land has 20% of coast, 80% land, coast has 50% water, 50% land

coast should surround water

implement backtrack method in case a move contradicts our restraints or if no move is possible

#for each cell, bool array representing domain, all initialized true.
#tile is in the domain to be picked if its possible
#pick random tile from domain
#update domains of other cells based on picked cell from before (propagate)
#pick new tile based on lowest entropy
#if no weightage, choosing smallest domain works fine
#if weightage, use formula on https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/
