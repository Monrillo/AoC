# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 16:06:03 2026

@author: castelf
"""
import numpy as np
import time

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day15.txt','r') as f: lines=f.readlines()

# lines=['1163751742',
# '1381373672',
# '2136511328',
# '3694931569',
# '7463417111',
# '1319128137',
# '1359912421',
# '3125421639',
# '1293138521',
# '2311944581']

matrix=np.array([[int(x) for x in list(line.strip('\n'))]for line in lines])

matrix.shape

path=[[(0,0)]]
good_path=[]

start_time=time.time()
while len(path)>0:
    p=path.pop(0)
    pos=p[-1]
    if pos==(matrix.shape[0]-1,matrix.shape[1]-1):good_path.append(p)
    else:
        #if pos[0]-1>0 and not (pos[0]-1,pos[1]) in p:path.append(p+[(pos[0]-1,pos[1])])
        #if pos[0]+1<matrix.shape[0] and not (pos[0]+1,pos[1]) in p:path.append(p+[(pos[0]+1,pos[1])])
        #if pos[0]+1<matrix.shape[0]:path.append(p+[(pos[0]+1,pos[1])])
        if pos[0]+1<matrix.shape[0] and abs(pos[0]-pos[1])<5:path.append(p+[(pos[0]+1,pos[1])])
        #if pos[1]-1>0 and not (pos[0],pos[1]-1) in p:path.append(p+[(pos[0],pos[1]-1)])
        #if pos[1]+1<matrix.shape[1] and not (pos[0],pos[1]+1) in p:path.append(p+[(pos[0],pos[1]+1)])
        #if pos[1]+1<matrix.shape[1]:path.append(p+[(pos[0],pos[1]+1)])
        if pos[1]+1<matrix.shape[1] and abs(pos[0]-pos[1])<5:path.append(p+[(pos[0],pos[1]+1)])

total=[sum(matrix[e] for e in g) for g in good_path]
end_time=time.time()

print("Part 1:",min(total)-matrix[0,0])
print("Time",end_time-start_time)

#len(good_path)
