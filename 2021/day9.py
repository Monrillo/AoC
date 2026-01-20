# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 09:45:18 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day9.txt','r') as f: lines=f.readlines()

# lines=['2199943210',
# '3987894921',
# '9856789892',
# '8767896789',
# '9899965678']

carte=[[int(x) for x in list(l.strip('\n'))] for l in lines]

minima=[]
risk=[]
for l in range(len(carte)):
    for c in range(len(carte[0])):
        neighbors=[]
        if l>0:neighbors.append(carte[l-1][c])
        if l<len(carte)-1:neighbors.append(carte[l+1][c])
        if c>0:neighbors.append(carte[l][c-1])
        if c<len(carte[0])-1:neighbors.append(carte[l][c+1])
        if all(carte[l][c]<x for x in neighbors):minima.append((l,c));risk.append(carte[l][c]+1)

print("Part 1:",sum(risk))

bassin_sizes=[]
for m in minima:
    bassin=[m]
    path=[m]
    while len(path)>0:
        l,c=path.pop(0)
        if l>0 and carte[l-1][c]!=9 and (l-1,c) not in bassin:bassin.append((l-1,c));path.append((l-1,c))
        if l<len(carte)-1 and carte[l+1][c]!=9 and (l+1,c) not in bassin:bassin.append((l+1,c));path.append((l+1,c))
        if c>0 and carte[l][c-1]!=9 and (l,c-1) not in bassin:bassin.append((l,c-1));path.append((l,c-1))
        if c<len(carte[0])-1 and carte[l][c+1]!=9 and (l,c+1) not in bassin:bassin.append((l,c+1));path.append((l,c+1))
    bassin_sizes.append(len(bassin))

bassin_max=[bassin_sizes.pop(bassin_sizes.index(max(bassin_sizes))) for _ in range(3)]

print("Part 2:",bassin_max[0]*bassin_max[1]*bassin_max[2])
