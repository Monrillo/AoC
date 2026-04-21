# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:29:08 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day1.txt','r') as f: lines=f.readlines()

carrying=[]
elf=0
for line in lines:
    if line.strip('\n')=='':carrying.append(elf);elf=0
    else: elf+=int(line.strip('\n'))

print("Part 1:",sorted(carrying)[-1])

print("Part 2:",sum(sorted(carrying)[-3:]))
