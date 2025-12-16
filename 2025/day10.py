# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 13:34:21 2025

@author: castelf
"""

import numpy as np
import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day10.txt','r') as f: lines=f.readlines()

# lines=['[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
# '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
# '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']

def light_out(length,button,clic):
    lights=np.ones(length,dtype=int)*-1
    for c in clic:lights[button[c]]*=-1
    return lights

resultat=0
for line in lines:
    elems=line.strip().split(' ')
    l_good=[-1 if x=='.' else 1 for x in list(elems[0])[1:-1]]
    inter=[[int(x) for x in elems[i][1:-1].split(',')] for i in range(1,len(elems)-1)]
    
    res=None
    for i in range(1,len(inter)+1):
        for prop in it.permutations(range(len(inter)), i):
            if np.array_equiv(light_out(len(l_good),inter,prop), l_good): res=i;break
        else: continue
        break
    resultat+=res
            
print("Part 1:",resultat)
