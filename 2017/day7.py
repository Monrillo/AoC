# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 13:52:35 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day7.txt','r') as f: lines=f.readlines()

nodes=[]
score=[]
fils=[]
for line in lines:
    ins=line.strip().split(' -> ')
    x=re.findall(r'(\w+) \((\d+)\)',ins[0])
    node,num=x[0]
    nodes.append(node)
    score.append(int(num))
    if len(ins)==2: fils.append(ins[1])
progs=''.join(fils)


for node in nodes:
    if node not in progs: print(node)
