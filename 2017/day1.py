# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:16:44 2025

@author: castelf
"""

line=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day1.txt','r').read()
circ=line+line[0]
res=0
for a,b in zip(circ, circ[1:]):
    if a==b: res+=int(a)
print('p1: '+str(res))
res2=0
for a,b in zip(circ, circ[len(line)//2:]):
    if a==b: res2+=2*int(a)
print('p2: '+str(res2))


