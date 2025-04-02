# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 15:43:40 2025

@author: castelf
"""

import numpy as np
import itertools as it

matrix=np.array([list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day11.txt','r')])

# lines=['...#......',
# '.......#..',
# '#.........',
# '..........',
# '......#...',
# '.#........',
# '.........#',
# '..........',
# '.......#..',
# '#...#.....']
# matrix=np.array([list(line.strip()) for line in lines])

row=[]
col=[]
for i in range(len(matrix)):
    if not '#' in matrix[i]:row.append(i)
    if not '#' in matrix[:,i]:col.append(i)

def distance(g1,g2,r,c,exp):
    x=abs(g1[0]-g2[0])
    y=abs(g1[1]-g2[1])
    for i in r:
        if min(g1[0],g2[0])<i<max(g1[0],g2[0]):x+=exp
    for i in c:
        if min(g1[1],g2[1])<i<max(g1[1],g2[1]):y+=exp
    return x+y

gal=[(np.where(matrix=='#')[0][i],np.where(matrix=='#')[1][i]) for i in range(len(np.where(matrix=='#')[0]))]

res1=res2=0
for c in it.combinations(gal, 2): res1+=distance(c[0],c[1],row,col,1);res2+=distance(c[0],c[1],row,col,999999)
print('Part 1: ',res1)
print('Part 2: ',res2)
