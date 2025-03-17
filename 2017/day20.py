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

d=[0]*len(particles)
for _ in range(1000):
    for i,p in enumerate(particles):
        p[3]+=p[6]
        p[4]+=p[7]
        p[5]+=p[8]
        p[0]+=p[3]
        p[1]+=p[4]
        p[2]+=p[5]
        d[i]=abs(p[0])+abs(p[1])+abs(p[2])
print(d.index(min(d)))
