# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 13:27:13 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day2.txt','r') as f: lines=f.readlines()

reports=[[int(x) for x in line.strip('\n').split()] for line in lines]

def check(rep):
    sens=-1 if rep[1]<rep[0] else 1
    safe=all(b==a+sens*1 or b==a+sens*2 or b==a+sens*3 for a,b in zip(rep,rep[1:]))
    return safe

print("Part 1:",sum(check(r) for r in reports))

print("Part 2:",sum(any(check(r[0:i]+r[i+1:]) for i in range(len(r))) for r in reports))

