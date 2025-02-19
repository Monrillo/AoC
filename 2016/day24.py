# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:34:31 2025

@author: castelf
"""

import numpy as np

mat=[list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day24.txt','r')]

lines=['###########',
'#0.1.....2#',
'#.#######.#',
'#4.......3#',
'###########']
mat=[list(line.strip()) for line in lines]

area=np.empty((len(mat),len(mat[0])),dtype=str)
for r in range(len(mat)):
    for c in range(len(mat[0])):
        area[r][c]=mat[r][c]

print(area)

np.where(area=='0')
