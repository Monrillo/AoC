# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:58:37 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day10.txt','r') as f: lines=f.readlines()

# lines=['89010123',
# '78121874',
# '87430965',
# '96549874',
# '45678903',
# '32019012',
# '01329801',
# '10456732']

matrix=np.array([[int(x) for x in list(l.strip('\n'))]for l in lines])   

path=[[(np.where(matrix==9)[0][i],np.where(matrix==9)[1][i])] for i in range(len(np.where(matrix==9)[0]))]
good_path=[]

while len(path)>0:
    p=path.pop(0)
    pos=p[-1]
    if matrix[pos]==0:good_path.append(p)
    else:
        if pos[0]-1>=0 and matrix[pos[0]-1,pos[1]]==matrix[pos]-1:path.append(p+[(pos[0]-1,pos[1])])
        if pos[0]+1<matrix.shape[0] and matrix[pos[0]+1,pos[1]]==matrix[pos]-1:path.append(p+[(pos[0]+1,pos[1])])
        if pos[1]-1>=0 and matrix[pos[0],pos[1]-1]==matrix[pos]-1:path.append(p+[(pos[0],pos[1]-1)])
        if pos[1]+1<matrix.shape[1] and matrix[pos[0],pos[1]+1]==matrix[pos]-1:path.append(p+[(pos[0],pos[1]+1)])

trailhead={}  
for p in good_path:
    if p[-1] not in trailhead.keys():trailhead[p[-1]]=set();trailhead[p[-1]].add(p[0])
    else:trailhead[p[-1]].add(p[0])

print("Part 1:",sum(len(v) for v in trailhead.values()))

print("Part 2:",len(good_path))

