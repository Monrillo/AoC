# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 14:26:35 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day5.txt','r') as f: lines=f.readlines()

lines=['3-5',
'10-14',
'16-20',
'12-18',
'',
'1',
'5',
'8',
'11',
'17',
'32']

recipe=True
good=[]
ingredients=[]
for l in lines:
    if l.strip()=='':recipe=False
    elif recipe:
        a,b=l.strip().split('-')
        good.append([int(a),int(b)])
    else:
        ingredients.append(int(l.strip()))

good_ingredients=[i for i in ingredients if any(g[0]<=i<=g[1] for g in good)]

print("Part 1:",len(good_ingredients))

good=np.array(good)
good[good[:,0]==np.min(good[:,0])][0]


good.pop(np.where(good[:,0]==np.min(good[:,0]))[0][0])
