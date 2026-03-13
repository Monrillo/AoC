# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:49:33 2026

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day14.txt','r') as f: lines=f.readlines()

# lines=['p=0,4 v=3,-3',
# 'p=6,3 v=-1,-3',
# 'p=10,3 v=-1,2',
# 'p=2,0 v=2,-1',
# 'p=0,0 v=1,3',
# 'p=3,0 v=-2,-2',
# 'p=7,6 v=-1,-3',
# 'p=3,0 v=-1,-2',
# 'p=9,3 v=2,3',
# 'p=7,3 v=-1,2',
# 'p=2,4 v=2,-3',
# 'p=9,5 v=-3,-3']

ligne=103
colonne=101
seconds=100
quadrant=[0,0,0,0]

for line in lines:
    x,y,vx,vy=[int(x) for x in re.findall(r'(-?\d+)', line.strip('\n'))]
    x+=seconds*vx
    y+=seconds*vy
    y%=ligne
    x%=colonne
    if x<colonne//2 and y<ligne//2: quadrant[0]+=1
    elif x>colonne//2 and y<ligne//2: quadrant[1]+=1
    elif x<colonne//2 and y>ligne//2: quadrant[2]+=1
    elif x>colonne//2 and y>ligne//2: quadrant[3]+=1

security_level=quadrant[0]*quadrant[1]*quadrant[2]*quadrant[3]

print("Part 1:",security_level)

import numpy as np
from matplotlib import pyplot as plt

# lines=['p=0,4 v=3,-3',
# 'p=6,3 v=-1,-3',
# 'p=10,3 v=-1,2',
# 'p=2,0 v=2,-1',
# 'p=0,0 v=1,3',
# 'p=3,0 v=-2,-2',
# 'p=7,6 v=-1,-3',
# 'p=3,0 v=-1,-2',
# 'p=9,3 v=2,3',
# 'p=7,3 v=-1,2',
# 'p=2,4 v=2,-3',
# 'p=9,5 v=-3,-3']

#ligne=7
#colonne=11
#seconds=5
robots={}
for i,line in enumerate(lines):
    robots[i]=[int(x) for x in re.findall(r'(-?\d+)', line.strip('\n'))]

for s in range(1,10000+1):
    if s%103==19 or s%101==74:
        matrix=np.zeros((ligne,colonne),dtype=int)
        for r in robots:
            x,y,vx,vy=robots[r]
            x+=s*vx
            y+=s*vy
            y%=ligne
            x%=colonne
            matrix[y,x]+=1
        plt.matshow(matrix)
        plt.title(s)
    

        

