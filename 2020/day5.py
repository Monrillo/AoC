# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:28:44 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day5.txt','r') as f: lines=f.readlines()

def seat(inp):
    inpb=inp.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    r=int(inpb[:7],2)
    c=int(inpb[-3:],2)
    return (r*8+c)

seat_ID=[seat(s.strip()) for s in lines]

print("Part 1:",max(seat_ID))

sorted(seat_ID)

for i in range(len(seat_ID)-1):
    if sorted(seat_ID)[i+1]!=sorted(seat_ID)[i]+1:print("Part 2:",sorted(seat_ID)[i]+1)
    