# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 13:55:11 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day7.txt','r') as f: lines=f.readlines()

# def splitter(b,l):
#     if l==len(lines): return 1
#     elif lines[l].strip()[b]=='^': return splitter(b-1,l+1)+splitter(b+1,l+1)
#     else: return splitter(b,l+1)

# lines=['.......S.......',
# '...............',
# '.......^.......',
# '...............',
# '......^.^......',
# '...............',
# '.....^.^.^.....',
# '...............',
# '....^.^...^....',
# '...............',
# '...^.^...^.^...',
# '...............',
# '..^...^.....^..',
# '...............',
# '.^.^.^.^.^...^.',
# '...............']


num_split=0
beam=[0]*len(lines[0].strip())
beam[lines[0].strip().index('S')]+=1
for l in lines[1:]:
    for i in range(len(beam)):
        if l.strip()[i]=='^' and beam[i]>0:
            num_split+=1
            beam[i-1]+=beam[i]
            beam[i+1]+=beam[i]
            beam[i]=0
print("Part 1:",num_split)
print("Part 2:",sum(beam))

