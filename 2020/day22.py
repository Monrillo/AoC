# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:47:06 2025

@author: castelf
"""

#from collections import deque
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day22.txt','r') as f: lines=f.readlines()

# lines=['Player 1:',
# '9',
# '2',
# '6',
# '3',
# '1',
# '',
# 'Player 2:',
# '5',
# '8',
# '4',
# '7',
# '10']

# lines=['Player 1:',
# '43',
# '19',
# '',
# 'Player 2:',
# '2',
# '29',
# '14']

# Creation of player's deck
for line in lines:
    if line.strip()=='Player 1:':p_1=[];first=True
    elif line.strip()=='':first=False
    elif first:p_1.append(int(line.strip()))
    elif line.strip()=='Player 2:':p_2=[]
    elif not first :p_2.append(int(line.strip()))

# Game Part 1
def game1(p1,p2):
    h1=p1.copy()
    h2=p2.copy()
    winner=0
    n=0
    while winner==0:
        n+=1
        c1=h1.pop(0)
        c2=h2.pop(0)

        if c1>c2:win1=True
        elif c2>c1:win1=False
            
        if win1:h1.append(c1);h1.append(c2)
        elif not win1:h2.append(c2);h2.append(c1)
        
        if len(h1)==0:winner=2
        elif len(h2)==0:winner=1
        
    if winner==2: hand=h2;winner1=False
    elif winner==1: hand=h1;winner1=True
    return winner1,hand,n

w,h,r=game1(p_1,p_2)

print("Part 1:", sum(np.flip(np.arange(1,len(h)+1))*h))

# Game Part 2
def game2(p1,p2):
    h1=p1.copy()
    h2=p2.copy()
    history=[]
    winner=0
    n=0
    while winner==0:
        n+=1
        if [h1,h2] in history: winner=1
        else:
            history.append([h1.copy(),h2.copy()])
            c1=h1.pop(0)
            c2=h2.pop(0)
            if c1<=len(h1) and c2<=len(h2):
                win1=game2(h1[:c1],h2[:c2])[0]
            else:
                if c1>c2:win1=True
                elif c2>c1:win1=False
                
            if win1:h1.append(c1);h1.append(c2)
            elif not win1:h2.append(c2);h2.append(c1)
            
            if len(h1)==0:winner=2
            elif len(h2)==0:winner=1
        
    if winner==2: hand=h2;winner1=False
    elif winner==1: hand=h1;winner1=True
    return winner1,hand,n

w,h,r=game2(p_1,p_2)

print("Part 2:", sum(np.flip(np.arange(1,len(h)+1))*h))
