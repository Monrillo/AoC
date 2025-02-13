# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:29:35 2025

@author: castelf
"""

num_elves=3001330

elf={}
for i in range(1,num_elves+1): elf[i]=1

steal=True
while len(elf)>1:
    stolen=[]
    for k in elf.keys():
        if steal: vol=k; steal=False
        elif not steal: elf[vol]+=elf[k];steal=True;stolen.append(k)
    for k in stolen: del elf[k] 

print(list(elf.keys())[0])
