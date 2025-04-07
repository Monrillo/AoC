# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:48:21 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day13.txt','r') as f: lines=f.readlines()

#for line in lines: print(line.strip())

# lines=['#.##..##.',
# '..#.##.#.',
# '##......#',
# '##......#',
# '..#.##.#.',
# '..##..##.',
# '#.#.##.#.',
# '',
# '#...##..#',
# '#....#..#',
# '..##..###',
# '#####.##.',
# '#####.##.',
# '..##..###',
# '#....#..#']

def score(m):
    score=0
    for c in range(m.shape[1]):
        ce=(2*c-m.shape[1])
        if ce>0:
            if np.array_equiv(m[:,ce:c], np.fliplr(m[:,c:2*c])): score+=c
        else:
            if np.array_equiv(m[:,:c], np.fliplr(m[:,c:2*c])): score+=c
    for r in range(m.shape[0]):
        re=(2*r-m.shape[0])
        if re>0:
            if np.array_equiv(m[re:r,:], np.flipud(m[r:2*r,:])): score+=r*100
        else:
            if np.array_equiv(m[:r,:], np.flipud(m[r:2*r,:])): score+=r*100
    return score

lines.append('')

score_tot=0
mat=[]
for line in lines:
    if line.strip()!='':mat.append(list(line.strip()))
    else:
        matrix=np.array(mat)
        score_tot+=score(matrix)
        mat=[]
print(score_tot)

