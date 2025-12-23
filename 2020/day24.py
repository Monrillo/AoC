# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 15:28:38 2025

@author: castelf
"""

import numpy as np
from collections import Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day24.txt','r') as f: lines=f.readlines()

# lines=['sesenwnenenewseeswwswswwnenewsewsw',
# 'neeenesenwnwwswnenewnwwsewnenwseswesw',
# 'seswneswswsenwwnwse',
# 'nwnwneseeswswnenewneswwnewseswneseene',
# 'swweswneswnenwsewnwneneseenw',
# 'eesenwseswswnenwswnwnwsewwnwsene',
# 'sewnenenenesenwsewnenwwwse',
# 'wenwwweseeeweswwwnwwe',
# 'wsweesenenewnwwnwsenewsenwwsesesenwne',
# 'neeswseenwwswnwswswnw',
# 'nenwswwsewswnenenewsenwsenwnesesenew',
# 'enewnwewneswsewnwswenweswnenwsenwsw',
# 'sweneswneswneneenwnewenewwneswswnese',
# 'swwesenesewenwneswnwwneseswwne',
# 'enesenwswwswneneswsenwnewswseenwsese',
# 'wnwnesenesenenwwnenwsewesewsesesew',
# 'nenewswnwewswnenesenwnesewesw',
# 'eneswnwswnwsenenwnwnwwseeswneewsenese',
# 'neswnwewnwnwseenwseesewsenwsweewe',
# 'wseweeenwnesenwwwswnew']

def path(l):
    x=y=0
    pos=0
    while pos<len(l):
        direc=l[pos]
        if direc=='e':x-=1;y+=1
        elif direc=='w':x+=1;y-=1
        else:
            pos+=1
            direc+=l[pos]
            if direc=='se':y+=1
            elif direc=='sw':x+=1
            elif direc=='nw':y-=1
            elif direc=='ne':x-=1
        pos+=1
    return (x,y)

tiles=[]
for line in lines:
    tiles.append(path(line.strip('\n')))
count=Counter(tiles)

print("Part 1:",sum(1 for k in count.keys() if count[k]%2==1))

tiles=np.array(tiles)
tiles+=100

matrix=np.zeros((200,200),dtype=int)
for t in tiles:matrix[t[0],t[1]]+=1

# La plus belle ligne de code que j'ai pu écrire
matrix%=2

def neigh(x,y):
    neighbors=0
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=j and matrix[x+i,y+j]==1:neighbors+=1
    return neighbors

from tqdm import tqdm
for _ in tqdm(range(100)):
    new_matrix=matrix.copy()
    for l in range(1,matrix.shape[0]-1):
        for c in range(1,matrix.shape[1]-1):
            if matrix[l,c]==1 and (neigh(l,c)==0 or neigh(l,c)>2): new_matrix[l,c]=0
            elif matrix[l,c]==0 and neigh(l,c)==2: new_matrix[l,c]=1
    matrix=new_matrix
    
print("Part 2:",np.sum(matrix))
