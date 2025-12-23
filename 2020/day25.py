# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 16:57:27 2025

@author: castelf
"""

card=11349501
door=5107328

# card=5764801
# door=17807724

def retrieve(n):
    num=1
    subject=7
    step=0
    while num!=n:
        num*=subject
        num%=20201227
        step+=1
    return step

def compute(sub,times):
    num=1
    for _ in range(times):
        num*=sub
        num%=20201227
    return num

card_loop=retrieve(card)
door_loop=retrieve(door)

print(compute(card,door_loop))

