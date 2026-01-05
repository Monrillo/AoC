# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 11:44:23 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day3.txt','r') as f: lines=f.readlines()

def bin_to_dec(l):
    return sum([2**i for i,e in enumerate(l[::-1]) if e=='1'])

data=['' for i in range(len(lines[0].strip('\n')))]

for line in lines:
    for i,x in enumerate(line.strip('\n')):
        data[i]+=x
        
gamma=''.join(['1' if d.count('1')>=d.count('0') else '0' for d in data])
epsilon=''.join(['1' if n=='0' else '0' for n in gamma])

epsilon_dec=bin_to_dec(epsilon)
gamma_dec=bin_to_dec(gamma)

print("Part 1:",epsilon_dec*gamma_dec)

data2=data.copy()
possib=range(len(data[0]))
for i in possib:
