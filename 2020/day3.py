# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 15:57:02 2025

@author: castelf
"""
import math

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day3.txt','r') as f: lines=f.readlines()

# lines =['..##.......',
# '#...#...#..',
# '.#....#..#.',
# '..#.#...#.#',
# '.#...##..#.',
# '..#.##.....',
# '.#.#.#....#',
# '.#........#',
# '#.##...#...',
# '#...##....#',
# '.#..#...#.#']

right=[1,3,5,7,1]
down=[1,1,1,1,2]

all_trees=[]
for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    pos=-r
    trees=0
    for i in range(0,len(lines),d):
        pos=(pos + r)%len(lines[i].strip())
        if lines[i].strip()[pos]=='#':trees+=1
    all_trees.append(trees)

print(math.prod(all_trees))


