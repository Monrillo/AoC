# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:17:09 2025

@author: castelf
"""

import numpy as np
from matplotlib import pyplot as plt
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
    for j in range(len(grid)):
        if j!=i and grid[i,3]!=0 and grid[j,4]>=grid[i,3]: viable.append((i,j))

print(len(viable))

test=np.full((max(grid[:,1]+1),max(grid[:,0])+1),1)
test[0,0]=test[0,31]=3
for g in grid:
    if g[3]==0: test[g[1],g[0]]=0
    if g[2]>100: test[g[1],g[0]]=2

fig,ax=plt.subplots(figsize=(20,20))
im=plt.matshow(test)
fig.colorbar(im)
plt.show()

grid[grid[:,3]==0]
grid[grid[:,2]>100]

grid[grid[:,1]==12]

(24-8)+22+(31-8)+30*5
