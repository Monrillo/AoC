# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:49:33 2026

@author: castelf
"""
import re
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day14.txt','r') as f: lines=f.readlines()

lines=['p=0,4 v=3,-3',
'p=6,3 v=-1,-3',
'p=10,3 v=-1,2',
'p=2,0 v=2,-1',
'p=0,0 v=1,3',
'p=3,0 v=-2,-2',
'p=7,6 v=-1,-3',
'p=3,0 v=-1,-2',
'p=9,3 v=2,3',
'p=7,3 v=-1,2',
'p=2,4 v=2,-3',
'p=9,5 v=-3,-3']