# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 14:55:30 2025

@author: castelf
"""

import numpy as np

positions=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day6.txt',dtype=int,delimiter=',')

# positions=np.array([[1, 1],
# [1, 6],
# [8, 3],
# [3, 4],
# [5, 5],
# [8, 9]])

# possible=np.where(np.logical_and((np.logical_and(positions[:,0]>np.min(positions[:,0]),positions[:,0]<np.max(positions[:,0]))),\
#                 (np.logical_and(positions[:,1]>np.min(positions[:,1]),positions[:,1]<np.max(positions[:,1])))))[0]

matrix=np.full((np.max(positions),np.max(positions)),-1,dtype=int)
summat=np.zeros_like(matrix)

def mind(r,c):
    d=[abs(r-pos[1])+abs(c-pos[0]) for pos in positions]
    if len(np.where(d==np.min(d))[0])==1: return np.where(d==np.min(d))[0][0]
    else : return -1

def sumd(r,c):
    d=[abs(r-pos[1])+abs(c-pos[0]) for pos in positions]
    if np.sum(d)<10000: return 1
    else : return 0

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        matrix[i,j]=mind(i,j)
        summat[i,j]=sumd(i,j)

possible=np.arange(len(positions))
bord=np.unique(np.hstack((matrix[0,:],matrix[-1,:],matrix[:,0],matrix[:,-1])))
possible=np.delete(possible,bord)

size=[len(np.where(matrix==p)[0]) for p in possible]
print(np.max(size))        

print(np.sum(summat))