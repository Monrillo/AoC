# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:52:29 2025

@author: castelf
"""
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day2.txt','r') as f:
    lines=f.readlines()

# lines=['ULL\n',
# 'RRDDD\n',
# 'LURDL\n',
# 'UUUUD']

keypad=np.array([[1,2,3],[4,5,6],[7,8,9]])
l=1
c=1

code=[]
for line in lines:
    for i in range(len(line)):
        if line[i]=='U' and l>0:
            l-=1
        elif line[i]=='D' and l<2:
            l+=1
        elif line[i]=='L' and c>0:
            c-=1
        elif line[i]=='R' and c<2:
            c+=1
    code.append(keypad[l,c])

print(code)

new_keypad=np.array([[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]])
l=2
c=0

new_code=[]
for line in lines:
    for i in range(len(line)):
        if line[i]=='U' and l>0 and new_keypad[c,l-1]!='0':
            l-=1
        elif line[i]=='D' and l<4 and new_keypad[c,l+1]!='0':
            l+=1
        elif line[i]=='L' and c>0 and new_keypad[c-1,l]!='0':
            c-=1
        elif line[i]=='R' and c<4 and new_keypad[c+1,l]!='0':
            c+=1
    new_code.append(new_keypad[l,c])

print(new_code)