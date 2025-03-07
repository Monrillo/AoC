# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:11:07 2025

@author: castelf
"""

import re

line=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day9.txt','r').read()

#line='{{<a!>},{<a!>},{<a!>},{<ab>}}'
line=re.sub(r'!.','',line)

cpt=0
garbage=False
value=0
res=0
garb_car=0
while cpt<len(line):
    if garbage and line[cpt]!='>': garb_car+=1
    if line[cpt]=='<': garbage=True
    elif line[cpt]=='>': garbage=False
    elif line[cpt]=='{' and not garbage: value+=1
    elif line[cpt]=='}' and not garbage: res+=value;value-=1
    cpt+=1
print(res)
print(garb_car)