# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 14:55:30 2025

@author: castelf
"""

import numpy as np

#positions=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day6.txt',dtype=int,delimiter=',')

positions=np.array([[1, 1],
[1, 6],
[8, 3],
[3, 4],
[5, 5],
[8, 9]])

possible=np.where(np.logical_and((np.logical_and(positions[:,0]>np.min(positions[:,0]),positions[:,0]<np.max(positions[:,0]))),\
                (np.logical_and(positions[:,1]>np.min(positions[:,1]),positions[:,1]<np.max(positions[:,1])))))[0]

matrix=np.full((np.max(positions),np.max(positions)),-1,dtype=int)
