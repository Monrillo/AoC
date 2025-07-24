# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 14:50:04 2025

@author: castelf
"""
import re
import numpy as np
import matplotlib.pyplot as plt

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day10.txt','r') as f: lines=f.readlines()

lines=['position=< 9,  1> velocity=< 0,  2>',
'position=< 7,  0> velocity=<-1,  0>',
'position=< 3, -2> velocity=<-1,  1>',
'position=< 6, 10> velocity=<-2, -1>',
'position=< 2, -4> velocity=< 2,  2>',
'position=<-6, 10> velocity=< 2, -2>',
'position=< 1,  8> velocity=< 1, -1>',
'position=< 1,  7> velocity=< 1,  0>',
'position=<-3, 11> velocity=< 1, -2>',
'position=< 7,  6> velocity=<-1, -1>',
'position=<-2,  3> velocity=< 1,  0>',
'position=<-4,  3> velocity=< 2,  0>',
'position=<10, -3> velocity=<-1,  1>',
'position=< 5, 11> velocity=< 1, -2>',
'position=< 4,  7> velocity=< 0, -1>',
'position=< 8, -2> velocity=< 0,  1>',
'position=<15,  0> velocity=<-2,  0>',
'position=< 1,  6> velocity=< 1,  0>',
'position=< 8,  9> velocity=< 0, -1>',
'position=< 3,  3> velocity=<-1,  1>',
'position=< 0,  5> velocity=< 0, -1>',
'position=<-2,  2> velocity=< 2,  0>',
'position=< 5, -2> velocity=< 1,  2>',
'position=< 1,  4> velocity=< 2,  1>',
'position=<-2,  7> velocity=< 2, -2>',
'position=< 3,  6> velocity=<-1, -1>',
'position=< 5,  0> velocity=< 1,  0>',
'position=<-6,  0> velocity=< 2,  0>',
'position=< 5,  9> velocity=< 1, -2>',
'position=<14,  7> velocity=<-2,  0>',
'position=<-3,  6> velocity=< 2, -1>']

pos=[]
vit=[]
for line in lines:
    x,y,vx,vy=re.findall(r'(-?\d+)', line.strip())
    pos.append([int(x),int(y)])
    vit.append([int(vx),int(vy)])
pos=np.array(pos)
vit=np.array(vit)

# approach lights
n=0
while np.max(pos[:,0])-np.min(pos[:,0])>100:
    pos+=vit
    n+=1

# Translation for positive values
pos[:,0]-=np.min(pos[:,0])
pos[:,1]-=np.min(pos[:,1])

# Make the loop by hand
pos+=vit
n+=1

mat=np.zeros((np.max(pos[:,1])+1,np.max(pos[:,0])+1),dtype=int)
for p in pos: mat[p[1]][p[0]]=1

fig,ax = plt.subplots(figsize=(12,12))
ax.matshow(mat)


