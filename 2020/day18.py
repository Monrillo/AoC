# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:40:23 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day18.txt','r') as f: lines=f.readlines()

def calc(line):
    nums=[x for x in line if x not in ['+','*']]
    ops=[x for x in line if x in ['+','*']]
    res=int(nums.pop(0))
    while ops!=[]:
        res=eval(str(res)+ops.pop(0)+nums.pop(0))
    return res

def calc_2(line):
    l=line.copy()
    plus = [i for i, x in enumerate(l) if x == '+']
    for p in plus[::-1]:
        res=eval(''.join(l[p-1:p+2]))
        del l[p-1:p+2]
        l.insert(p-1,str(res))
    return eval(''.join(l))

resultat=0

for l in lines:
    l=l.strip().replace('(', '( ').replace(')', ' )').split(' ')
    indices = [i for i, x in enumerate(l) if x == '(']
    for i in indices[::-1]:
        end = [s for s, x in enumerate(l) if x == ')' and s>i].pop(0)
        res=calc(l[i+1:end])
        del l[i:end+1]
        l.insert(i,str(res))
    resultat+=(calc(l))

print("Part 1:",resultat)

resultat=0

for l in lines:
    l=l.strip().replace('(', '( ').replace(')', ' )').split(' ')
    indices = [i for i, x in enumerate(l) if x == '(']
    for i in indices[::-1]:
        end = [s for s, x in enumerate(l) if x == ')' and s>i].pop(0)
        res=calc_2(l[i+1:end])
        del l[i:end+1]
        l.insert(i,str(res))
    resultat+=(calc_2(l))

print("Part 2:",resultat)
