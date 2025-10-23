# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 11:16:21 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day13.txt','r') as f: lines=f.readlines()

# lines=['939',
# '7,13,x,x,59,x,31,19']

start=int(lines[0].strip())
bus=[int(x) for x in lines[1].strip().split(',') if x!='x']
gap=[(start//b+1)*b for b in bus]
res=bus[gap.index(min(gap))]*(min(gap)-start)

print("Part 1:",res)

import sys

a, b = open("C:\\Users\castelf\Documents\GitHub\AoC\\2020\day13.txt").read().strip().split("\n")
timestamp = int(a)
busses = [(i, int(x)) for i, x in enumerate(b.split(",")) if x != "x"]

# Part 1.
min_wait = sys.maxsize
part1 = None

# Part 2.
d = 1
i = 0

for offset, bus in busses:
    # Part 1. 
    loops = -(timestamp // -bus)
    wait = loops * bus - timestamp
    if wait < min_wait:
        part1 = wait * bus
        min_wait = wait

    # Part 2.
    while True:
        i += d
        if (i + offset) % bus == 0:
            d = d * bus
            break

print (part1)
print (i)




