# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:54:04 2025

@author: castelf
"""

import numpy as np
sp=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day2.txt',dtype=int)
res=0
res2=0
for line in sp:
    res+=(np.max(line)-np.min(line))
    for el1 in line:
        for el2 in line:
            if el1!=el2 and el1%el2==0: res2+=el1//el2;break
print('p1 : '+str(res))
print('p2 : '+str(res2))