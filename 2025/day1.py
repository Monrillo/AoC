# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 09:28:13 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day1.txt','r') as f: lines=f.readlines()

# lines=['L68',
# 'L30',
# 'R48',
# 'L5',
# 'R60',
# 'L55',
# 'L1',
# 'L99',
# 'R14',
# 'L82']

res=0
res2=0
point=50
for line in lines:
    direction = line.strip()[0]
    distance = int(line.strip()[1:])
    if direction=='L':
        flip= (100 - point)%100 
        pas = (flip + distance)//100
        point = (point - distance)%100
    elif direction=='R':
        passes_2 = (point + distance)//100
        pas = (point + distance)//100
        point = (point + distance)%100
    res2+=abs(pas)
    if point==0: res+=1
    
print("Part 1:",res)

print("Part 2:",res2)

