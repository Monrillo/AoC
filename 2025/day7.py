# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 13:55:11 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day7.txt','r') as f: lines=f.readlines()


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

beams=[lines[0].strip().index('S')]
num_split=0
double=0

for l in lines[1:]:
    split=[b for b in beams if l.strip()[b]=='^']
    num_split+=len(split)
    for s in split:
        beams.remove(s)
        if s+1 in beams:double+=1
        else: beams.append(s+1)
        if s-1 in beams:double+=1
        else: beams.append(s-1)

print("Part 1:",num_split)

def splitter(b,l):
    if l==len(lines): return 1
    elif lines[l].strip()[b]=='^': return splitter(b-1,l+1)+splitter(b+1,l+1)
    else: return splitter(b,l+1)

print("Part 2:",splitter(lines[0].strip().index('S'),0))
