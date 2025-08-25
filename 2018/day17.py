# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 16:59:28 2025

@author: castelf
"""

#with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day17.txt','r') as f: lines=f.readlines()

lines=['x=495, y=2..7',
'y=7, x=495..501',
'x=501, y=3..7',
'x=498, y=2..4',
'x=506, y=1..2',
'x=498, y=10..13',
'x=504, y=10..13',
'y=13, x=498..504']

for line in lines: print(line.strip().split(', '))
