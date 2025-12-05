# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 15:03:30 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day4.txt','r') as f: lines=f.readlines()

# lines=['..@@.@@@@.',
# '@@@.@.@.@@',
# '@@@@@.@.@@',
# '@.@@@@..@.',
# '@@.@@@@.@@',
# '.@@@@@@@.@',
# '.@.@.@.@@@',
# '@.@@@.@@@@',
# '.@@@@@@@@.',
# '@.@.@@@.@.']

mat=[list(l.strip()) for l in lines]
matrix=np.array(mat)
extend_matrix=np.pad(matrix, ((1, 1), (1, 1)), 'constant', constant_values='.')
rolls=[(np.where(extend_matrix=='@')[0][i],np.where(extend_matrix=='@')[1][i]) for i in range(len(np.where(extend_matrix=='@')[0]))]

def neigh(pos):
    x,y=pos
    return len(np.where(extend_matrix[x-1:x+2,y-1:y+2]=='@')[0])-1

forklift=[r for r in rolls if neigh(r)<=3]
            
print("Part 1:",len(forklift))

total=len(forklift)

while forklift!=[]:
    for f in forklift: extend_matrix[f]='.'
    rolls=[(np.where(extend_matrix=='@')[0][i],np.where(extend_matrix=='@')[1][i]) for i in range(len(np.where(extend_matrix=='@')[0]))]
    forklift=[r for r in rolls if neigh(r)<=3]
    total+=len(forklift)

print("Part 2:",total)

