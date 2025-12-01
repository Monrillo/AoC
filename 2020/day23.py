# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 14:29:25 2025

@author: castelf
"""
order='389125467'

cups=[int(x) for x in list(order)]
length=len(cups)
maxi=max(cups)
mini=min(cups)
pos=0



for n in range(1,11):
    num=cups[pos]
    pos_num=cups[pos]
    
    if pos<length-4:
        pick=cups[pos+1:pos+4]
    else:
        pick=cups[pos+1:pos+4]+cups[0:(pos+4)%length]
    
    while num>mini:
        num-=1
        if num not in pick:break
        elif num<=mini:num=maxi+1
    
    print("-- move ",n," --")
    print(cups)
    print("Pick up:",pick)
    print("Destination:",num)
    
    if pos<length-4:
        del cups[pos+1:pos+4]
    else:
        del cups[pos+1:pos+4]
        del cups[0:(pos+4)%length]
    
    cups[cups.index(num)+1:1]=pick
    pos=cups.index(pos_num)
    pos=(pos+1)%length
    
    






