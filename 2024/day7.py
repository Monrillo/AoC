# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:55:11 2026

@author: castelf
"""
from tqdm import tqdm
import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day7.txt','r') as f: lines=f.readlines()

# lines=['190: 10 19',
# '3267: 81 40 27',
# '83: 17 5',
# '156: 15 6',
# '7290: 6 8 6 15',
# '161011: 16 10 13',
# '192: 17 8 14',
# '21037: 9 7 18 13',
# '292: 11 6 16 20']

def compute(n,o):
    res=n[0]
    for i in range(len(o)):
        if o[i]=='|':
            res+=n[i+1]
        else:
            res=str(eval(res+o[i]+n[i+1]))
    return int(res)


resultat_1=0
incorrect=[]
for line in lines:
    res=int(line.strip('\n').split(': ')[0])
    nums=line.strip('\n').split(': ')[1].split(' ')
    if any(compute(nums,ops)==res for ops in it.product('*+', repeat=len(nums)-1)):
        resultat_1+=res
    else:
        incorrect.append([res,nums])

print("Part 1:",resultat_1)

resultat_2=resultat_1
for i in tqdm(range(len(incorrect))):
    res,nums=incorrect[i]
    if any(compute(nums,ops)==res for ops in it.product('*+|', repeat=len(nums)-1)):
        resultat_2+=res

print("Part 2:",resultat_2)

