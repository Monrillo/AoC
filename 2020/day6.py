# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:02:03 2025

@author: castelf
"""

#import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day6.txt','r') as f: lines=f.readlines()

# lines=['abc',
# '',
# 'a',
# 'b',
# 'c',
# '',
# 'ab',
# 'ac',
# '',
# 'a',
# 'a',
# 'a',
# 'a',
# '',
# 'b']

forms=[]
f=''
for line in lines:
    if len(line.strip())==0:forms.append(set(f));f=''
    else: f+=line.strip()
forms.append(set(f))

print("Part 1:",sum([len(f) for f in forms]))

n=0
for line in lines:
    elems=set(line.strip())
    if len(elems)==0:n+=1
    else: forms[n]&=elems

print("Part 2:",sum([len(f) for f in forms]))

