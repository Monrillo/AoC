# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:28:35 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day9.txt','r') as f:
    line=f.read()

# line='A(2x2)BCD(2x2)EFG'
# line='A(1x5)BC'
# line='(6x1)(1x3)A'
# line='X(8x2)(3x3)ABCY'
# line='ADVENT'

# brac=re.search('\((\d+)x(\d+)\)',line)

# Me
def rec_len(l):
    brac=re.search('\((\d+)x(\d+)\)',l)
    if not brac:
        return l
    pos=brac.start()
    size=int(brac.group(1))
    rpt=int(brac.group(2))
    end=brac.end()
    return l[:pos] + rpt*l[end:end+size] + rec_len(l[end+size:])

# LieutenantSwr2d2
def rec_len_sol(l):
    brac=re.search('\((\d+)x(\d+)\)',l)
    if not brac:
        return len(l)
    pos=brac.start()
    size=int(brac.group(1))
    rpt=int(brac.group(2))
    end=brac.end()
    return len(l[:pos]) + rpt*size + rec_len_sol(l[end+size:])

def rec_len_sol_2(l):
    brac=re.search('\((\d+)x(\d+)\)',l)
    if not brac:
        return len(l)
    pos=brac.start()
    size=int(brac.group(1))
    rpt=int(brac.group(2))
    end=brac.end()
    return len(l[:pos]) + rpt*rec_len_sol_2(l[end:end+size]) + rec_len_sol_2(l[end+size:])

print(rec_len_sol(line))
print(rec_len_sol_2(line))


# line='(3x3)XYZ'
# line='X(8x2)(3x3)ABCY'
# line='(27x12)(20x12)(13x14)(7x10)(1x12)A'
# line='X(8x2)(3x3)ABCY'
# line='ADVENT'

