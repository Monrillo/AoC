# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 10:53:43 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day5.txt','r') as f: line=f.read()

#line='dabAcCaCBAcCcaDA'

noend=True
while noend:
    n=0
    for a,b in zip(line,line[1:]):
        if abs(ord(a)-ord(b))==32:
            line=line[:n]+line[n+2:];break
        if n==len(line)-2: noend=False
        n+=1

print(len(line))