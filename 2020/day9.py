# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:53:33 2025

@author: castelf
"""

import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day9.txt','r') as f: lines=f.readlines()

# lines=['35',
# '20',
# '15',
# '25',
# '47',
# '40',
# '62',
# '55',
# '65',
# '95',
# '102',
# '117',
# '150',
# '182',
# '127',
# '219',
# '299',
# '277',
# '309',
# '576']

data=[int(x.strip()) for x in lines]
preamble=25
i=0

while True:
    if not any(sum(el)==data[i+preamble] for el in it.combinations(data[i:i+preamble], 2)):
        res=data[i+preamble];break
    else:
        i+=1

print("Part 1:",res)

length=2
not_found=True
while not_found:
    for i in range(len(data)-length):
        if sum(data[i:i+length])==res:
            print("Part 2:",min(data[i:i+length])+max(data[i:i+length]))
            not_found=False
            break
    length+=1
