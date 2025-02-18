# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:17:09 2025

@author: castelf
"""

import numpy as np
import re

mat=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day22.txt',skiprows=2,dtype=str)
grid=np.zeros((len(mat),6),dtype=int)
for i in range(len(mat)):
    grid[i,0]=int(re.findall(r'x(\d+)',mat[i,0])[0])
    grid[i,1]=int(re.findall(r'y(\d+)',mat[i,0])[0])
    grid[i,2]=int(re.findall(r'(\d+)',mat[i,1])[0])
    grid[i,3]=int(re.findall(r'(\d+)',mat[i,2])[0])
    grid[i,4]=int(re.findall(r'(\d+)',mat[i,3])[0])
    grid[i,5]=int(re.findall(r'(\d+)',mat[i,4])[0])

viable=[]
for i in range(len(grid)):
    if grid[i,3]==0: continue
    for j in range(len(grid)):
        if j!=i and grid[i,4]>=grid[j,3]: viable.append((i,j))

print(len(viable))