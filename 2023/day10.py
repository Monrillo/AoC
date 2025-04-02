# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:54:26 2025

@author: castelf
"""

import numpy as np

matrix=np.array([list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day10.txt','r')])

# matrix=np.array([['.','.','F','7','.'],
# ['.','F','J','|','.'],
# ['S','J','.','L','7'],
# ['|','F','-','-','J'],
# ['L','J','.','.','.']])

lines=['.F----7F7F7F7F-7....',
'.|F--7||||||||FJ....',
'.||.FJ||||||||L7....',
'FJL7L7LJLJ||LJ.L-7..',
'L--J.L7...LJS7F-7L7.',
'....F-J..F7FJ|L7L7L7',
'....L7.F7||L7|.L7L7|',
'.....|FJLJ|FJ|F7|.LJ',
'....FJL-7.||.||||...',
'....L---J.LJ.LJLJ...']
matrix=np.array([list(line.strip()) for line in lines])

r_s=np.where(matrix=='S')[0][0]
c_s=np.where(matrix=='S')[1][0]

def first_dir(r,c):
    if r>0 and matrix[r-1,c] in ['7','|','F']: return 'N'
    elif c<(len(matrix)-1) and matrix[r,c+1] in ['7','-','J']: return 'E'
    elif r<(len(matrix)-1) and matrix[r+1,c] in ['L','|','J']: return 'S'
    elif c>0 and matrix[r,c-1] in ['L','-','F']: return 'W'

def move(r,c,d):
    if d=='N':r-=1
    elif d=='S':r+=1
    elif d=='E':c+=1
    elif d=='W':c-=1
    
    if d in ['N','S'] and matrix[r,c] in ['L','F']: d='E'
    elif d in ['N','S'] and matrix[r,c] in ['J','7']: d='W'
    elif d in ['E','W'] and matrix[r,c] in ['J','L']: d='N'
    elif d in ['E','W'] and matrix[r,c] in ['F','7']: d='S'
    
    return r,c,d

r,c,d=r_s,c_s,first_dir(r_s,c_s)
r,c,d=move(r,c,d)
step=1

while r!=r_s or c!=c_s:
    r,c,d=move(r,c,d)
    step+=1

print(step//2)
