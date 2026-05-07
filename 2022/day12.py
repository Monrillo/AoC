# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:58:54 2026

@author: castelf
"""

import copy

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day12.txt','r') as f: lines=f.readlines()

map_height=[list(line.strip('\n')) for line in lines]
num_l=len(map_height)
num_c=len(map_height[0])

height={}
for l in range(num_l):
    for c in range(num_c):
        if map_height[l][c]=='S': start=(l,c);map_height[l][c]='a'
        elif map_height[l][c]=='E': end=(l,c);map_height[l][c]='z'
        height[(l,c)]=[ord(map_height[l][c]),None]

# Possible starting points
bottom=[p for p in height.keys() if height[p][0]==ord('a')]

# Part 1 - Starting at S point
height_test = copy.deepcopy(height)

trackers=[[start,0]]
height_test[start]=[ord('a'),0]

while trackers:
    pos,step=trackers.pop(0)
    next_pos=[[(pos[0]-1,pos[1]),step+1],[(pos[0]+1,pos[1]),step+1],[(pos[0],pos[1]-1),step+1],[(pos[0],pos[1]+1),step+1]]
    for n in next_pos:
        p,s=n
        if p in height_test.keys() and height_test[p][0]<=height_test[pos][0]+1 and (height_test[p][1] is None or s<height_test[p][1]):
            height_test[p][1]=s
            trackers.append(n)

print("Part 1:",height_test[end][1])

# Part 2 - Starting at all possible starting points
score=[]

for st in bottom:
    height_test = copy.deepcopy(height)
    trackers=[[st,0]]
    height_test[st]=[ord('a'),0]
    
    while trackers:
        pos,step=trackers.pop(0)
        next_pos=[[(pos[0]-1,pos[1]),step+1],[(pos[0]+1,pos[1]),step+1],[(pos[0],pos[1]-1),step+1],[(pos[0],pos[1]+1),step+1]]
        for n in next_pos:
            p,s=n
            if p in height_test.keys() and height_test[p][0]<=height_test[pos][0]+1 and (height_test[p][1] is None or s<height_test[p][1]):
                height_test[p][1]=s
                trackers.append(n)
    
    if height_test[end][1] is not None: score.append(height_test[end][1])

print("Part 2:",min(score))


