# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:39:55 2025

@author: castelf
"""

#first_row='.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'

def tile(l,c,r):
    if l==c=='^' and r=='.': return '^'
    elif c==r=='^' and l=='.': return '^'
    elif l=='^' and c==r=='.': return '^'
    elif r=='^' and l==c=='.': return '^'
    else: return '.'

lines=['.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.']
num_rows=400000

safe_tiles=lines[0].count('.')
while len(lines)<num_rows:
    row=lines[-1]
    new_row=''
    new_row+=tile('.',row[0],row[1])
    for i in range(1,len(row)-1): new_row+=tile(row[i-1],row[i],row[i+1])
    new_row+=tile(row[-2],row[-1],'.')
    safe_tiles+=new_row.count('.')
    lines.append(new_row)

print(safe_tiles)

