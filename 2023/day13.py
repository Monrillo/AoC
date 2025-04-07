# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:48:21 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day13.txt','r') as f: lines=f.readlines()

#for line in lines: print(line.strip())

lines=['#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.',
'',
'#...##..#',
'#....#..#',
'..##..###',
'#####.##.',
'#####.##.',
'..##..###',
'#....#..#']

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

def modify(m):
    for c in range(m.shape[1]):
        ce=(2*c-m.shape[1])
        if ce>0: check=np.array_equiv(m[:,ce:c], np.fliplr(m[:,c:2*c]))
        else: check=np.array_equiv(m[:,:c], np.fliplr(m[:,c:2*c]))
    for r in range(m.shape[0]):
        re=(2*r-m.shape[0])
        if re>0:
            if np.array_equiv(m[re:r,:], np.flipud(m[r:2*r,:])): score+=r*100
        else:
            if np.array_equiv(m[:r,:], np.flipud(m[r:2*r,:])): score+=r*100
    return 

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

import numpy as np

def mirrorpos(arr, axis=0, diff=0):
    m = np.array(arr, dtype=int)
    if axis == 1:
        m = m.T
    for i in range(m.shape[0] - 1):
        upper_flipped = np.flip(m[: i + 1], axis=0)
        lower = m[i + 1 :]
        rows = min(upper_flipped.shape[0], lower.shape[0])
        if np.count_nonzero(upper_flipped[:rows] - lower[:rows]) == diff:
            return i + 1
    return 0

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day13.txt', "r") as file:
    data = file.read().split("\n\n")
for i in range(2):
    total = 0
    for puzzle in data:
        arr = []
        for line in puzzle.splitlines():
            arr.append([*line.strip().replace(".", "0").replace("#", "1")])
        total += 100 * mirrorpos(arr, axis=0, diff=i) + mirrorpos(arr, axis=1, diff=i)
    print(total)