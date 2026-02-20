# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:38:37 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day9.txt','r') as f: disk=f.read()

#disk='2333133121414131402'

space=[]
nums=[]
num=0
for i,d in enumerate(disk):
    if i%2==0:nums.append([int(d),num])
    else:space.append(int(d));num+=1
    
checksum=0
spacing=False
position=0
while nums:
    if space[0]==0 and spacing:space.pop(0);spacing=False
    
    if spacing:
        checksum+=position*nums[-1][1]
        nums[-1][0]-=1
        if nums[-1][0]==0:nums.pop(-1)
        space[0]-=1
        if space[0]==0:space.pop(0);spacing=False
    else:
        checksum+=position*nums[0][1]
        nums[0][0]-=1    
        if nums[0][0]==0:nums.pop(0);spacing=True
    position+=1
    if space[0]<0:print(position);break

print("Part 1:",checksum)
