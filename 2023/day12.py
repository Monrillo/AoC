# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:02:27 2025

@author: castelf
"""

import re
from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day12.txt','r') as f: file=f.readlines()

lines=[]
res=[]
for line in file:
    l,n=line.strip().split()
    res.append(tuple([int(x) for x in n.split(',')]))
    lines.append(l)

def comptage(line):
    return tuple([len(g) for g in re.findall('#+', line)])

def possib(line):
    pool=deque([line])
    while '?' in pool[0]:
        p=pool.popleft()
        pool.append(p[:re.search('\?', p).start()]+'.'+p[re.search('\?', p).start()+1:])
        pool.append(p[:re.search('\?', p).start()]+'#'+p[re.search('\?', p).start()+1:])
    return pool

result=sum(sum([1 for l in possib(l) if comptage(l)==res[i]]) for i,l in enumerate(lines))
print(result)

lines=[]
res=[]
for line in file:
    l,n=line.strip().split()
    n=(n+',')*5
    l=(l+'?')*5
    res.append(tuple([int(x) for x in n[:-1].split(',')]))
    lines.append(l[:-1])

result=sum(sum([1 for l in possib(l) if comptage(l)==res[i]]) for i,l in enumerate(lines))
print(result)


D = open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day12.txt','r').read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

# i == current position within dots
# bi == current position within blocks
# current == length of current block of '#'
# state space is len(dots) * len(blocks) * len(dots)
DP = {}
def f(dots, blocks, i, bi, current):
  key = (i, bi, current)
  if key in DP:
    return DP[key]
  if i==len(dots):
    if bi==len(blocks) and current==0:
      return 1
    elif bi==len(blocks)-1 and blocks[bi]==current:
      return 1
    else:
      return 0
  ans = 0
  for c in ['.', '#']:
    if dots[i]==c or dots[i]=='?':
      if c=='.' and current==0:
        ans += f(dots, blocks, i+1, bi, 0)
      elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
        ans += f(dots, blocks, i+1, bi+1, 0)
      elif c=='#':
        ans += f(dots, blocks, i+1, bi, current+1)
  DP[key] = ans
  return ans

for part2 in [False,True]:
  ans = 0
  for line in L:
    dots,blocks = line.split()
    if part2:
      dots = '?'.join([dots, dots, dots, dots, dots])
      blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
    blocks = [int(x) for x in blocks.split(',')]
    DP.clear()
    score = f(dots, blocks, 0, 0, 0)
    #print(dots, blocks, score, len(DP))
    ans += score
  print(ans)