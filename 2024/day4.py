# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 16:47:36 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day4.txt','r') as f: lines=f.readlines()

# lines=['MMMSXXMASM',
# 'MSAMXMSMSA',
# 'AMXSXMAAMM',
# 'MSAMASMSMX',
# 'XMASAMXAMM',
# 'XXAMMXXAMA',
# 'SMSMSASXSS',
# 'SAXAMASAAA',
# 'MAMMMXMMMM',
# 'MXMXAXMASX']

matrix=np.array([list(l.strip('\n')) for l in lines])

xmas=0
#test=[]
for i in range(len(np.where(matrix=='X')[0])):
    l=np.where(matrix=='X')[0][i]
    c=np.where(matrix=='X')[1][i]
    if c<matrix.shape[1]-3 and matrix[l][c+1]=='M' and matrix[l][c+2]=='A' and matrix[l][c+3]=='S':xmas+=1#;test.append((l,c,1))
    if l<matrix.shape[0]-3 and c<matrix.shape[1]-3 and matrix[l+1][c+1]=='M' and matrix[l+2][c+2]=='A' and matrix[l+3][c+3]=='S':xmas+=1#;test.append((l,c,2))
    if l<matrix.shape[0]-3 and matrix[l+1][c]=='M' and matrix[l+2][c]=='A' and matrix[l+3][c]=='S':xmas+=1#;test.append((l,c,3))
    if l<matrix.shape[0]-3 and c>=3 and matrix[l+1][c-1]=='M' and matrix[l+2][c-2]=='A' and matrix[l+3][c-3]=='S':xmas+=1#;test.append((l,c,4))
    if c>=3 and matrix[l][c-1]=='M' and matrix[l][c-2]=='A' and matrix[l][c-3]=='S':xmas+=1#;test.append((l,c,5))
    if l>=3 and c>=3 and matrix[l-1][c-1]=='M' and matrix[l-2][c-2]=='A' and matrix[l-3][c-3]=='S':xmas+=1#;test.append((l,c,6))
    if l>=3 and matrix[l-1][c]=='M' and matrix[l-2][c]=='A' and matrix[l-3][c]=='S':xmas+=1#;test.append((l,c,7))
    if l>=3 and c<matrix.shape[1]-3 and matrix[l-1][c+1]=='M' and matrix[l-2][c+2]=='A' and matrix[l-3][c+3]=='S':xmas+=1#;test.append((l,c,8))

print("Part 1:",xmas)
        
xmas2=0
for l in range(1,matrix.shape[0]-1):
    for c in range(1,matrix.shape[1]-1):
        if matrix[l][c]=='A':
            if matrix[l-1][c-1]=='M' and matrix[l+1][c-1]=='M' and matrix[l-1][c+1]=='S' and matrix[l+1][c+1]=='S':xmas2+=1
            if matrix[l-1][c-1]=='M' and matrix[l+1][c-1]=='S' and matrix[l-1][c+1]=='M' and matrix[l+1][c+1]=='S':xmas2+=1
            if matrix[l-1][c-1]=='S' and matrix[l+1][c-1]=='S' and matrix[l-1][c+1]=='M' and matrix[l+1][c+1]=='M':xmas2+=1
            if matrix[l-1][c-1]=='S' and matrix[l+1][c-1]=='M' and matrix[l-1][c+1]=='S' and matrix[l+1][c+1]=='M':xmas2+=1

print("Part 2:",xmas2)
