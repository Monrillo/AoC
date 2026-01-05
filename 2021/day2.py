# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 11:16:31 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day2.txt','r') as f: lines=f.readlines()

depth=depth2=0
pos=0
aim=0
for line in lines:
    if line.strip('\n').split(' ')[0]=='forward':
        pos+=int(line.strip('\n').split(' ')[1])
        depth2+=int(line.strip('\n').split(' ')[1])*aim
    elif line.strip('\n').split(' ')[0]=='up':
        depth-=int(line.strip('\n').split(' ')[1])
        aim-=int(line.strip('\n').split(' ')[1])
    elif line.strip('\n').split(' ')[0]=='down':
        depth+=int(line.strip('\n').split(' ')[1])
        aim+=int(line.strip('\n').split(' ')[1])

print("Part 1:",pos*depth)
print("Part 2:",pos*depth2)

