# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 14:27:00 2026

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day3.txt','r') as f: code=f.read()

total_1=total_2=0
enable=True
for it in re.finditer(r'mul\((\d+),(\d+)\)|don\'t\(\)|do\(\)', code):
    if it.group()[:3]=='don':enable=False
    elif it.group()[:3]=='do(':enable=True
    else:
        total_1+=int(it.groups()[0])*int(it.groups()[1])
        if enable:
            total_2+=int(it.groups()[0])*int(it.groups()[1])
    
print("Part 1:",total_1)

print("Part 2:",total_2)
