# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 10:07:29 2025

@author: castelf
"""

import re
from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day8.txt','r') as f: lines=f.readlines()

# lines=['LLR',
# '',
# 'AAA = (BBB, BBB)',
# 'BBB = (AAA, ZZZ)',
# 'ZZZ = (ZZZ, ZZZ)']

# lines=['LR',
# '',
# '11A = (11B, XXX)',
# '11B = (XXX, 11Z)',
# '11Z = (11B, XXX)',
# '22A = (22B, XXX)',
# '22B = (22C, 22C)',
# '22C = (22Z, 22Z)',
# '22Z = (22B, 22B)',
# 'XXX = (XXX, XXX)']

pos=deque([])
left=deque([])
right=deque([])
all_pos=deque([])
all_end=deque([])
cmd=list(lines[0].strip())
for line in lines[2:]:
    p,l,r=re.findall('(\w+) = \((\w+), (\w+)\)', line)[0]
    if p[-1]=='A':all_pos.append(p)
    elif p[-1]=='Z':all_end.append(p)
    pos.append(p)
    left.append(l)
    right.append(r)

# Part 1
position='AAA'
step=0
cpt=0
while position!='ZZZ':
    if cmd[cpt]=='L':position=left[pos.index(position)]
    elif cmd[cpt]=='R':position=right[pos.index(position)]
    step+=1
    cpt+=1
    if cpt==len(cmd):cpt=0
print(step)

# Part 2
step=0
cpt=0
steps=[]
while len(all_end)>0:
    if cmd[cpt]=='L':all_pos=[left[pos.index(p)] for p in all_pos]
    elif cmd[cpt]=='R':all_pos=[right[pos.index(p)] for p in all_pos]
    step+=1
    cpt+=1
    if cpt==len(cmd):cpt=0
    if any(p in all_end for p in all_pos):
        steps.append(step)
        [all_end.remove(t) for t in all_pos if t in all_end]
#print(steps)

# Solution has been used for lcm trick

from math import gcd

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

print(lcm(steps))

