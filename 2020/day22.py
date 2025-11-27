# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:47:06 2025

@author: castelf
"""

from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day22.txt','r') as f: lines=f.readlines()

lines=['Player 1:',
'9',
'2',
'6',
'3',
'1',
'',
'Player 2:',
'5',
'8',
'4',
'7',
'10']

for line in lines:
    if line.strip()=='Player 1:':p_1=deque([]);first=True
    elif line.strip()=='':first=False
    elif first:p_1.append(int(line.strip()))
    elif line.strip()=='Player 2:':p_2=deque([])
    elif not first :p_2.append(int(line.strip()))
    
    