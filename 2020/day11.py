# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:24:28 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day11.txt','r') as f: lines=f.readlines()

# lines=['L.LL.LL.LL',
# 'LLLLLLL.LL',
# 'L.L.L..L..',
# 'LLLL.LL.LL',
# 'L.LL.LL.LL',
# 'L.LLLLL.LL',
# '..L.L.....',
# 'LLLLLLLLLL',
# 'L.LLLLLL.L',
# 'L.LLLLL.LL']

matrix=np.array([list(l.strip()) for l in lines])
rm,cm=matrix.shape
next_matrix=matrix.copy()


def occupation(r,c):
    busy=0
    for i in range(-1,2):
        for j in range(-1,2):
            if (i!=0 or j!=0):
                if 0<=r+i<rm and 0<=c+j<cm and matrix[r+i,c+j]=='#':busy+=1
    return busy

def sight(r,c):
    busy=0
    
    # NW
    n=0
    while True:
        n+=1
        if r-n<0 or c-n<0 or matrix[r-n,c-n]=='L':break
        elif matrix[r-n,c-n]=='#': busy+=1;break
        else: continue
    
    # N
    n=0
    while True:
        n+=1
        if r-n<0 or matrix[r-n,c]=='L':break
        elif matrix[r-n,c]=='#': busy+=1;break
        else: continue
    
    # NE
    n=0
    while True:
        n+=1
        if r-n<0 or c+n>=cm or matrix[r-n,c+n]=='L':break
        elif matrix[r-n,c+n]=='#': busy+=1;break
        else: continue
    
    # E
    n=0
    while True:
        n+=1
        if c+n>=cm or matrix[r,c+n]=='L':break
        elif matrix[r,c+n]=='#': busy+=1;break
        else: continue
    
    # SE
    n=0
    while True:
        n+=1
        if r+n>=rm or c+n>=cm or matrix[r+n,c+n]=='L':break
        elif matrix[r+n,c+n]=='#': busy+=1;break
        else: continue
    
    # S
    n=0
    while True:
        n+=1
        if r+n>=rm or matrix[r+n,c]=='L':break
        elif matrix[r+n,c]=='#': busy+=1;break
        else: continue
    
    # SW
    n=0
    while True:
        n+=1
        if r+n>=rm or c-n<0 or matrix[r+n,c-n]=='L':break
        elif matrix[r+n,c-n]=='#': busy+=1;break
        else: continue
    
    # W
    n=0
    while True:
        n+=1
        if c-n<0 or matrix[r,c-n]=='L':break
        elif matrix[r,c-n]=='#': busy+=1;break
        else: continue

    return busy

identical=False
while not identical:
    #mem_matrix+=1
    
    # Arrival
    matrix=next_matrix.copy()
    pos=np.reshape(np.concatenate((np.where(matrix=='L')[0],np.where(matrix=='L')[1])),(2,len(np.where(matrix=='L')[0]))).T
    for p in pos:
        if occupation(p[0],p[1])==0:
            next_matrix[p[0],p[1]]='#'
    
    # Departure
    matrix=next_matrix.copy()
    pos=np.reshape(np.concatenate((np.where(matrix=='#')[0],np.where(matrix=='#')[1])),(2,len(np.where(matrix=='#')[0]))).T
    for p in pos:
        if occupation(p[0],p[1])>=4:
            next_matrix[p[0],p[1]]='L'

    identical=np.array_equal(matrix, next_matrix)

print("Part 1:",len(np.where(matrix=='#')[0]))

matrix=np.array([list(l.strip()) for l in lines])
next_matrix=matrix.copy()

identical=False
while not identical:
    #mem_matrix+=1
    
    # Arrival
    matrix=next_matrix.copy()
    pos=np.reshape(np.concatenate((np.where(matrix=='L')[0],np.where(matrix=='L')[1])),(2,len(np.where(matrix=='L')[0]))).T
    for p in pos:
        if sight(p[0],p[1])==0:
            next_matrix[p[0],p[1]]='#'
    
    # Departure
    matrix=next_matrix.copy()
    pos=np.reshape(np.concatenate((np.where(matrix=='#')[0],np.where(matrix=='#')[1])),(2,len(np.where(matrix=='#')[0]))).T
    for p in pos:
        if sight(p[0],p[1])>=5:
            next_matrix[p[0],p[1]]='L'

    identical=np.array_equal(matrix, next_matrix)

print("Part 2:",len(np.where(matrix=='#')[0]))