# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:06:26 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day7.txt','r') as f:
    lines=f.readlines()

# Taken from barnybug
def abba(x):
    return any(a==d and b==c and a!=b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))

# Idea from barnybug
def aba(x,y):
    return any(a==c and a!=b and b+a+b in y for a,b,c in zip(x, x[1:], x[2:]))

res=0
new_res=0
for line in lines:
    parts = re.split(r'\[([^\]]+)\]', line)
    oob=' '.join(parts[0::2])
    inb=' '.join(parts[1::2])
    if abba(oob) and not abba(inb): res+=1
    if aba(oob,inb): new_res+=1

print(res)
print(new_res)

