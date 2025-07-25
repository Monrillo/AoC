# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 16:15:18 2025

@author: castelf
"""

#with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day13.txt','r') as f: lines=f.readlines()

import numpy as np

lines=[
"/->-\        ",
"|   |  /----\\",
"| /-+--+-\  |",
"| | |  | v  |",
"\-+-/  \-+--/",
"  \------/   "]

mat=[list(l) for l in lines]
#matrix=np.array([l[:150] for l in mat])
matrix=np.array(mat)

matrix.shape

np.where(matrix=='>')

