# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:47:40 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day14.txt','r') as f: lines=f.readlines()

# lines=['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
# 'mem[8] = 11',
# 'mem[7] = 101',
# 'mem[8] = 0']

memory={}

for l in lines:
    a,b=l.strip().split(' = ')
    if a=='mask': mask=b
    else:
        num=re.findall('mem\[(\d+)\]', a)
        k=int(num[0])
        bin_num=format(int(b), '036b')
        res=''.join([bin_num[i] if mask[i]=='X' else mask[i] for i in range(36)])
        memory[k]=res
        
print("Part 1:",sum(int(v, 2) for v in memory.values()))

def decoder(l):
    r=[l]
    while any('X' in e for e in r):
        for i in range(len(r)):
            if 'X' in r[i]: el=r.pop(i);break
        r.append(el.replace('X','0',1))
        r.append(el.replace('X','1',1))
    return r

# lines = ['mask = 000000000000000000000000000000X1001X',
# 'mem[42] = 100',
# 'mask = 00000000000000000000000000000000X0XX',
# 'mem[26] = 1']

memory={}

for l in lines:
    a,b=l.strip().split(' = ')
    if a=='mask': mask=b
    else:
        num=re.findall('mem\[(\d+)\]', a)
        k=int(num[0])
        bin_num=format(k, '036b')
        res=''.join([bin_num[i] if mask[i]=='0' else mask[i] for i in range(36)])
        for ad in decoder(res): memory[int(ad, 2)]=int(b)

print("Part 2:",sum(memory.values()))

