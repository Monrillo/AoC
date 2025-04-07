# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:02:53 2025

@author: castelf
"""

data=[line.strip() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day2.txt','r')]
two_tot=0
three_tot=0
for d in data:
    two=0
    three=0
    for l in d:
        if d.count(l)==2:two=1
        if d.count(l)==3:three=1
    two_tot+=two
    three_tot+=three
print(two_tot*three_tot)

for i in data:
    for j in data:
        diffs = 0
        for idx, ch in enumerate(i):
            if ch != j[idx]:
                diffs += 1
        if diffs == 1:
            ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
            print("Part Two:", ''.join(ans))