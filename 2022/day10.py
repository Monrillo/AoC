# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:25:07 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day10.txt','r') as f: lines=f.readlines()

reg=1
cycle=0
signal=[]
printing=''

for line in lines:
    instr=line.strip('\n')
    if instr=='noop':
        cycle+=1
        if cycle in [20,60,100,140,180,220]:signal.append(reg*cycle)
        if reg-1<=(cycle-1)%40<=reg+1:printing+='#'
        else:printing+=' '
    else:
        _,n=instr.split(' ')
        cycle+=1
        if cycle in [20,60,100,140,180,220]:signal.append(reg*cycle)
        if reg-1<=(cycle-1)%40<=reg+1:printing+='#'
        else:printing+=' '
        cycle+=1
        if cycle in [20,60,100,140,180,220]:signal.append(reg*cycle)
        if reg-1<=(cycle-1)%40<=reg+1:printing+='#'
        else:printing+=' '
        reg+=int(n)

print("Part 1:",sum(signal))

print("Part 2:")
for l in range(6):
    print(printing[l*40:l*40+39])

