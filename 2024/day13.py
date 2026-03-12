# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:28:11 2026

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day13.txt','r') as f: lines=f.readlines()

def play(ax,ay,bx,by,px,py):
    possib=[]
    for a in range(1,101):
        for b in range(1,101):
            if a*ax+b*bx>px or a*ay+b*by>py: break
            if a*ax+b*bx==px and a*ay+b*by==py: possib.append((a,b))
    return possib

# lines=['Button A: X+94, Y+34',
# 'Button B: X+22, Y+67',
# 'Prize: X=8400, Y=5400',
# '',
# 'Button A: X+26, Y+66',
# 'Button B: X+67, Y+21',
# 'Prize: X=12748, Y=12176',
# '',
# 'Button A: X+17, Y+86',
# 'Button B: X+84, Y+37',
# 'Prize: X=7870, Y=6450',
# '',
# 'Button A: X+69, Y+23',
# 'Button B: X+27, Y+71',
# 'Prize: X=18641, Y=10279']

cost=0
for line in lines:
    if line.startswith('Button A'):
        ax,ay=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
    elif line.startswith('Button B'):
        bx,by=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
    elif line.startswith('Prize'):
        px,py=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
        res=play(ax, ay, bx, by, px, py)
        if res:
            cost+=min(3*r[0]+r[1] for r in res)

print("Part 1:",cost)


