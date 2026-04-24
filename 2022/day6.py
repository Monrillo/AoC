# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:54:18 2026

@author: castelf
"""
from collections import Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day6.txt','r') as f: line=f.read()

part1=False
part2=False
p=0
while not part1 or not part2:
    if not part1 and all(m==1 for m in Counter(line[p:p+4]).values()):
        print("Part 1:",p+4)
        part1=True
    if not part2 and all(m==1 for m in Counter(line[p:p+14]).values()):
        print("Part 2:",p+14)
        part2=True
    p+=1
