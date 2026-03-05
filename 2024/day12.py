# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:47:55 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day12.txt','r') as f: lines=f.readlines()

lines=['RRRRIICCFF',
'RRRRIICCCF',
'VVRRRCCFFF',
'VVRCCCJFFF',
'VVVVCJJCFE',
'VVIVCCJJEE',
'VVIIICJJEE',
'MIIIIIJJEE',
'MIIISIJEEE',
'MMMISSJEEE']

field=[list(l.strip('\n')) for l in lines]
ligne=len(field)
colonne=len(field[0])



pos=set(((0,1),(0,2),(0,3)))
field[pos]
