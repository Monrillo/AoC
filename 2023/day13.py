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


lines.append('')

score=0
mat=[]
for line in lines:
    if line.strip()!='':mat.append(list(line.strip()))
    else:
        matrix=np.array(mat)
        for c in range(matrix.shape[1]):
            ce=(2*c-matrix.shape[1])
            if ce>0:
                if np.array_equiv(matrix[:,ce:c], np.fliplr(matrix[:,c:2*c])): score+=c
            else:
                if np.array_equiv(matrix[:,:c], np.fliplr(matrix[:,c:2*c])): score+=c
        for r in range(matrix.shape[0]):
            re=(2*r-matrix.shape[0])
            if re>0:
                if np.array_equiv(matrix[re:r,:], np.flipud(matrix[r:2*r,:])): score+=r*100
            else:
                if np.array_equiv(matrix[:r,:], np.flipud(matrix[r:2*r,:])): score+=r*100
        mat=[]
print(score)

