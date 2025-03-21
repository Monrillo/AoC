# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 15:07:34 2025

@author: castelf
"""

import re

#matrix=np.array([list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day3.txt','r').readlines()])

lines=['467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']

for line in lines:
    print(re.findall(r'\d+', line))
