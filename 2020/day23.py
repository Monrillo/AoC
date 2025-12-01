# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 14:29:25 2025

@author: castelf
"""
order='389125467'

cups=[int(x) for x in list(order)]
maxi=max(cups)
mini=min(cups)
pos=0

num=cups[pos]
pick=cups[pos+1:pos+4]
del cups[pos+1:pos+4]

while num>mini-1:
    num-=1
    if num in cups:break
    elif num==mini:num=maxi

cups[cups.index(num)+1:1]=pick
pos+=1

print(cups)
print("Pick up:",pick)
print("Destination:",num)
print("Position:",pos)