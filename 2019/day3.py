# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 14:50:45 2025

@author: castelf
"""
from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day3.txt','r') as f: lines=f.readlines()

lines=['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

line1=lines[0].strip().split(',')
line2=lines[1].strip().split(',')

wire1=deque()
wire2=deque()

pos=(0,0)
wire1.append(pos)
for dep in line1:
    if dep[0]=='L':
        for i in range(int(dep[1:])):pos=(pos[0],pos[1]-1);wire1.append(pos)
    elif dep[0]=='R':
        for i in range(int(dep[1:])):pos=(pos[0],pos[1]+1);wire1.append(pos)
    elif dep[0]=='U':
        for i in range(int(dep[1:])):pos=(pos[0]+1,pos[1]);wire1.append(pos)
    elif dep[0]=='D':
        for i in range(int(dep[1:])):pos=(pos[0]-1,pos[1]);wire1.append(pos)

pos=(0,0)
wire2.append(pos)
for dep in line2:
    if dep[0]=='L':
        for i in range(int(dep[1:])):pos=(pos[0],pos[1]-1);wire2.append(pos)
    elif dep[0]=='R':
        for i in range(int(dep[1:])):pos=(pos[0],pos[1]+1);wire2.append(pos)
    elif dep[0]=='U':
        for i in range(int(dep[1:])):pos=(pos[0]+1,pos[1]);wire2.append(pos)
    elif dep[0]=='D':
        for i in range(int(dep[1:])):pos=(pos[0]-1,pos[1]);wire2.append(pos)

cross=[x for x in wire1 if x in wire2]
print(min([abs(c[0])+abs(c[1]) for c in cross[1:]]))
print(min([list(wire1).index(c)+list(wire1).index(c) for c in cross[1:]]))
