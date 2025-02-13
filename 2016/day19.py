# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:29:35 2025

@author: castelf
"""
import numpy as np

num_elves=5

elf={}
for i in range(1,num_elves+1): elf[i]=1

steal=True
while len(elf)>1:
    stolen=[]
    for k in elf.keys():
        if steal: vol=k; steal=False
        elif not steal: elf[vol]+=elf[k];steal=True;stolen.append(k)
    for k in stolen: del elf[k] 

print(list(elf.keys())[0])

elf={}
for i in range(1,num_elves+1): elf[i]=1

n=0
stolen=[]
while len(elf)>1:
    while n<list(elf.keys()):
        k=list(elf.keys())

np.where(np.array(list(elf.keys()))>n)


steal=True
while len(elf)>1:
    stolen=[]
    for k in elf.keys():
        if steal: vol=k; steal=False
        elif not steal: elf[vol]+=elf[k];steal=True;stolen.append(k)
    for k in stolen: del elf[k] 

print(list(elf.keys())[0])

# target = 3001330
# i = 1

# while i * 3 < target:
#     i *= 3

# print(target - i)


# import collections

# ELF_COUNT=3001330

# def solve_parttwo():
#     left = collections.deque()
#     right = collections.deque()
#     for i in range(1, ELF_COUNT+1):
#         if i < (ELF_COUNT // 2) + 1:
#             left.append(i)
#         else:
#             right.appendleft(i)

#     while left and right:
#         if len(left) > len(right):
#             left.pop()
#         else:
#             right.pop()

#         # rotate
#         right.appendleft(left.popleft())
#         left.append(right.pop())
#     return left[0] or right[0]