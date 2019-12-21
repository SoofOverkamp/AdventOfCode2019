import string
from collections import deque

from itertools import repeat

from graphing import *
from print_2d import String2DBuilder
_data = '''                                         J           W         D   K     J       P   R   M                                             
                                         I           O         E   I     K       W   T   H                                             
  #######################################.###########.#########.###.#####.#######.###.###.###########################################  
  #...#.....#.....#.#.......#.......#.#.#.....#.........#.......#.#...#.........#...#...#...............#.....#.#...#.........#.#.#.#  
  ###.#.###.#####.#.#.###########.#.#.#.###.#####.###.#.#####.###.###.#########.###.#.#.#####.#.#####.#####.###.#.#######.#.###.#.#.#  
  #...#...#.......#.......#.......#.............#.#.#.#.#...#.....#.#.....#.......#...#.#...#.#.#...#.#...#...#.#...#...#.#.........#  
  ###.###.#.#.#.#####.#################.#.#######.#.#####.#.###.###.#.#.###.#######.###.#.#.###.#.#####.###.###.#.###.#####.#########  
  #.#...#.#.#.#.#.#.#.#.#...#.......#.#.#.....#.......#...#.....#...#.#.#...#...#...#...#.#.........#...#...#.#.....#.#...#...#...#.#  
  #.###.#######.#.#.#.#.###.#######.#.#.#####.###.###.###.#########.###.#.###.#.#####.###.#######.###.###.###.#.#####.#.###.###.###.#  
  #.....#...#.#.......#...#...#.#.....#.#...#...#...#...#.......#.#.....#.....#.#.......#.#.....#.........#.#.......#.#.#...........#  
  #####.#.###.#######.###.###.#.#####.###.#####.#.###.#######.###.###.###.#.###.#.#.#.###.###.#####.#.###.#.#.#######.#.#.###.#######  
  #...#...#...#.......#...............#.....#...#.#.....#.........#.....#.#.#.#.#.#.#.#...#.....#...#...#...................#.#.#...#  
  ###.#.#####.###.###.###.#.###.###.#.#.#.#.#.###.#.###.###.###.#.#####.#####.#.#.###.###.#.###.#####.#.#.#######.#######.###.#.#.###  
  #...#.#.#.......#.......#.#.....#.#...#.#.#...#.#.#...#.....#.#.#.#...#.....#.#...#.#...#.#...#.#.#.#.#.....#.#.....#.#.#...#...#.#  
  #.###.#.#############.###.#.#.#.#######.#.#.#########.#.###.#####.#.###.###.#.#.#######.#.#.###.#.#####.###.#.#######.#######.###.#  
  #.....#...#.......#.....#.#.#.#.#...#...#.....#.......#.#.......#.....#...#...#...#...#.#.#...........#.#.#...........#...#.......#  
  #####.#.#####.#.###################.###.#############.#.#####.#######.###.#####.#####.#.#.###.###.#.#.###.###.###.#.#.###.#.#######  
  #.#.....#.#.#.#.....#.#...#...#...............#.....#.#.#...#.#.#.#.#.#.....#.....#.#.......#.#.#.#.#.....#.....#.#.#.#.......#.#.#  
  #.#####.#.#.###.###.#.###.#.#############.#.#.#.###.#.#.#.#####.#.#.#.###.#######.#.#.#.###.#.#.###.#####.###.#######.#####.###.#.#  
  #.#...#.....#.....#.#...........#.#.#.#.#.#.#.#.#.#.#.#.........#.......#.#.#.....#...#...#.#.#.#.#.....#.#.#.......#...#.#.#.....#  
  #.#.###.#######.#######.#.###.###.#.#.#.#.#######.#.#.#.###.#.#######.###.#.###.#######.#####.#.#.#########.#.#.#########.#.#####.#  
  #...#.......#.........#.#.#.....#.........#...#.#.....#.#...#...#.....#.......#.......#.#...#...........#.#.#.#.#.....#.#.#.......#  
  ###.###.###.#.###.#.#######.#####.#####.#####.#.###.#.#.#####.#######.###.#########.#.#####.#.#####.#####.#.#####.#####.#.#.#######  
  #...#...#.#.#...#.#.#...........#.#...............#.#.#.....#.#.#.....#...#...#.....#...#.......#.#.#.......#.....#.#.#...#.......#  
  ###.###.#.###.###.#########.###.###.#.#.#############.#.###.###.#####.#.###.###.#.#########.#.###.#########.#.#####.#.###.#.#######  
  #...#.#.#.#.....#.#.....#.....#.....#.#.#...#...#.....#.#.#...#.....#.#.......#.#.#...#.#...#.#...#.#.#.#.........#.#.#.#.....#...#  
  ###.#.#.#.#.###########.#########.#####.#.#####.#####.###.#.###.#.###.#.#.#######.#.#.#.###.#.#.###.#.#.###.#######.#.#.###.###.#.#  
  #.#.........#...#.........#.....#...#.#...#...#.....#.#.......#.#.#...#.#.....#.....#.....#.#.......#.....#...#.#.#.....#.......#.#  
  #.###.###.#####.#######.#####.#.#.###.#.#.#.#####.###.#.#########.#.#######.#########.#.#####.###.#.#.#.###.###.#.#.#######.#######  
  #.....#.#.#.....#.#...#.....#.#...#.....#.....#.#.#...#.....#.#.#.#.#.......#.......#.#...#...#.#.#.#.#...#...#...#.......#.......#  
  #.###.#.#####.###.#.#######.#########.###.#####.#.###.#.#.###.#.#.#.###.###.###.###.#.#######.#.#####.#####.###.###.###.###.#.#####  
  #.#.......#.#.....#...#.#...#.#.......#.......#...#...#.#.......#.#...#...#.#.#.#...#.#.................#.#.#.#.......#.#...#.#.#.#  
  #####.#####.#.#####.###.###.#.#######.#####.###.#.#.#######.#####.###.#.#.###.#.#.###.#.#.#####.###.#####.#.#.#.#########.#.###.#.#  
  #.........#.......#.#.#.........#.....#...#.#.#.#...#.....#...#.......#.#...#...#.....#.#.....#.#.#.#...#.#...#.........#.#.#.#.#.#  
  #.#.#.#####.#######.#.#.#####.#######.#.###.#.#.#######.#####.#.###.#.###.#####.###.#.#######.#.#.#####.#.#.###.#.#########.#.#.#.#  
  #.#.#...#...#...#.#...#.#.#.....#...#.#.......#.....#.........#...#.#.#.......#...#.#.....#...#.....#...........#...#...#...#.#...#  
  #####.#.#.#.#.###.#.#####.###.###.#####.#######.#######.#######.#############.#.#.#########.#####.#####.###.###########.#.#.#.#.###  
  #.....#.#.#.#.........#.#.....#...#    T       G       S       B             E Q S         R    #...#...#...#.....#...#.#.#.#.#...#  
  #####.#####.#######.###.###.###.###    J       M       G       O             V Z W         T    ###########.###.###.###.###.#.#.###  
  #...........#...........#...#.....#                                                             #...#...#.#.....#...#.....#.......#  
  ###.#######.#.#####.###.###.###.#.#                                                             #.#####.#.###.#####.###.#######.###  
SG..#.......#.......#...#.#.....#.#..RK                                                           #...#.#.....#.#.#.....#.......#.#.#  
  #.#######.###.#.#######.#.#.#.###.#                                                             #.###.###.###.#.#.#####.#######.#.#  
  #.......#.#...#.#...#...#.#.#...#.#                                                             #...#.#...#.#...........#...#......SW
  #.###.#.#.#######.###.#.#.#.#.#.#.#                                                             #.###.###.#.#.###.#.###.###.#####.#  
  #...#.#.......#.#...#.#...#.#.#...#                                                           RX....#...#.....#...#...#.....#...#.#  
  ###.###.#.#####.###.###########.###                                                             #.#####.#.#####.#######.###.###.#.#  
  #.#.#.#.#.#.#...#.........#.#.#.#.#                                                             #.#.#...#.#.#.#.#...#.#.#...#.....#  
  #.###.#####.#.#######.###.#.#.###.#                                                             #.#.#.#.#.#.#.#####.#.#####.#.###.#  
ZN........#.......#.#...#.#.#...#....MH                                                           #.....#.....#...#...#.#...#...#...#  
  #.#########.#.###.#.###.#.#.#.###.#                                                             #############.###.###.###.#########  
  #...#...#.#.#...#...#.#...#.#...#.#                                                           DE....#...#...#...#.................#  
  #.#####.#.###.#.#.#.#.#.###.###.#.#                                                             #.#.#.#.#.#.#.#.#.###.###.#####.#.#  
  #.............#...#...#.....#.....#                                                             #.#.#.#...#.#.#...#...#.....#...#.#  
  ###################################                                                             ###.#.#####.#.###.#########.#####.#  
  #.......#.................#.......#                                                             #...#.#.....#.#.#...#.....#.#.#....ZZ
  #.#####.#.#####.#.#.###.###.###.#.#                                                             ###.#.#.#####.#.###.#.#######.#.###  
  #.#.........#...#.#.#.#...#.#...#.#                                                             #.....#.........#...#...#..........HL
  #.#######.#####.#####.###.#.#.#####                                                             ###.###.###############.#######.#.#  
  #.....#.#...#...#.........#.#.#....KI                                                           #...#...#...........#.#.......#.#.#  
  #.#.###.#.###.#######.#####.#.###.#                                                             #####.###.###.###.###.###.###.#####  
RX..#.#.#.#.#...#.#...........#.....#                                                             #.#.#.#.....#.#.....#.#...#.....#.#  
  ###.#.#.#######.#.#.#####.#.#.#.#.#                                                             #.#.#####.#########.#.###.#.#####.#  
  #.#.#...#...#.#.#.#.#.#.#.#.#.#.#.#                                                           XK....#.......#.....#.#.....#.#......RK
  #.###.#.###.#.#.#####.#.###.#######                                                             ###.#.#.###.###.###.#.#.###.###.###  
BO....#.#.#.....#...#.......#.#.#...#                                                             #.....#.#.#...#.#.#...#...#.....#.#  
  #.#.#.#.###.###.###.#########.#.###                                                             #########.#####.#.#.###.###.#.#.#.#  
  #.#.#.#.#.#...#...#.....#.#...#....WO                                                         UJ......#.#.........#.#.#.#.#.#.#...#  
  ###.#.#.#.#.#.#.#.#.#.###.###.#.###                                                             #####.#.###.###.###.#.###.###.#####  
  #.....#.....#...#...#.............#                                                             #.....#.#.....#...#.#...#...#.#.#.#  
  #####.#####.###########.###.###.###                                                             ###.###.#####.#.#.###.#.#.#####.#.#  
  #...#.#...#.#...#.....#...#.#.....#                                                             #.#...#.....#.#.#...#.#.#.#.#......IT
  #.#.###.#.###.#.###.#.###.#######.#                                                             #.###.#.#.###.#.#######.#.#.#####.#  
  #.#...#.#.#...#.#.#.#.#.#.#.#...#.#                                                             #...#...#.....#...................#  
  #.#.#.#.#.#.###.#.#.#.#.#.#.#.#.###                                                             ###.###############################  
YD..#.#...#...#...#...#.#.#.#...#.#.#                                                             #.............................#...#  
  #.#####.#####.###.#.###.#####.###.#                                                             ###.###.#####.#.#.#####.#####.#.#.#  
  #.#.....#...#.....#................ZN                                                         YD..#...#...#...#.#...#.#.#...#.#.#..ST
  ###########.#####.#.#.#.###.#.#####                                                             #.#.###.###.#.#.###.#.###.#.#.#.###  
XK....#...#.......#.#.#.#.#.#.#.#...#                                                             #.#...#.#.#.#.#...#...#...#...#...#  
  #.#.#.#.#.###.#.###.###.#.#######.#                                                             #.#.#.###.###########.###.#####.###  
  #.#...#.....#.#.#.#.#.#.#...#.....#                                                             #...#...#...#...#.#.#...#.........#  
  #.###########.###.#.#.###.#.###.#.#                                                             #########.#####.#.#.#########.#.###  
  #.#...........#.#.#.#.....#...#.#.#                                                           HL..#...#.......#.....#.......#.#.#..GM
  #.#.###.#######.#.###.#######.#.#.#                                                             #.#.#.###.###.#.###.#.#####.#####.#  
  #.#.#...................#.#.....#..JK                                                           #...#.#.#...#.#...#.....#.#.#.#.#.#  
  #.#####.#############.###.#########                                                             ###.###.###.#.#.###.#####.#.#.#.#.#  
  #.#...#.#.#.#.......#.#.#...#.....#                                                             #...#.....#.#.....#...#.....#.....#  
  #####.###.#.#.#.#.#.###.#.#.###.###                                                             #.###.#.###.###.###.#.###.###.###.#  
  #.#.#.........#.#.#...#...#.......#                                                             #.....#.......#.#...#.#.......#...#  
  #.#.#.#####.#.###.###.#.#######.#.#                                                             #.#######.###.#####.###.#####.#####  
JO........#...#...#.#...#.....#...#.#                                                             #...#.......#...#...#...#.....#...#  
  #####.###.#######.###.###.###.#.#.#                                                             #.#.#######.#.#.#######.###.#.#.#.#  
  #.......#...#.......#.....#.#.#.#..ST                                                           #.#.....#...#.#.#.........#.#...#.#  
  ###.#########.#.#.###.#.###.#####.#                                                             ###.#.###.#.#######.#######.#######  
  #...........#.#.#...#.#...#...#.#.#                                                             #...#.#...#...#.#...#.#.......#...#  
  #######.#######.#.#####.#####.#.#.#            P       Z         J       I   J           A      #.#.#####.###.#.#.###.###.###.#.###  
  #.........#...#.#.#.......#.#.....#            W       A         I       T   O           E      #.#...#...#.....#.#.......#.......#  
  #.###.###.#.#.#######.#.###.#.###.#############.#######.#########.#######.###.###########.#############.#######.#######.#.#.###.#.#  
  #.#...#...#.#...#.....#.....#.#.........#.......#.#.....#.#.#.#...#.#.......#.....#.#.#.#...#...#...#.....#...#.....#...#.#...#.#.#  
  #.#.#####.#####.#####.###.#######.#######.###.###.#.#####.#.#.###.#.#.###########.#.#.#.#.###.###.#########.###.#.###.###.###.#.###  
  #.#...#.....#.#.#.#.#...#.#.#.........#...#.....#.........#.#...#.#...#...#.....#...#.#.#.........#.#.........#.#...#.#.....#.#...#  
  #.#####.#####.#.#.#.#.###.#.#.###.#####.#.#####.###.#.###.#.#.#.#.#.#.#.#.#.###.#.###.#.#.###.#.###.#.###########.#####.#.#####.#.#  
  #.#.#.....#.............#.#...#.#.....#.#.#...#.#.#.#...#.#...#...#.#.#.#.#.#.#.#...#.......#.#...#.........#.#.#...#...#.....#.#.#  
  ###.#.#.###.#.###.#.###.#.#.###.#.###.#.#.#.###.#.###.#.#.#.#######.###.#.#.#.#.#.###.###.#.#######.###.#####.#.#.#######.#####.###  
  #.....#.#...#.#...#.#.#.#.#.#.....#...#.#.#.........#.#.#.#.#.#.........#.#.#.......#.#.#.#...#...#.#.#.#.#.........#.#.......#.#.#  
  #.###.#######.#.#.###.#.#####.#.#.#######.#.#.#.#.#######.#.#.#.#.#######.#.#########.#.#########.#.#.###.###.#.#.#.#.###.#.###.#.#  
  #.#...#.....#.#.#.#.........#.#.#.....#...#.#.#.#.#...#...#.#.#.#.#.......#.....#.....#...#...#...........#...#.#.#.....#.#...#...#  
  #####.###.#.#####.#.#.###.###.#.#.#.#############.###.###.#.#.#.###.#.#########.###.#.#.#.###.#.#######.###.#####.###.###.#######.#  
  #.....#.#.#.......#.#.#.#...#.#.#.#.....#.....#.......#.#.#...#.#...#.#...#.......#.#...#...........#.#.#.....#.....#.#...#...#.#.#  
  ###.#.#.#.###.###.#####.#####.#####.#######.#####.#####.#.#.#####.#.###.#.###.###########.###.#####.#.#######.###.#####.#.###.#.#.#  
  #...#...#...#.#...#.......#.#.#.#...#...............#.....#.#.#.#.#.....#.#.....#.........#.......#.......#...#.......#.#.......#.#  
  #.#####.#.###.#.#.###.#.#.#.#.#.###############.#.#######.#.#.#.#.#######.###.#.#####.#######.#.#.#.#.#.#####.#.#.###.###.#.#####.#  
  #.#.....#.#...#.#.#.#.#.#.......#.#...#.....#...#.#.#.....#.....#.#.......#...#.#.....#.#.#.#.#.#.#.#.#.#.#.#.#.#...#.#...#.#...#.#  
  #.#####.#####.#####.###.#########.###.###.#######.#.#.###.#.###########.#####.#.###.#.#.#.#.#######.#####.#.#####.#.#.###.###.#####  
  #.....#.#.......#.......#.....#.......#...#...#...#.#.#...#.....#.#.......#.#.#...#.#.........#.#.#...#.#.......#.#.#.#.......#...#  
  #####.#######.#######.#######.#######.###.#.#####.#.#####.#.#.###.#######.#.###.###.###.###.###.#.#####.#.#.#####.#.#.#.#.#.#.###.#  
  #.....#.............#.#.#.#...#...#.....#...#.......#.....#.#...#.#.....#...#.#...#.#...#.................#.#.#.#.#.#.#.#.#.#.....#  
  #.###.#####.#.###.#####.#.###.#.#######.###.###.#.#######.#.#####.#.#.###.###.#.###.#######.#.#.#.#####.#####.#.#####.#####.#####.#  
  #.#...#.....#.#.#.#...#...#.....#.#...#.#.#...#.#.......#.#...#.#.#.#.#.#.#.#.....#...#.#.#.#.#.#.....#.#.#.....#.#...#.#.......#.#  
  #.#.#.#####.###.#####.###.###.#.#.#.###.#.#.#.#.#########.###.#.#.###.#.#.#.###.#.#.###.#.#.#.#.#.#.#.#.#.###.###.#####.###.###.#.#  
  #.#.#.#.#.#.#...#.#.........#.#.............#...#.......#.#...#.#.....#.....#...#.#.......#.#.#.#.#.#.#.........#...#...#.#...#.#.#  
  #####.#.#.#####.#.#######.#.###.###.#.#####.#######.#####.#.###.###.#.#.#######.#.#.###.###.#.###.#######.#.###.#.#####.#.#.#.#####  
  #.....#...#...#.#.#.#.....#.......#.#.#.............#.....#...#...#.#.....#.....#.#.#.#...#.#.#.......#...#.#.....#.........#.....#  
  ###.###.###.#.#.#.#.#.#.#.#.###.###.#.###.#######.#######.###.#.#.#.#############.#.#.###########.###.#.#.#######.#.###.###.#######  
  #.#.#.#.#.#.#.#.......#.#.#.#.....#.#.#.#.#.........#.....#...#.#.#.........#.#...#...#...#.#...#...#.#.#.......#.#.#...#.......#.#  
  #.###.#.#.###.###.###.#######.#.###.###.###.#############.#.###.#.#.#####.###.###.#.###.###.#.###.#######.#.#.###########.#.#.#.#.#  
  #.......#...#...#.#...#.#.#.#.#.#...#.#.............#.#...#.....#.#.#.#...#...#...#.....#.......#.#.....#.#.#.#...........#.#.#...#  
  #######.#.#####.#.#####.#.#.###.#####.#.#########.###.#.#########.###.#.#.#.#.###.###.###.#####.#.#.#.#.###########.#.###.###.#.###  
  #.....#.............#...#.........#.....#...#.....#.......#.#.........#.#.#.#.....#...#.#...#...#...#.#...........#.#.#...#.#.#...#  
  #.#.###.###.###.#######.#.#.#.#.###.#.#.###.#.###.#######.#.#.###.#######.###.#.###.###.#.#########.#######.#.###########.#.###.#.#  
  #.#.....#.....#.#.........#.#.#.#...#.#.#.......#.#.........#...#.#.......#...#...#.............#.........#.#.....#...........#.#.#  
  ###############################################.#####.#.#######.#######.#########.#####.###########################################  
                                                 A     U A       Q       T         E     Z                                             
                                                 E     J A       Z       J         V     A                                             '''


# _data = '''         A
#          A
#   #######.#########
#   #######.........#
#   #######.#######.#
#   #######.#######.#
#   #######.#######.#
#   #####  B    ###.#
# BC...##  C    ###.#
#   ##.##       ###.#
#   ##...DE  F  ###.#
#   #####    G  ###.#
#   #########.#####.#
# DE..#######...###.#
#   #.#########.###.#
# FG..#########.....#
#   ###########.#####
#              Z
#              Z       '''
#
# _data = '''                   A
#                    A
#   #################.#############
#   #.#...#...................#.#.#
#   #.#.#.###.###.###.#########.#.#
#   #.#.#.......#...#.....#.#.#...#
#   #.#########.###.#####.#.#.###.#
#   #.............#.#.....#.......#
#   ###.###########.###.#####.#.#.#
#   #.....#        A   C    #.#.#.#
#   #######        S   P    #####.#
#   #.#...#                 #......VT
#   #.#.#.#                 #.#####
#   #...#.#               YN....#.#
#   #.###.#                 #####.#
# DI....#.#                 #.....#
#   #####.#                 #.###.#
# ZZ......#               QG....#..AS
#   ###.###                 #######
# JO..#.#.#                 #.....#
#   #.#.#.#                 ###.#.#
#   #...#..DI             BU....#..LF
#   #####.#                 #.#####
# YN......#               VT..#....QG
#   #.###.#                 #.###.#
#   #.#...#                 #.....#
#   ###.###    J L     J    #.#.###
#   #.....#    O F     P    #.#...#
#   #.###.#####.#.#####.#####.###.#
#   #...#.#.#...#.....#.....#.#...#
#   #.#####.###.###.#.#.#########.#
#   #...#.#.....#...#.#.#.#.....#.#
#   #.###.#####.###.###.#.#.#######
#   #.#.........#...#.............#
#   #########.###.###.#############
#            B   J   C
#            U   P   P               '''
#
# _data = '''             Z L X W       C
#              Z P Q B       K
#   ###########.#.#.#.#######.###############
#   #...#.......#.#.......#.#.......#.#.#...#
#   ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###
#   #.#...#.#.#...#.#.#...#...#...#.#.......#
#   #.###.#######.###.###.#.###.###.#.#######
#   #...#.......#.#...#...#.............#...#
#   #.#########.#######.#.#######.#######.###
#   #...#.#    F       R I       Z    #.#.#.#
#   #.###.#    D       E C       H    #.#.#.#
#   #.#...#                           #...#.#
#   #.###.#                           #.###.#
#   #.#....OA                       WB..#.#..ZH
#   #.###.#                           #.#.#.#
# CJ......#                           #.....#
#   #######                           #######
#   #.#....CK                         #......IC
#   #.###.#                           #.###.#
#   #.....#                           #...#.#
#   ###.###                           #.#.#.#
# XF....#.#                         RF..#.#.#
#   #####.#                           #######
#   #......CJ                       NM..#...#
#   ###.#.#                           #.###.#
# RE....#.#                           #......RF
#   ###.###        X   X       L      #.#.#.#
#   #.....#        F   Q       P      #.#.#.#
#   ###.###########.###.#######.#########.###
#   #.....#...#.....#.......#...#.....#.#...#
#   #####.#.###.#######.#######.###.###.#.#.#
#   #.......#.......#.#.#.#.#...#...#...#.#.#
#   #####.###.#####.#.#.#.#.###.###.#.###.###
#   #.......#.....#.#...#...............#...#
#   #############.#.#.###.###################
#                A O F   N
#                A A D   M                     '''



class Tile:
    char: str

    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

    def __repr__(self):
        return self.__str__()


wall = Tile('#')
corridor = Tile('.')
start_tile = Tile('A')
end_tile = Tile('Z')

portal_chars = iter(list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase)[1:-1])

code_to_char = dict()


class Portal(Tile):
    code: str
    outer: bool

    def __init__(self, code, outer):
        self.outer = outer
        self.code = code
        if code not in code_to_char:
            code_to_char[code] = next(portal_chars)
        super().__init__(code_to_char[code])

    def __str__(self):
        return self.code

    def __repr__(self):
        return self.code


Coord = (int, int)
MazeMap = {Coord: Tile}
PortalPairs = {str: (Coord, Coord)}


def make_map(maze_lists: [str]) -> (MazeMap, Coord, Coord, PortalPairs):
    maze_map: {(int, int): Tile} = dict()
    start: (int, int) = (math.inf, math.inf)
    end: (int, int) = (math.inf, math.inf)
    portals: {Tile} = set()
    portal_pairs: {str: (str, str)} = dict()
    portal_orphans : {str: str} = dict()
    max_x, max_y = max(map(len, maze_lists)) - 1, len(maze_lists) - 1
    outer_portal_edges = ((2, max_x - 2), (2, max_y - 2))

    for y, line in enumerate(maze_lists):
        for x, cell in enumerate(line):
            if cell == '#':
                maze_map[(x, y)] = wall
            elif cell == '.':
                maze_map[(x, y)] = corridor
            elif 'A' <= cell <= 'Z':
                maze_map[(x, y)] = Tile(cell)
                portals.add((x, y))
            elif cell == ' ':
                pass
            else:
                raise Exception("Unknown cell {}".format(cell))

    while len(portals) > 0:
        portal_pos = portals.pop()
        entrance: Union[(int, int), None] = None
        chr1: str = '?'
        chr2: str = '?'
        for n in neighbours(portal_pos):
            if n not in maze_map:
                continue
            if maze_map[n] == corridor:
                entrance = n
                if n > portal_pos:
                    chr2 = maze_map.pop(portal_pos).char
                else:
                    chr1 = maze_map.pop(portal_pos).char
                maze_map[portal_pos] = wall
            if n in portals:
                portals.remove(n)
                next_to = (2 * n[0] - portal_pos[0], 2 * n[1] - portal_pos[1])
                if next_to in maze_map and maze_map[next_to] == corridor:
                    entrance = next_to
                    if n > portal_pos:
                        chr1 = maze_map.pop(portal_pos).char
                        chr2 = maze_map.pop(n).char
                    else:
                        chr2 = maze_map.pop(portal_pos).char
                        chr1 = maze_map.pop(n).char
                    maze_map[n] = wall
                else:
                    if portal_pos > n:
                        chr1 = maze_map.pop(n).char
                    else:
                        chr2 = maze_map.pop(n).char

        if entrance is None:
            raise Exception("Broken portal {}".format(portal_pos))
        code = chr1 + chr2
        if code == 'AA':
            maze_map[entrance] = start_tile
            start = entrance
        elif code == 'ZZ':
            maze_map[entrance] = end_tile
            end = entrance
        else:
            maze_map[entrance] = Portal(code, None)
            if code in portal_orphans:
                other = portal_orphans.pop(code)
                if outer_portal_edges[0][1] <= entrance[0] or entrance[0] <= outer_portal_edges[0][0] or \
                        outer_portal_edges[1][1] <= entrance[1] or entrance[1] <= outer_portal_edges[1][0]:
                    maze_map[entrance].outer = True
                    maze_map[other].outer = False
                else:
                    maze_map[other].outer = True
                    maze_map[entrance].outer = False
                portal_pairs[code] = (entrance, other)
            else:
                portal_orphans[code] = entrance

    if len(portal_orphans) > 0:
        raise Exception("Orphaned portals: {}".format(portal_orphans))
    return maze_map, start, end, portal_pairs


def make_graph(maze_map: MazeMap, pos: Coord, portal_pairs: PortalPairs):
    maze_root: Graph[Tile] = Graph(maze_map[pos])
    frontier = deque(list(
        zip(filter(lambda x: maze_map[x] != wall, neighbours(pos)),
            repeat(maze_root), repeat(1), repeat(pos))))
    pos_node_map = {pos: maze_root}
    visited = {pos}
    for cell, _, _, _ in frontier:
        visited.add(cell)
    while len(frontier) > 0:
        cell, node, cost, tail = frontier.pop()
        visited.add(cell)
        tile = maze_map[cell]
        ns = list(filter(lambda x: maze_map[x] != wall, neighbours(cell)))
        if type(tile) == Portal:
            tile: Portal
            cell1, cell2 = portal_pairs[tile.code]
            if cell1 == cell:
                ns.append(cell2)
            else:
                ns.append(cell1)
        if len(ns) > 2 or type(tile) == Portal or tile == start_tile or tile == end_tile:
            # We make a node!
            extending_node = node
            node = Graph(tile)
            node.add_connected(extending_node, cost)
            pos_node_map[cell] = node
            cost = 0
        elif len(ns) == 1:
            continue

        for n in ns:
            if n != tail and n in pos_node_map:
                node.add_connected(pos_node_map[n], cost + 1)
            if n not in visited:
                frontier.append((n, node, cost + 1, cell))
    return maze_root


def run():
    print(_data)
    maze_list = _data.splitlines()
    maze_map, start, end, portal_pairs = make_map(maze_list)
    dict(map(lambda x: (0, x + 1), (4,)))
    String2DBuilder(map(lambda x: (x[0], x[1].char), maze_map.items())).print()

    maze_graph = make_graph(maze_map, start, portal_pairs)

    start = (maze_graph, 0)

    def get_neighbours(node: (Graph[Tile], int)):
        graph_node: Graph[Tile]
        level: int
        graph_node, level = node
        for n, cost in graph_node.connected:
            if type(graph_node.val) == Portal and type(n.val) == Portal:
                if graph_node.val.outer and level > 0:
                    yield (n, level - 1), cost
                elif not graph_node.val.outer:
                    yield (n, level + 1), cost
            else:
                yield (n, level), cost

    end_node, dists, prev = find_path(start, is_final=lambda x: x[0].val == end_tile and x[1] == 0,
                                      get_neighbours=get_neighbours)
    print(end_node, dists[end_node])


if __name__ == '__main__':
    run()