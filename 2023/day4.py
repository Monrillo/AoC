# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:06:11 2025

@author: castelf
"""

import numpy as np

nums=[line.strip().split(': ')[1].split(' | ') for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day4.txt','r').readlines()]

# lines=['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
# nums=[line.strip().split(': ')[1].split(' | ') for line in lines]

result=0
queue=np.ones(len(nums),dtype=int)
for i,num in enumerate(nums):
    wins=[int(x) for x in num[0].split()]
    list_nums=[int(x) for x in num[1].split()]
    tot=0
    for n in wins:
        if n in list_nums:tot+=1
    if tot>0:
        result+=2**(tot-1)
        queue[i+1:i+tot+1]+=queue[i]
print(result)
print(np.sum(queue))