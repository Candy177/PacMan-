"""
X= wall
.=pellet
O=power up
"""
from cons import (cel_size, maze_grid_cols,maze_grid_rows,maze_lvl_start_x,maze_lvl_start_y)
maze_level_1 = [
    "XXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXX",
    "X..............................OX",
    "X.XXX.XXX.XXXXXX.XXXXXX.XXX.XXX.X",
    "X.X X.X X.X    X.X    X.X X.X X.X",
    "X.XXX.X X.XXXXXX.XXXXXX.X X.XXX.X",
    "X.....XXX.X....X.X....X.XXX.....X",
    "XXXXX.......XX.X.X.XX.......XXXXX",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX.......XXXXXXXXX.......XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX...O...XXXX.XXXX.......XXX.X",
    "X.X X.XXXXX.X  X.X  X.XXXXX.X X.X",
    "X.X X.X   X.X  X.X  X.X   X.X X.X",
    "X.X X.X   X.X  X.X  X.X   X.X X.X",
    "X.X X.XXXXX.X  X.X  X.XXXXX.X X.X",
    "X.XXX.......XXXX.XXXX...O...XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX.......XXXXXXXXX.......XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "XXXXX.......XX.X.X.XX.......XXXXX",
    "X.....XXX.X....X.X....X.XXX.....X",
    "X.XXX.X X.XXXXXX.XXXXXX.X X.XXX.X",
    "X.X X.X X.X    X.X    X.X X.X X.X",
    "X.XXX.XXX.XXXXXX.XXXXXX.XXX.XXX.X",
    "XO..............................X",
    "XXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXX"
]
def calc_maze(maze_lvl):
    walls=[]
    pellets=[]
    powerups=[]

    for row in range (maze_grid_rows):
        for col in range(maze_grid_cols):
            chara=maze_lvl[row][col]
            chara_x= maze_lvl_start_x + cel_size * col
            chara_y= maze_lvl_start_y - cel_size * row
            if chara=="X":
                walls.append((chara_x,chara_y))
            elif chara==".":
                pellets.append((chara_x,chara_y))
            elif chara=="O":
                powerups.append((chara_x,chara_y))
    return walls, pellets, powerups
         
