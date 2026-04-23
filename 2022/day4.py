# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:38:10 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day4.txt','r') as f: lines=f.readlines()

score_1=0
score_2=0
for line in lines:
    elf1,elf2=line.strip('\n').split(',')
    e1_min,e1_max=map(int,elf1.split('-'))
    e2_min,e2_max=map(int,elf2.split('-'))
    if e1_min<=e2_min and e1_max>=e2_max or e2_min<=e1_min and e2_max>=e1_max: score_1+=1
    if e1_max>=e2_min and e2_max>=e1_min or e1_min<=e2_max and e2_min<=e1_max: score_2+=1
print("Part 1:",score_1)

print("Part 2:",score_2)
