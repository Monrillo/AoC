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

lines=['.#....#####...#..',
'##...##.#####..##',
'##...#...#.#####.',
'..#.....X...###..',
'..#.#.....#....##']

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
c=np.where(matrix=='#')[0][visible.index(max(visible))]
l=np.where(matrix=='#')[1][visible.index(max(visible))]
print(l,c)

c=np.where(matrix=='X')[0][0]
l=np.where(matrix=='X')[1][0]
print(l,c)

angle=set()
for s in range(len(np.where(matrix=='#')[0])):
    x=c-np.where(matrix=='#')[0][s]
    y=l-np.where(matrix=='#')[1][s]
    angle.add(np.arctan2(y,x))


x=c-6
y=l-8
np.arctan2(y,x)




