# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 10:03:46 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day2.txt','r') as f: lines=f.readlines()

valid=0
valid2=0
for l in lines:
    a,b=l.strip().split(': ')
    mi,ma=re.findall('\d+', a)
    if int(mi)<=b.count(a[-1])<=int(ma):valid+=1
    if (not b[int(mi)-1]==a[-1] and b[int(ma)-1]==a[-1]) or (b[int(mi)-1]==a[-1] and not b[int(ma)-1]==a[-1]):valid2+=1

print("Part 1:",valid)
print("Part 2:",valid2)
