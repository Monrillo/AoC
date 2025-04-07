# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 16:24:02 2025

@author: castelf
"""

import numpy as np
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day3.txt','r') as f: lines=f.readlines()

# lines=['#1 @ 1,3: 4x4',
# '#2 @ 3,1: 4x4',
# '#3 @ 5,5: 2x2']

matrix=np.zeros((10000,10000),dtype=int)

for line in lines:
    num,r,c,lr,lc=re.findall('(\d+)', line)
    matrix[int(r):int(r)+int(lr),int(c):int(c)+int(lc)]+=1

print(len(np.where(matrix>1)[0]))

for line in lines:
    num,r,c,lr,lc=re.findall('(\d+)', line)
    if np.all(matrix[int(r):int(r)+int(lr),int(c):int(c)+int(lc)]==1):print(num)
