# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:37:18 2025

@author: castelf
"""

import time
import numpy as np
from collections import deque

start = time.time()
memory=deque([[4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]])
#memory=[[4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]]
#memory=[[0,2,7,0]]

while True:
    cycle=memory[-1].copy()
    pile=np.where(np.array(cycle)==np.max(np.array(cycle)))[0][0]
    tokens=cycle[pile]
    cycle[pile]=0
    for i in range(tokens): cycle[(pile+1+i)%len(cycle)]+=1
    if cycle in memory: break
    memory.append(cycle)

print(len(memory))
print(time.time() - start)

memory=deque([cycle])

while True:
    cycle=memory[-1].copy()
    pile=np.where(np.array(cycle)==np.max(np.array(cycle)))[0][0]
    tokens=cycle[pile]
    cycle[pile]=0
    for i in range(tokens): cycle[(pile+1+i)%len(cycle)]+=1
    if cycle in memory: break
    memory.append(cycle)

print(len(memory))
print(time.time() - start)
