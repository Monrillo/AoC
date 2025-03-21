# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 15:07:34 2025

@author: castelf
"""

import re
import numpy as np

lines=np.array([line.strip() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day3.txt','r').readlines()])

# lines=['467..114..',
# '...*......',
# '..35..633.',
# '......#...',
# '617*......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '...$.*....',
# '.664.598..']

def check_num(num,l,c):
    if num[1]==l and (c==num[2]-1 or c==num[3]): return True
    if (num[1]==l+1 or num[1]==l-1) and (c>=num[2]-1 and c<=num[3]): return True

numbers=[]
for i,line in enumerate(lines):
    for num in re.finditer(r'(\d+)', line):
        numbers.append([int(num.group()),i,num.start(),num.end()])
numbers=np.array(numbers)

result1=0
result2=0
for i,line in enumerate(lines):
    for sign in re.finditer(r'[^\.|\d]', line):
        for num_pos in numbers[np.where((numbers[:,1]>=i-1) & (numbers[:,1]<=i+1))]:
            if check_num(num_pos,i,sign.start()): result1+=num_pos[0]
            
    for sign in re.finditer('\*', line):
        num_list=[]
        for num_pos in numbers[np.where((numbers[:,1]>=i-1) & (numbers[:,1]<=i+1))]:
            if check_num(num_pos,i,sign.start()): num_list.append(num_pos[0])
        if len(num_list)==2: result2+=num_list[0]*num_list[1]
print(result1)
print(result2)

