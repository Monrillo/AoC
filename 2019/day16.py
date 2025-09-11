# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:56:54 2025

@author: castelf
"""
import numpy as np
import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day16.txt','r') as f: signal=f.read()

#signal=str(12345678)
#signal=str(80871224585914546619083218645595)

cyc=it.cycle([0,1,0,-1])
phase_1=[next(cyc) for _ in range(len(signal)+1)]
mat_phase=np.repeat(phase_1,1)[1:len(signal)+1]
for n in range(2,len(signal)+1):
    mat_phase=np.vstack((mat_phase,np.repeat(phase_1,n)[1:len(signal)+1]))

num=np.array([int(s) for s in signal])
#matrix=np.tile(num,(len(signal),1))
for _ in range(100):
    num=np.array([int(str(n)[-1]) for n in np.sum(num*mat_phase, axis=1)])
    
print(num[:8])
    
# For part 2 I do not know and I picked up a solution


h = open("C:\\Users\castelf\Documents\GitHub\AoC\\2019\day16.txt").read()*10000
i = (h[int(h[0:7]):])
for a in range(100):
    print(a)
    string = '' 
    e = 0
    while e < len(i):
        if e == 0:
            total = 0
            for f in i:
                total += int(f)
        elif e > 0:
            total -= int(i[e-1])
        string += str(total)[-1]
        e+=1
    i = string
print(i[0:8])

