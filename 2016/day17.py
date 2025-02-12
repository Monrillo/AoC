# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:32:19 2025

@author: castelf
"""

import numpy as np
from hashlib import md5
import re


def move(w):
    h=md5(w[2].encode()).hexdigest()
    pos_m=[]
    for i,c in enumerate(h[:4]):
        if re.match(r'b|c|d|e|f',c):
            if i==0 and w[1]>1: pos_m.append([w[0],w[1]-1,w[2]+'U'])
            elif i==1 and w[1]<4: pos_m.append([w[0],w[1]+1,w[2]+'D'])
            elif i==2 and w[0]>1: pos_m.append([w[0]-1,w[1],w[2]+'L'])
            elif i==3 and w[0]<4: pos_m.append([w[0]+1,w[1],w[2]+'R'])
    return pos_m

code='edjrjqaa'
pos=[1,1,code] # finish point is at 4,4
path=[pos]

good_way=[]
while len(path)>0:
    p=path.pop(0)
    if p[0]==p[1]==4: good_way.append(p[2][len(code):]);continue
    path+=move(p)

l=[len(x) for x in good_way]
p1=good_way[np.where(l==np.min(l))[0][0]]
p2=np.max(l)
print(p1)
print(p2)