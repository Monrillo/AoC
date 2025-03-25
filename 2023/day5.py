# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 09:42:48 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day5.txt','r') as f: lines=f.readlines()

lines=['seeds: 79 14 55 13',
'',
'seed-to-soil map:',
'50 98 2',
'52 50 48',
'',
'soil-to-fertilizer map:',
'0 15 37',
'37 52 2',
'39 0 15',
'',
'fertilizer-to-water map:',
'49 53 8',
'0 11 42',
'42 0 7',
'57 7 4',
'',
'water-to-light map:',
'88 18 7',
'18 25 70',
'',
'light-to-temperature map:',
'45 77 23',
'81 45 19',
'68 64 13',
'',
'temperature-to-humidity map:',
'0 69 1',
'1 0 69',
'',
'humidity-to-location map:',
'60 56 37',
'56 93 4']




seeds=[int(x) for x in re.findall('(\d+)', lines[0])]
location=[]
#comp={'soil':0,'fertilizer':0,'water':0,'light':0,'temperature':0,'humidity':0,'location':0}
for seed in seeds:
    #comp['soil']=seed
    val=seed
    for line in lines[1:]:
        #l=line.strip()
        #if re.match('map:', l):curs=re.match('(\w+)', l)[2]
        if re.match('\d+', line):
            dest,start,leng=[int(x) for x in re.findall('(\d+)', line)]
            if start<val<start+leng:val=dest+(val-start)
    location.append(val)

print(min(location))
    
print(seeds)
lines[0]
re.findall('(\d+)', lines[3])
re.findall('(\w+)', lines[2])
if re.match('\d+', lines[3]):dest,start,leng=[int(x) for x in re.findall('(\d+)', lines[3])]
if re.match('', lines[1]):print('yes')




D = open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day5.txt').read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))