# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 15:03:30 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day4.txt','r') as f: lines=f.readlines()

lines=['..@@.@@@@.',
'@@@.@.@.@@',
'@@@@@.@.@@',
'@.@@@@..@.',
'@@.@@@@.@@',
'.@@@@@@@.@',
'.@.@.@.@@@',
'@.@@@.@@@@',
'.@@@@@@@@.',
'@.@.@@@.@.']

mat=[list(l.strip()) for l in lines]
matrix=np.array(mat)
extend_matrix=np.pad(matrix, ((1, 1), (1, 1)), 'constant', constant_values='.')
rolls=[(x,y) for x in np.where(extend_matrix=='@')[0] for y in np.where(extend_matrix=='@')[1]]

for roll in rolls:
    x,y=roll
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            print((x+dx,y+dy))
            
    

sum([(x+dx,y+dy) for dx in [-1,0,1] for dy in [-1,0,1]])
for dx in [-1,0,1]:print(dx)
