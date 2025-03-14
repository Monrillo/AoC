# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:47:48 2025

@author: castelf
"""

# Part 1
prog = [0]
index=0
cpt=0
for _ in range(2017):
    index=(index+335)%len(prog)+1
    cpt+=1
    prog.insert(index, cpt)
print(prog[prog.index(2017)+1])

#Part 2

len_prog=1
index=0
cpt=0
for _ in range(50000000):
    index=(index+335)%len_prog+1
    cpt+=1
    len_prog+=1
    if index==1: res=cpt
print(res)