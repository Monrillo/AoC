# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:43:21 2026

@author: castelf
"""

import itertools as it
from tqdm import tqdm

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day19.txt','r') as f: lines=f.readlines()

lines=['r, wr, b, g, bwu, rb, gb, br',
'',
'brwrr',
'bggr',
'gbbr',
'rrbgbr',
'ubwu',
'bwurrg',
'brgr',
'bbrgwb']

all_towels=lines[0].strip('\n').split(', ')
pattern=[]
for line in lines[2:]:
    pattern.append(line.strip('\n'))
    
def is_possible(design):
    return design=='' or any(design.startswith(t) and is_possible(design[len(t):]) for t in towels)

res=0
for pat in tqdm(pattern):
    towels=[t for t in all_towels if t in pat]
    if is_possible(pat):res+=1

print("Part 1:",res)

def check_towel(pat):
    possib=[t for t in towels if t in pat]
    rep_max=len(pat)//min(len(p) for p in possib)
    rep_min=len(pat)//max(len(p) for p in possib)
    return any(''.join(i)==pat for r in range(rep_min,rep_max+1) for i in it.product(possib, repeat=r))

res=0
for p in tqdm(pattern):
    if check_towel(p): res+=1
print("Part 1:",res)


pat=pattern[-1]
possib=[t for t in towels if t in pat]
long=[p for p in possib if len(p)>1]

def design_possible(towels, design, index):
    if index == len(design):
        return True

    for towel in towels:
        if towel == design[index:index+len(towel)]:
            if design_possible(towels, design, index+len(towel)):
                return True

    return False


def design_possible_count(towels, design, cache):
    if design == "":
        return 1

    if (c := cache.get(design, None)) is not None:
        return c

    result = 0
    for towel in towels:
        if towel == design[:len(towel)]:
            result += design_possible_count(towels, design[len(towel):], cache)

    cache[design] = result
    return result


def part1(towels, designs):
    return sum(1 for d in designs if design_possible(towels, d, 0))


def part2(towels, designs):
    return sum(design_possible_count(towels, d, {}) for d in designs)

part1(all_towels,pattern)
