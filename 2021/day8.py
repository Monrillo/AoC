# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 15:42:24 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day8.txt','r') as f: lines=f.readlines()

def tri(dig):
    numbers={}
    nums=dig.split()
    for d in nums:
        if len(d)==2:numbers[d]=1
        elif len(d)==3:numbers[d]=7
        elif len(d)==4:numbers[d]=4
        elif len(d)==7:numbers[d]=8
    nums=[x for x in nums if x not in numbers.keys()]
    for d in nums:
        if len(d)==5 and all(x in d for x in list(numbers.keys())[list(numbers.values()).index(7)]):
            numbers[d]=3
        elif len(d)==6 and not all(x in d for x in list(numbers.keys())[list(numbers.values()).index(1)]):
            numbers[d]=6
    nums=[x for x in nums if x not in numbers.keys()]
    for d in nums:
        if len(d)==5 and all(x in list(numbers.keys())[list(numbers.values()).index(6)] for x in d):
            numbers[d]=5
        elif len(d)==5 and not all(x in list(numbers.keys())[list(numbers.values()).index(6)] for x in d):
            numbers[d]=2
        elif len(d)==6 and all(x in d for x in list(numbers.keys())[list(numbers.values()).index(3)]):
            numbers[d]=9
        elif len(d)==6 and not all(x in d for x in list(numbers.keys())[list(numbers.values()).index(3)]):
            numbers[d]=0
    
    return numbers
    
part1=0
part2=0

for line in lines:
    digits,output=line.strip('\n').split(' | ')
    table=tri(digits)
    result=[]
    for o in output.split():
        for x in table.keys():
            if len(x)==len(o) and all(d in o for d in x): result.append(table[x])
                
    part1+=sum(1 for x in result if x in [1,7,4,8])
    part2+=int(''.join(str(n) for n in result))
    
print("Part 1:",part1)

print("Part 2:",part2)
