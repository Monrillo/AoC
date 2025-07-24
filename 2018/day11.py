# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 11:28:47 2025

@author: castelf
"""

import numpy as np

# Serial number
serial=5791

# Initialise
mat=np.zeros((300,300),dtype=int)

def level(x,y):
    rackid=10+x
    l=rackid*y+serial
    l*=rackid
    res=('000'+str(l))[-3]
    return int(res)-5

# Construct the grid
for r in range(300):
    for c in range(300):
        x=r+1; y=c+1
        mat[r][c]=level(x,y)


# Compute maximum
# result=[]
# for size in range(1,301):
#     coord=[]
#     pow_lvl=[]
#     for r in range(301-size):
#         for c in range(301-size):
#             coord.append((r+1,c+1))
#             pow_lvl.append(np.sum(mat[r:r+size,c:c+size]))
#     result.append([pow_lvl[np.argmax(pow_lvl)],coord[np.argmax(pow_lvl)],size])
                      
# result=np.array(result,dtype=object)

# print(result[np.argmax(result[:,0])])


# TO GO FASTER

for size in range(1,301):
    coord=[]
    pow_lvl=[]
    for r in range(301-size):
        for c in range(301-size):
            coord.append((r+1,c+1))
            pow_lvl.append(np.sum(mat[r:r+size,c:c+size]))
    print([pow_lvl[np.argmax(pow_lvl)],coord[np.argmax(pow_lvl)],size])
                      
###############################

# Solution from sciyoshi

def level2(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = np.fromfunction(level, (300, 300))

for width in range(3, 300):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = np.where(windows == maximum)
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)
