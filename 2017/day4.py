# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 10:25:21 2025

@author: castelf
"""

import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day4.txt','r') as f: lines=f.readlines()

def anagram(w1,w2):
    for w in it.permutations(w2,len(w2)):
        if ''.join(w)==w1: return True; break
    return False

res1=0
res2=0
for line in lines:
    words=line.split()
    good1=True
    good2=True
    for i in range(len(words)):
        for j in range(len(words)):
            if i!=j and words[i]==words[j]: good1=False
            if i!=j and anagram(words[i],words[j]): good2=False
    if good1: res1+=1
    if good2: res2+=1

print('p1: '+str(res1))
print('p2: '+str(res2))
