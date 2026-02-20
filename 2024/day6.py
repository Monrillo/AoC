# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 09:57:52 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day6.txt','r') as f: lines=f.readlines()

# lines=['....#.....',
# '.........#',
# '..........',
# '..#.......',
# '.......#..',
# '..........',
# '.#..^.....',
# '........#.',
# '#.........',
# '......#...']

matrix=np.array([list(l.strip('\n')) for l in lines])

# Position
init_pos=np.concatenate([np.where(matrix=='^')[0],np.where(matrix=='^')[1]])

# Direction
directions=[[-1,0],[0,1],[1,0],[0,-1]]

pos=init_pos
# Loop
while True:
    matrix[pos[0],pos[1]]='X'
    d=directions[0]
    new_pos=pos+d
    if new_pos[0]<0 or new_pos[1]<0 or new_pos[0]==matrix.shape[0] or new_pos[1]==matrix.shape[1]: break
    elif matrix[new_pos[0],new_pos[1]]=='#': directions=directions[1:]+directions[:1]
    else: pos=new_pos

print("Part 1:",len(np.where(matrix=='X')[0]))

def test_loop(l,c):
    directions=[[-1,0],[0,1],[1,0],[0,-1]]
    pos=init_pos
    path=set()
    while True:
        d=directions[0]
        if (pos[0],pos[1],d[0],d[1]) in path: return True;break
        path.add((pos[0],pos[1],d[0],d[1]))
        new_pos=pos+d
        if new_pos[0]<0 or new_pos[1]<0 or new_pos[0]==matrix.shape[0] or new_pos[1]==matrix.shape[1]: return False;break
        elif matrix[new_pos[0],new_pos[1]]=='#' or (new_pos[0]==l and new_pos[1]==c): directions=directions[1:]+directions[:1]
        else: pos=new_pos

from tqdm import tqdm

guard=0
for i in tqdm(range(len(np.where(matrix=='X')[0]))):
    l=np.where(matrix=='X')[0][i]
    c=np.where(matrix=='X')[1][i]
    if test_loop(l,c):guard+=1

print("Part 2:",guard)
