# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:49:23 2025

@author: castelf
"""

goal=347991

odd=1
while True:
    if odd**2>=goal: break
    odd+=2

s=(odd**2)-(odd//2)
p=[abs(s-goal),abs(s-(odd-1)-goal),abs(s-(odd-1)*2-goal),abs(s-(odd-1)*3-goal)]

print(min(p)+(odd//2))

# From oantolin

from itertools import count

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x

part2(goal)
