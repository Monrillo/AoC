# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:14:52 2026

@author: castelf
"""
from collections import Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day1.txt','r') as f: lines=f.readlines()

l0=sorted([int(line.strip('\n').split()[0]) for line in lines])
l1=sorted([int(line.strip('\n').split()[1]) for line in lines])

print("Part 1:",sum(abs(l1[i]-l0[i]) for i in range(len(l0))))

count=Counter(l1)

print("Part 2:",sum(n*count[n] for n in l0))

