# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 11:44:23 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day3.txt','r') as f: lines=f.readlines()

# lines=['00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010']

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

data2=[list(d) for d in data]
oxygen=''
while data2:
    d=data2.pop(0)
    if len(d)>1:
        common='1' if d.count('1')>=d.count('0') else '0'
        ignore=[i for i,x in enumerate(d) if x!=common]
    else:
        common=d[0]
        ignore=[]
    oxygen+=common
    
    for j in range(len(data2)):
        for i in ignore[::-1]:
            data2[j].pop(i)

data2=[list(d) for d in data]
co=''
while data2:
    d=data2.pop(0)
    if len(d)>1:
        least='0' if d.count('0')<=d.count('1') else '1'
        ignore=[i for i,x in enumerate(d) if x!=least]
    else:
        least=d[0]
        ignore=[]
    co+=least
    
    for j in range(len(data2)):
        for i in ignore[::-1]:
            data2[j].pop(i)

oxygen_dec=bin_to_dec(oxygen)
co_dec=bin_to_dec(co)

print("Part 2:",oxygen_dec*co_dec)

