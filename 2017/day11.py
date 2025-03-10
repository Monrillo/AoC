# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:42:32 2025

@author: castelf
"""

from collections import deque

line=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day11.txt','r').read().split(',')

v=0
h=0

dist=deque([])
for d in line:
    if d=='n': v+=1
    elif d=='s': v-=1
    elif d=='nw': v+=1;h-=1
    elif d=='se': v-=1;h+=1
    elif d=='ne': h+=1
    elif d=='sw': h-=1
    eloig=max(abs(v), abs(h))
    dist.append(eloig)
print(dist[-1])
print(max(dist))
