# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 16:20:04 2025

@author: castelf
"""

import re

values=[re.findall('(-?\d+)', line) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day20.txt','r').readlines()]
particles=[[int(x) for x in val] for val in values]

# lines=['p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
# 'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>']
# values=[re.findall('(-?\d+)', line) for line in lines]
# particles=[[int(x) for x in val] for val in values]

# lines=['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
# 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
# 'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
# 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']
# values=[re.findall('(-?\d+)', line) for line in lines]
# particles=[[int(x) for x in val] for val in values]

d=[0]*len(particles)
col=[False]*len(particles)
for _ in range(500):
    pos=[]
    for i,p in enumerate(particles):
        p[3]+=p[6]
        p[4]+=p[7]
        p[5]+=p[8]
        p[0]+=p[3]
        p[1]+=p[4]
        p[2]+=p[5]
        d[i]=abs(p[0])+abs(p[1])+abs(p[2])
        pos.append((p[0],p[1],p[2]))
    for i,po in enumerate(pos):
        if pos.count(po)>1: col[i]=True
print(d.index(min(d)))
print(len(particles)-sum(col))

