# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:25:20 2025

@author: castelf
"""

import numpy as np

# area=np.full((10,10),'.')
# odfn=10
# finish=(4,7)
area=np.full((50,50),'.')
odfn=1358
finish=(39,31)
for x in range(len(area)):
    for y in range(len(area)):
        num=(x*x + 3*x + 2*x*y + y + y*y)+odfn
        if bin(num)[2:].count('1')%2==1: area[y,x]='#'
#print(area)

pos=(1,1)
way=[[pos]]

def move(w):
    y=w[-1][0];x=w[-1][1]
    pos_m=[]
    if y-1>=0 and area[y-1,x]=='.' and (y-1,x) not in w: pos_m.append(w+[(y-1,x)])
    if y+1<len(area) and area[y+1,x]=='.' and (y+1,x) not in w: pos_m.append(w+[(y+1,x)])
    if x-1>=0 and area[y,x-1]=='.' and (y,x-1) not in w: pos_m.append(w+[(y,x-1)])
    if x+1<len(area) and area[y,x+1]=='.' and (y,x+1) not in w: pos_m.append(w+[(y,x+1)])
    return pos_m

good_way=[]
fifty_rule=[pos]
while len(way)>0:
    p=way.pop(0)
    if p[-1]==finish: good_way.append(p)
    if p[-1] not in fifty_rule and len(p)<=51: fifty_rule.append(p[-1])
    paths=move(p)
    way+=paths
    #print(way)

l=[len(x) for x in good_way]
np.where(l==np.min(l))[0][0]
res=good_way[np.where(l==np.min(l))[0][0]]
#for p in res: area[p]='O'
#print(area)
print(np.min(l)-1)
print(len(fifty_rule))

#-----------------------------------------------------------------------------

# DFS : Depth First Search

frontier = [(1,1,0)]
explored = {}

def get_wall(tup):
    num = tup[0] * tup[0] + 3 * tup[0] + 2 * tup[0] * tup[1] +tup[1] + tup[1] * tup[1] + 1358
    return bin(num)[2:].count("1") % 2 == 0 and tup[0] >= 0 and tup[1] >= 0

def get_next(tup):
    cand = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x[0] + tup[0], x[1] + tup[1], tup[2] + 1) for x in cand if get_wall((x[0] + tup[0], x[1] + tup[1]))]

while len(frontier) > 0:
    new = frontier.pop()
    explored[(new[0], new[1])] = new[2]
    frontier += [x for x in get_next(new) if not (x[0], x[1]) in explored or explored[(x[0], x[1])] > x[2]]

print (explored[(31,39)], len([explored[x] for x in explored.keys() if explored[x] <= 50]))
