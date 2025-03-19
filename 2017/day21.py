# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 10:25:35 2025

@author: castelf
"""

import numpy as np

#inst=[line.strip().split(' => ') for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day21.txt','r').readlines()]

matrix=np.array([['.','#','.'],['.','.','#'],['#','#','#']])

lines=['../.# => ##./#../...\n',
'.#./..#/### => #..#/..../..../#..#']
inst=[line.strip().split(' => ') for line in lines]





np.fliplr(matrix)
np.flipud(matrix)
np.rot90(matrix)

