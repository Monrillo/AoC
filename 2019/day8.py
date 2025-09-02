# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 11:30:17 2025

@author: castelf
"""
import numpy as np
from collections import Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day8.txt','r') as f: data=list(f.read())

# data=list('123456789012')
# wide=3
# tall=2

wide=25
tall=6

layers=np.reshape(data,(-1,wide*tall))
message=np.ones(wide*tall,dtype=int)*-1

zero=[]
one_two=[]
for lay in layers:
    counts=Counter(lay)
    zero.append(counts['0'])
    one_two.append(counts['1']*counts['2'])
    for t in np.where(lay=='1')[0]:
        if message[t]==-1:message[t]=1
    for t in np.where(lay=='0')[0]:
        if message[t]==-1:message[t]=0

print(one_two[zero.index((min(zero)))])

message=np.reshape(message,(-1,wide))
print(message)
