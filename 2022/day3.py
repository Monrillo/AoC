# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:49:42 2026

@author: castelf
"""

from collections import Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day3.txt','r') as f: lines=f.readlines()

priority='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

score_1=0
for line in lines:
    mid=len(line.strip('\n'))//2
    share=[it for it in Counter(line.strip('\n')[:mid]) if it in Counter(line.strip('\n')[mid:])][0]
    score_1+=priority.index(share)+1

print("Part 1:",score_1)

score_2=0
for i in range(0,len(lines),3):
    a=lines[i].strip('\n')
    b=lines[i+1].strip('\n')
    c=lines[i+2].strip('\n')
    share=[it for it in Counter(a) if (it in Counter(b) and it in Counter(c))][0]
    score_2+=priority.index(share)+1

print("Part 2:",score_2)

