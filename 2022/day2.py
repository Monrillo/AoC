# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:05:03 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day2.txt','r') as f: lines=f.readlines()

def fight_1(y,o): 
    you = ['X','Y','Z']
    opponent = ['A','B','C']
    
    py=you.index(y)
    po=opponent.index(o)
    
    if py==po+1 or py==po-2:
        return 6+py+1
    if py==po:
        return 3+py+1
    else:
        return py+1

def fight_2(y,o):
    opponent = ['A','B','C']
    po=opponent.index(o)
    
    if y=='X' and po>0:
        return po
    elif y=='X' and po==0:
        return 3
    elif y=='Y':
        return 3+po+1
    elif y=='Z' and po<2:
        return 6+po+2
    elif y=='Z' and po==2:
        return 7

score_1=0
score_2=0
for line in lines:
    op_hand,yo_hand=line.strip('\n').split(' ')
    score_1+=fight_1(yo_hand,op_hand)
    score_2+=fight_2(yo_hand,op_hand)

print("Part 1:",score_1)

print("Part 2:",score_2)

