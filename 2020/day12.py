# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 10:08:21 2025

@author: castelf
"""
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day12.txt','r') as f: lines=f.readlines()

#move={'E':0,'S':0,'W':0,'N':0}
direction=['E','S','W','N']
pos=[0,0]

def turn(d):
    global direction
    if d=='L': direction=list(direction[-1])+direction[:-1]
    elif d=='R': direction=direction[1:]+list(direction[0])

def move(line):
    global pos
    if line[0]=='N': pos[1]+=int(line[1:])
    elif line[0]=='S': pos[1]-=int(line[1:])
    elif line[0]=='E': pos[0]+=int(line[1:])
    elif line[0]=='W': pos[0]-=int(line[1:])

for l in lines:
    if l[0]=='F': move(direction[0]+l[1:].strip())
    elif l[0]=='L' or l[0]=='R':
        for _ in range(int(l[1:].strip())//90):
            turn(l[0])
    else: move(l.strip())

distance=abs(pos[0])+abs(pos[1])
print("Part 1:",distance)

pos_b=np.array([0,0])
pos_w=np.array([10,1])

# Rotation matrixes
left=np.array([[0,-1],[1,0]])
right=np.array([[0,1],[-1,0]])

def move_2(line):
    global pos_b
    global pos_w
    if line[0]=='N': pos_w[1]+=int(line[1:])
    elif line[0]=='S': pos_w[1]-=int(line[1:])
    elif line[0]=='E': pos_w[0]+=int(line[1:])
    elif line[0]=='W': pos_w[0]-=int(line[1:])
    elif line[0]=='F': pos_b+=pos_w*int(line[1:])
    elif line[0]=='L':
        for _ in range(int(line[1:])//90): pos_w=np.dot(left,pos_w)
    elif line[0]=='R':
        for _ in range(int(line[1:])//90): pos_w=np.dot(right,pos_w)

for l in lines: move_2(l.strip())

distance=abs(pos_b[0])+abs(pos_b[1])
print("Part 2:",distance)
