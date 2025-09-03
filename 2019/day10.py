# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 14:16:39 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day10.txt','r') as f: lines=f.readlines()

# lines=['.#..##.###...#######',
# '##.############..##.',
# '.#.######.########.#',
# '.###.#######.####.#.',
# '#####.##.#.##.###.##',
# '..#####..#.#########',
# '####################',
# '#.####....###.#.#.##',
# '##.#################',
# '#####.##.###..####..',
# '..######..##.#######',
# '####.##.####...##..#',
# '.#####..#.######.###',
# '##...#.##########...',
# '#.##########.#######',
# '.####.#.###.###.#.##',
# '....##.##.###..#####',
# '.#.#.###########.###',
# '#.#.#.#####.####.###',
# '###.##.####.##.#..##']

# lines=['.#....#####...#..',
# '##...##.#####..##',
# '##...#...#.#####.',
# '..#.....X...###..',
# '..#.#.....#....##']

matrix=np.array([list(line.strip()) for line in lines])

asteroids=[]
for p in range(len(np.where(matrix=='#')[0])):
    angle=set()
    for s in range(len(np.where(matrix=='#')[0])):
        if s!=p:
            x=np.where(matrix=='#')[0][p]-np.where(matrix=='#')[0][s]
            y=np.where(matrix=='#')[1][p]-np.where(matrix=='#')[1][s]
            angle.add(np.arctan2(y,x))
    asteroids.append(angle)
        
visible=[len(a) for a in asteroids]
print(max(visible))

# New station
l=np.where(matrix=='#')[0][visible.index(max(visible))]
c=np.where(matrix=='#')[1][visible.index(max(visible))]

angle={}
for s in range(len(np.where(matrix=='#')[0])):
    x=l-np.where(matrix=='#')[0][s]
    y=c-np.where(matrix=='#')[1][s]
    if np.arctan2(y,x) in angle:
        angle[np.arctan2(y,x)].append((np.where(matrix=='#')[0][s],np.where(matrix=='#')[1][s]))
    else: angle[np.arctan2(y,x)]=[(np.where(matrix=='#')[0][s],np.where(matrix=='#')[1][s])]


angle_vis=list(angle.keys())
angle_vis.sort()
angle_vis.reverse()
angle_vis=angle_vis[angle_vis.index(0.0):]+angle_vis[:angle_vis.index(0.0)]

vaporize=0
while vaporize<200:
    angle_del=[]
    for ang in angle_vis:
        if vaporize==199:
            if len(angle[ang])==1:
                end=angle[ang][0]
            else:
                dist=[abs(l-pos[0])+abs(c-pos[1]) for pos in angle[ang]]
                end=angle[ang][dist.index(min(dist))]
            print(end[1]*100+end[0])
        if len(angle[ang])==1:
            del angle[ang];angle_del.append(ang)
        else:
            dist=[abs(l-pos[0])+abs(c-pos[1]) for pos in angle[ang]]
            angle[ang].pop(dist.index(min(dist)))
        vaporize+=1
    angle_vis=[x for x in angle_vis if x not in angle_del]


