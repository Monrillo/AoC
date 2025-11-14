# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:40:23 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day18.txt','r') as f: lines=f.readlines()

l=lines[0].strip()
eval(l)

re.findall(r'\(\w+\)', l)
for i in re.finditer(r'\(\w+\)', l):print(i)

re.search(r"\((\w+)\)", l)
list(l)


ltest='1 + 2 * 3 + 4 * 5 + 6'

def calc(line):
    nums=re.findall('\d+', line)
    ops=[x for x in line if x in ['+','*']]
    res=int(nums.pop(0))
    while ops!=[]:
        res=eval(str(res)+ops.pop(0)+nums.pop(0))
    return res

calc(ltest)