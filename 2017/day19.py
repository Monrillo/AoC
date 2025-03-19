# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 10:26:57 2025

@author: castelf
"""

# import numpy as np

# test=np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day19.txt',dtype=str)

import re

mat=[list(line[:-1]) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day19.txt','r').readlines()]
mat[-1].extend(' ')


# lines=['     |          \n',
# '     |  +--+    \n',
# '     A  |  C    \n',
# ' F---|----E|--+ \n',
# '     |  |  |  D \n',
# '     +B-+  +--+ ']
# mat=[list(line[:-1]) for line in lines]
# mat[-1].extend(' ')


word=[]
r=0
c=mat[r].index('|')
d='S'
step=1
while True:
    if d=='N': r-=1
    elif d=='S': r+=1
    elif d=='E': c+=1
    elif d=='W': c-=1
    step+=1
    if mat[r][c]==' ': break
    elif re.match(r'\w',mat[r][c]): word.append(mat[r][c])
    elif mat[r][c]=='+':
        if d=='S' or d=='N':
            if mat[r][c-1]!=' ':d='W'
            else: d='E'
        else:
            if mat[r-1][c]!=' ':d='N'
            else: d='S'

print(''.join(word))
print(step-1)