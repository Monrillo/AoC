# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 16:15:07 2026

@author: castelf
"""
import math

def fac_sum(n):
    return sum(i for i in range(1,n+1))

with open("C:\\Users\castelf\Documents\GitHub\AoC\\2021\day7.txt") as f:
        positions = list(map(int, f.read().split(',')))

#positions = [16,1,2,0,4,2,7,1,2,14]

mean=sum(positions)/len(positions)
var=sum((p-mean)**2 for p in positions)/len(positions)
std=math.sqrt(var)

ecart={}
ecart_2={}

for e in range(round(mean)-round(std),round(mean)+round(std)+1):
    ecart[e]=sum(abs(p-e) for p in positions)

for e in range(round(mean)-10,round(mean)+11):
    ecart_2[e]=sum(fac_sum(abs(p-e)) for p in positions)

print("Part 1:",min(ecart.values()))

print("Part 2:",min(ecart_2.values()))
