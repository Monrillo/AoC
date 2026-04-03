# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:10:12 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day14.txt','r') as f: lines=f.readlines()

lines=['O....#....',
'O.OO#....#',
'.....##...',
'OO.#O....O',
'.O.....O#.',
'O.#..O.#.#',
'..O..#O..O',
'.......O..',
'#....###..',
'#OO..#....']

platform=[list(line.strip('\n')) for line in lines]

rocks=[]
for l in range(len(platform)):
    for c in range(len(platform[0])):
        if platform[l][c]=='O':rocks.append((l,c))

while rocks:
    x,y=rocks.pop(0)
    platform[x][y]='.'
    dx=0
    while x-dx>=0:
        if platform[x-dx][y]!='.':break
        else:dx+=1
