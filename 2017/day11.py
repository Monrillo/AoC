# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:42:32 2025

@author: castelf
"""

import numpy as np
from collections import deque

line=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day11.txt','r').read().split(',')

f=0
l=0
r=0
dist=deque([])
for d in line:
    if d=='n': f+=1
    elif d=='s': f-=1
    elif d=='nw': l+=1
    elif d=='se': l-=1
    elif d=='ne': r+=1
    elif d=='sw': r-=1
    eloig=abs(f)
    if np.sign(f)==np.sign(r): eloig+=abs(r)
    elif abs(r)>abs(f): eloig+=abs(r)-abs(f)
    if np.sign(f)==np.sign(l): eloig+=abs(l)
    elif abs(l)>abs(f): eloig+=abs(l)-abs(f)
    dist.append(eloig)
print(dist[-1])
print(max(dist))
