# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 10:00:12 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day1.txt','r') as f: lines=f.readlines()

data=[int(l.strip('\n')) for l in lines]
    
print("Part 1:",sum(1 for a,b in zip(data,data[1:]) if a<b))

sums=[sum((a,b,c)) for a,b,c in zip(data,data[1:],data[2:])]

print("Part 2:",sum(1 for a,b in zip(sums,sums[1:]) if a<b))