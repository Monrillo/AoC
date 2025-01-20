# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:51:17 2025

@author: castelf
"""
import numpy as np

cols = np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day3.txt',dtype='int')
good=0

for col in cols:
    if np.partition(col,1)[0] + np.partition(col,1)[1]>np.partition(col,1)[2]:
        good+=1
print(good)

good=0
for col in np.split(cols[:,0],len(cols[:,0])//3):
    if np.partition(col,1)[0] + np.partition(col,1)[1]>np.partition(col,1)[2]:
        good+=1
for col in np.split(cols[:,1],len(cols[:,1])//3):
    if np.partition(col,1)[0] + np.partition(col,1)[1]>np.partition(col,1)[2]:
        good+=1
for col in np.split(cols[:,2],len(cols[:,2])//3):
    if np.partition(col,1)[0] + np.partition(col,1)[1]>np.partition(col,1)[2]:
        good+=1
print(good)

