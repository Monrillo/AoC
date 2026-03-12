# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:28:11 2026

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day13.txt','r') as f: lines=f.readlines()

# My part of code

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

########################################################################

# Solution taken from amnorm https://github.com/amundsno/advent-of-go-24/blob/48fd1b113ba9292a209d73b398948fc641585f36/day13/day13.py

def lde(a, b, c):
    # From https://new.math.uiuc.edu/public348/python/diophantus.html
    q, r = divmod(a, b)
    if r == 0:
        return ([0, c/b])
    else:
        sol = lde(b, r, c)
        u = sol[0]
        v = sol[1]
        return ([v, u-q*v])

from math import gcd, floor, ceil
def cost_to_price(ax, ay, bx, by, tx, ty):
    # Adapted from solution by amnorm
    
    det = ax*by - bx*ay
    if det != 0:
        # Case 1: Only one possible solution
        aDet = tx*by - ty*bx
        bDet = ty*ax - tx*ay
        
        if aDet % det == 0 and bDet % det == 0:
            # The solution is valid only A and B are integers
            A, B = aDet//det, bDet//det
            return 3*A + B
        
        return -1
    
    detAug = ax*ty - tx*ay
    if detAug == 0 and tx % gcd(ax, bx) != 0:
        # Case 2: Many possible solutions, but none are valid
        return -1
    
    # Case 3: Many possible solutions, but only one is optimal
    # Find one solution to the LDE: A(ax) + B(bx) = tx
    A0, B0 = lde(ax, bx, tx)
    
    # General solutions are of the form: A = A0 + k*bx, B = B0 - k*ax
    # Select the k that minimizes the cost inefficient button
    k = [ceil(-A0/bx), floor(B0/ax)]
    k = max(k[0], k[1]) if ax/bx > 3 else min(k[0], k[1])
    
    A = A0+k*bx
    B = B0-k*ax
    
    if A < 0 or B < 0:
        # Invalid solution, despite selecting optimal k
        return -1
    
    return 3*A + B

cost=0
cost_2=0
sup=10000000000000
for line in lines:
    if line.startswith('Button A'):
        ax,ay=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
    elif line.startswith('Button B'):
        bx,by=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
    elif line.startswith('Prize'):
        px,py=[int(x) for x in re.findall(r'(\d+)', line.strip('\n'))]
        res=cost_to_price(ax, ay, bx, by, px, py)
        if res>0:
            cost+=res
        res_2=cost_to_price(ax, ay, bx, by, sup+px, sup+py)
        if res_2>0:
            cost_2+=res_2

print("Part 1:",cost)

print("Part 2:",cost_2)
