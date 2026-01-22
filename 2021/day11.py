# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:04:06 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day11.txt','r') as f: lines=f.readlines()

# lines=['5483143223',
# '2745854711',
# '5264556173',
# '6141336146',
# '6357385478',
# '4167524645',
# '2176841721',
# '6882881134',
# '4846848554',
# '5283751526']

matrix=np.array([[int(x) for x in list(line.strip('\n'))] for line in lines])

flash=0
step=0
while True:
    step+=1
    matrix+=1
    while len(np.where(matrix==10)[0])>0:
        new_matrix=matrix.copy()
        for p in range(len(np.where(matrix==10)[0])):
            flash+=1
            l=np.where(matrix==10)[0][p]
            c=np.where(matrix==10)[1][p]
            new_matrix[l][c]=0
            for i in range(-1,2):
                for j in range(-1,2):
                    if 0<=l+i<=9 and 0<=c+j<=9 and 0<new_matrix[l+i][c+j]<10:new_matrix[l+i][c+j]+=1
        matrix=new_matrix.copy()
    if step==100:flash_100=flash
    if len(np.where(matrix==0)[0])==100:break
        
print("Part 1:",flash_100)

print("Part 2:",step)
