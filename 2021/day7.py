# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 16:15:07 2026

@author: castelf
"""


with open("C:\\Users\castelf\Documents\GitHub\AoC\\2021\day7.txt") as f:
        positions = list(map(int, f.read().split(',')))

positions = [16,1,2,0,4,2,7,1,2,14]

sum(positions)/len(positions)
