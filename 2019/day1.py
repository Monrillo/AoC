# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:21:46 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day1.txt','r') as f: lines=f.readlines()

def comp(n): return(n//3-2)
def comp_add(n):
    na=comp(n)
    res=na
    while comp(na)>=0:
        na=comp(na)
        res+=na
    return res

print("Part1 :",sum([comp(n) for n in [int(l.strip()) for l in lines]]))
print("Part2 :",sum([comp_add(n) for n in [int(l.strip()) for l in lines]]))
