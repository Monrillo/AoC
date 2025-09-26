# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:49:09 2025

@author: castelf
"""
from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day8.txt','r') as f: lines=f.readlines()

# lines=['nop +0',
# 'acc +1',
# 'jmp +4',
# 'acc +3',
# 'jmp -3',
# 'acc -99',
# 'acc +1',
# 'jmp -4',
# 'acc +6']

instr=[l.strip().split() for l in lines]

def compute(ins):
    accumulator=0
    pos=0
    path=deque([])
    while pos<len(ins):
        if pos in path:break
        path.append(pos)
        if ins[pos][0]=='acc': accumulator+=int(ins[pos][1]);pos+=1
        elif ins[pos][0]=='jmp': pos+=int(ins[pos][1])
        else: pos+=1
    return pos,accumulator

print("Part 1:",compute(instr)[1])

change=[i for i in range(len(instr)) if instr[i][0]=='jmp' or instr[i][0]=='nop']

for c in change:
    new_instr=[l.strip().split() for l in lines]
    if new_instr[c][0]=='jmp': new_instr[c][0]='nop'
    elif new_instr[c][0]=='nop': new_instr[c][0]='jmp'
    p,res=compute(new_instr)
    if p>=len(new_instr):print("Part 2:",res);break

