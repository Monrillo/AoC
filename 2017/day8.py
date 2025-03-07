# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 16:31:49 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day8.txt','r') as f: lines=f.readlines()

def evaluate(op):
    return eval(str(reg[op.split()[0]])+op.split()[1]+op.split()[2])

def oper(op):
    if op.split()[1]=='inc': reg[op.split()[0]]+=int(op.split()[2])
    elif op.split()[1]=='dec': reg[op.split()[0]]-=int(op.split()[2])

reg={}
res=[]
for line in lines:
    inst=line.strip().split(' if ')
    try:
        reg[inst[1].split()[0]]
    except:
        reg[inst[1].split()[0]]=0
    try:
        reg[inst[0].split()[0]]
    except:
        reg[inst[0].split()[0]]=0
    if evaluate(inst[1]): oper(inst[0])
    res.append(max(reg.values()))

print(res[-1])
print(max(res))
