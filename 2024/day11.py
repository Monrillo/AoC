# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:36:27 2026

@author: castelf
"""


with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day11.txt','r') as f: arrange=[int(x) for x in f.read().split(' ')]

stones={}
for a in arrange:
    if a in stones.keys(): stones[a]+=1
    else: stones[a]=1

def update_stone(n):
    if n==0:
        return [1]
    elif len(str(n))%2==0:
        s=str(n)
        return [int(s[:len(s)//2]),int(s[len(s)//2:])]
    else :
        return [n*2024]
    
def blink(stones):
    new_stones={}
    for stone in stones:
        res=update_stone(stone)
        for r in res:
            if r in new_stones.keys(): new_stones[r]+=stones[stone]
            else: new_stones[r]=stones[stone]
    return new_stones
        

#stones=deque([125,17])
#print(stones)
for _ in range(25):
    stones=blink(stones)
    
print("Part 1:",sum(stones.values()))

for _ in range(50):
    stones=blink(stones)
    
print("Part 2:",sum(stones.values()))

