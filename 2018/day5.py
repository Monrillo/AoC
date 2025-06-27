# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 10:53:43 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day5.txt','r') as f: line=f.read()

#line='dabAcCaCBAcCcaDA'

def polymer(l):
    n=0
    tot=len(l)-2
    while True:
        if abs(ord(l[n])-ord(l[n+1]))==32:
            l=l[:n]+l[n+2:]
            tot-=2
            if n>0: n-=1
        else:
            n+=1
            if n>=tot:break
    return len(l)

print(polymer(line))

import string

res=[]
for l,u in zip(list(string.ascii_lowercase),list(string.ascii_uppercase)):
    newline=line.replace(l,'')
    newline=newline.replace(u,'')
    res.append(polymer(newline))

print(min(res))
