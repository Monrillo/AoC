# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 13:52:03 2025

@author: castelf
"""

lines=['0: 3',
'1: 2',
'4: 4',
'6: 4']
lines = [line.split(': ') for line in lines]
#lines = [line.split(': ') for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day13.txt','r').readlines()]
heights = {int(pos): int(height) for pos, height in lines}
print(sum(pos * heights[pos] for pos in heights if pos % ((heights[pos] - 1) * 2) == 0))
for wait in range(20):
    print(sum(pos * heights[pos] for pos in heights if (pos+wait) % ((heights[pos] - 1) * 2) == 0))





wait=0
while True:
    if sum(pos * heights[pos] for pos in heights if (pos+wait) % ((heights[pos] - 1) * 2) == 0)==0: break
    wait+=1
print(wait)






def scanner(height, time):
    offset = time % ((height - 1) * 2)
    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))