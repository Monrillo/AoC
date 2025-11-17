# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 15:58:59 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day19.txt','r') as f: lines=f.readlines()

lines=['0: 4 1 5',
'1: 2 3 | 3 2',
'2: 4 4 | 5 5',
'3: 4 5 | 5 4',
'4: "a"',
'5: "b"']

instr=[l.strip().replace('"','').split(': ') for l in lines]
rec={}
for i in instr:
    rec[i[0]]=i[1].split(' | ')

rec['3']
