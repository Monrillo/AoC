# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:34:31 2025

@author: castelf

Solution thanks to pedrosorio
"""

from collections import deque
#from itertools import permutations

mat = [line.strip() for line in open('C:\\Users\Florent\Documents\GitHub\AoC\\2016\day24.txt').readlines()]

lines=['###########',
'#0.1.....2#',
'#.#######.#',
'#4.......3#',
'###########']

mat=[line.strip() for line in lines]

# find position of numbers into the map
def find_position(mp, num):
    pos = [(i,j) for i in range(len(mp)) for j in range(len(mp[i])) if mp[i][j]==str(num)]
    if pos:
        return pos[0]

num_pos = [find_position(mat, n) for n in range(10) if find_position(mat, n)!=None]
init_pos = num_pos.pop(0)

directions = set([(-1, 0), (1, 0), (0, 1), (0, -1)])

# I use the bfs algorithm from pedrosorio solution (BST stands for Binary Search Tree)
# to compute the distance between 2 number positions into the map
def dist_from_to(mp, fr, to):
    path = deque([(0, fr)])
    visited = set([fr])
    
    while path:
        dist, pos = path.pop()
        if pos == to:
            return dist
        
        y, x = pos
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if mp[ny][nx]!='#' and mp[ny][nx] not in visited:
                visited.add((ny, nx))
                path.appendleft((dist+1,(ny, nx)))

dst_init = [dist_from_to(mat, init_pos, n_pos) for n_pos in num_pos]




























import numpy as np

mat=[list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day24.txt','r')]

# lines=['###########',
# '#0.1.....2#',
# '#.#######.#',
# '#4.......3#',
# '###########']
# mat=[list(line.strip()) for line in lines]

# Creation of the matrix area
area=np.empty((len(mat),len(mat[0])),dtype=str)
for r in range(len(mat)):
    for c in range(len(mat[0])):
        area[r][c]=mat[r][c]

#print(area)

# List of number and their position in the matrix
num_pos=[(np.where(area==str(0))[0][0],np.where(area==str(0))[1][0])]
for i in range(1,10):
    if len(np.where(area==str(i))[0])!=0:
        r,c=np.where(area==str(i))
        num_pos.append((r[0],c[0]))

# From previous day13
def move(w):
    y=w[-1][0];x=w[-1][1]
    pos_m=[]
    link=[]
    if y-1>=0 and area[y-1,x]=='.' and (y-1,x) not in w: pos_m.append(w+[(y-1,x)])
    if (y-1,x) in num_pos: link.append(w+[(y-1,x)])
    if y+1<len(area) and area[y+1,x]=='.' and (y+1,x) not in w: pos_m.append(w+[(y+1,x)])
    if (y+1,x) in num_pos: link.append(w+[(y+1,x)])
    if x-1>=0 and area[y,x-1]=='.' and (y,x-1) not in w: pos_m.append(w+[(y,x-1)])
    if (y,x-1) in num_pos: link.append(w+[(y,x-1)])
    if x+1<len(area) and area[y,x+1]=='.' and (y,x+1) not in w: pos_m.append(w+[(y,x+1)])
    if (y,x+1) in num_pos: link.append(w+[(y,x+1)])
    return pos_m,link


# Distance between each pair of numbers
links=[]
dist=[]
for pos in num_pos:
    way=[[pos]]
    while len(way)>0:
        p=way.pop(0)
        paths,connec=move(p)
        if connec:
            for c in connec:
                if c[0]!=c[-1]:
                    links.append((min(num_pos.index(c[0]),num_pos.index(c[-1])),max(num_pos.index(c[0]),num_pos.index(c[-1]))))
                    dist.append(len(c)-1)
        way+=paths

# Minimum distance between each pair of numbers
min_links=[]
min_dist=[]
for i,l in enumerate(sorted(links)):
    if l in min_links:
        if min_dist[min_links.index(l)]>dist[i]: min_dist[min_links.index(l)]=dist[i]
    else:
        min_links.append(l)
        min_dist.append(dist[i])
