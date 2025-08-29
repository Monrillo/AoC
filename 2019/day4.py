# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:38:29 2025

@author: castelf
"""
from collections import deque

def check(n):
    if any(a==b for a,b in zip(str(n),str(n)[1:])) and all(int(b)>=int(a) for a,b in zip(str(n),str(n)[1:])): return True
    else: return False

res=deque()
for i in range(278384,824796):
    if check(i):res.append(i)

print(len(res))

def check2(n):
    double={}
    for a,b in zip(str(n),str(n)[1:]):
        if a==b:
            if a in double.keys(): double[a]+=1
            else: double[a]=1
    if 1 in double.values(): return True
    else: return False

res2=deque()
for i in res:
    if check2(i): res2.append(i)

print(len(res2))
