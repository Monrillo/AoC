# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 14:24:47 2025

@author: castelf
"""

import numpy as np

liste=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day9.txt',dtype=int)

# liste=np.array([[0,3,6,9,12,15],
# [1,3,6,10,15,21],
# [10,13,16,21,30,45]])

def deep(li):
    step=0
    while not all(val == 0 for val in li): li=np.diff(li);step+=1
    return step

result=0
for l in liste:
    res=0
    for i in range(deep(l),-1,-1):
        cp=l.copy()
        for _ in range(i): cp=np.diff(cp)
        res+=cp[-1]
    result+=res
print(result)

result=0
for l in liste:
    l=l[::-1]
    res=0
    for i in range(deep(l),-1,-1):
        cp=l.copy()
        for _ in range(i): cp=np.diff(cp)
        res+=cp[-1]
    result+=res
print(result)
