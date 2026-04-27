# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:03:57 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day8.txt','r') as f: lines=f.readlines()

# lines=['30373',
# '25512',
# '65332',
# '33549',
# '35390']

forest=[[int(x) for x in list(line.strip('\n'))] for line in lines]
size=len(lines)

def check_visible(l,c):
    return all(forest[i][c]<forest[l][c] for i in range(l))\
        or all(forest[i][c]<forest[l][c] for i in range(l+1,size))\
            or all(forest[l][i]<forest[l][c] for i in range(c))\
                or all(forest[l][i]<forest[l][c] for i in range(c+1,size))

# Trees in border
visible=4*(size-1)

# Trees in the center
visible+=sum(check_visible(l,c) for c in range(1,size-1) for l in range(1,size-1))

print("Part 1:",visible)

def check_scenic(l,c):
    xd=xu=yl=yr=0
    while l-xd>=0:
        xd+=1
        if (l-xd)==0 or forest[l-xd][c]>=forest[l][c]:break
    while l+xu<size:
        xu+=1
        if (l+xu)==size-1 or forest[l+xu][c]>=forest[l][c]:break
    while c-yl>=0:
        yl+=1
        if (c-yl)==0 or forest[l][c-yl]>=forest[l][c]:break
    while c+yr<size:
        yr+=1
        if (c+yr)==size-1 or forest[l][c+yr]>=forest[l][c]:break
    return xd*xu*yl*yr
    
    
    return all(forest[i][c]<forest[l][c] for i in range(l))\
        or all(forest[i][c]<forest[l][c] for i in range(l+1,size))\
            or all(forest[l][i]<forest[l][c] for i in range(c))\
                or all(forest[l][i]<forest[l][c] for i in range(c+1,size))


print("Part 2:",max(check_scenic(l,c) for c in range(1,size-1) for l in range(1,size-1)))
