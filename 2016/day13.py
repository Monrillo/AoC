# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:25:20 2025

@author: castelf
"""

import numpy as np

area=np.full((10,10),'.')
odfn=10
for x in range(len(area)):
    for y in range(len(area)):
        num=(x*x + 3*x + 2*x*y + y + y*y)+odfn
        if bin(num)[2:].count('1')%2==1: area[y,x]='#'

area[1,1]='O'
area[4,7]='X'

def move(x,y):
    pos_m=[]
    if y-1>=0 and area[y-1,x]=='.': pos_m.append((y-1,x))
    if y+1<len(area) and area[y+1,x]=='.': pos_m.append((y+1,x))
    if x-1>=0 and area[y,x-1]=='.': pos_m.append((y,x-1))
    if x+1<len(area) and area[y,x+1]=='.': pos_m.append((y,x+1))
    return pos_m

pos_move=move(1,1)
if (4,7) in pos_move: step+=1;break
next_move=pos_move[np.random.randint(len(pos_move))]
