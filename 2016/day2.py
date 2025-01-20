# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:52:29 2025

@author: castelf
"""
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day2.txt','r') as f:
    lines=f.readlines()

keypad=np.array([[1,2,3],[4,5,6],[7,8,9]])
pos=(1,1)

keypad[pos]

for line in lines:
    print(line.strip())