# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:28:00 2025

@author: castelf
"""

ins=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day12.txt','r')]
#Part 1
reg={'a':0,'b':0,'c':0,'d':0}
#Part 2
reg={'a':0,'b':0,'c':1,'d':0}
cpt=0
while cpt<len(ins):
    l=ins[cpt]
    if l[0]=='inc': reg[l[1]]+=1
    elif l[0]=='dec': reg[l[1]]-=1
    elif l[0]=='cpy':
        try: reg[l[2]]=int(l[1])
        except: reg[l[2]]=reg[l[1]]
    elif l[0]=='jnz':
        try:
            if int(l[1])!=0:
                cpt+=int(l[2]);continue
        except:
            if reg[l[1]]!=0:
                cpt+=int(l[2]);continue
    cpt+=1
print(reg['a'])
