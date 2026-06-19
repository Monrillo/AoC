# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:56:23 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day13.txt','r') as f: lines=f.readlines()

lines=['[1,1,3,1,1]',
'[1,1,5,1,1]',
'',
'[[1],[2,3,4]]',
'[[1],4]',
'',
'[9]',
'[[8,7,6]]',
'',
'[[4,4],4,4]',
'[[4,4],4,4,4]',
'',
'[7,7,7,7]',
'[7,7,7]',
'',
'[]',
'[3]',
'',
'[[[]]]',
'[[]]',
'',
'[1,[2,[3,[4,[5,6,7]]]],8,9]',
'[1,[2,[3,[4,[5,6,0]]]],8,9]']

line1=lines[3].strip('\n')
line2=lines[4].strip('\n')

# cur=1

# group1={}
# group2={}

# if line1[cur]=='[':group1+=1
# elif line1[cur]==']':group1-=1

# if line2[cur]=='[':group2+=1
# elif line2[cur]==']':group2-=1


# len(group1)

list_1=eval(line1)
list_2=eval(line2)

all(isinstance(l, list) for l in list_1)
for l in list_1: print(l)

len(list_2)

len(list_1[0])
len(list_2[0])
