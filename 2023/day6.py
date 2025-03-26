# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 15:43:09 2025

@author: castelf
"""

import math

# Time:        61     70     90     66
# Distance:   643   1184   1362   1041

time=[61,70,90,66]
distance=[643,1184,1362,1041]

# time=[7,15,30]
# distance=[9,40,200]

pos=[]
tot_t=''
tot_d=''
for t,d in zip(time,distance):
    ways=0
    tot_t+=str(t)
    tot_d+=str(d)
    for s in range(t):
        if ((t-s)*s)>d: ways+=1
    pos.append(ways)

print(math.prod(pos))

tot_t=int(tot_t)
tot_d=int(tot_d)
ways=0
for s in range(tot_t):
    if ((tot_t-s)*s)>tot_d: ways+=1
print(ways)
