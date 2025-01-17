# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:08:14 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day1.txt','r') as f:
    instr=f.read().split(', ')

# test='R2, R2, R2'
# instr=test.split(', ')

direction='NESW'
dir_num=0
x=0
y=0

path=[]
revis=[]
for ins in instr:
    if ins[0]=='L':
        dir_num-=1
        dir_num=dir_num%len(direction)  
    elif ins[0]=='R':
        dir_num+=1
        dir_num=dir_num%len(direction)
    
    if direction[dir_num]=='N':
        y+=int(ins[1:])
    elif direction[dir_num]=='S':
        y-=int(ins[1:])
    elif direction[dir_num]=='E':
        x+=int(ins[1:])
    elif direction[dir_num]=='W':
        x-=int(ins[1:])
    
    if (x,y) in path:
        revis.append((x,y))
    path.append((x,y))
    

print(abs(x)+abs(y))
print(abs(revis[0][0])+abs(revis[0][1]))
