# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:10:12 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day14.txt','r') as f: lines=f.readlines()

# lines=['O....#....',
# 'O.OO#....#',
# '.....##...',
# 'OO.#O....O',
# '.O.....O#.',
# 'O.#..O.#.#',
# '..O..#O..O',
# '.......O..',
# '#....###..',
# '#OO..#....']

platform=[list(line.strip('\n')) for line in lines]
num_l=len(platform)
num_c=len(platform[0])

# Find rocks
rocks=[]
for l in range(num_l):
    for c in range(num_c):
        if platform[l][c]=='O':rocks.append((l,c))
num_rocks=len(rocks)

# Tilting function
def tilt(direction):
    global rocks
    global platform
    
    if direction=="n":
        rocks.sort(key=lambda tup: tup[0])
        c_x=-1
        c_y=0
    elif direction=="s":
        rocks.sort(key=lambda tup: tup[0], reverse=True)
        c_x=1
        c_y=0
    elif direction=="w":
        rocks.sort(key=lambda tup: tup[1])
        c_x=0
        c_y=-1
    elif direction=="e":
        rocks.sort(key=lambda tup: tup[1], reverse=True)
        c_x=0
        c_y=1
    for _ in range(num_rocks):
        x,y=rocks.pop(0)
        platform[x][y]='.'
        delta=0
        while 0<=(x+c_x*delta)<num_l and 0<=(y+c_y*delta)<num_c:
            if platform[x+c_x*delta][y+c_y*delta]!='.':break
            else:delta+=1
        delta-=1
        rocks.append((x+c_x*delta,y+c_y*delta))
        platform[x+c_x*delta][y+c_y*delta]='O'

# Tilt North
tilt('n')

# Count points
points=sum(num_l-r[0] for r in rocks)

print("Part 1:",points)

# Finish cycle
tilt('w')
tilt('s')
tilt('e')

# List of rock positions after each cycle
load_positions=[set(rocks)]

while True:
    tilt('n')
    tilt('w')
    tilt('s')
    tilt('e')
    if any(set(rocks)==l for l in load_positions):break
    else:load_positions.append(set(rocks))
    
pos=len(load_positions)
long=len(load_positions)-load_positions.index(set(rocks))

pos_final=((1000000000-1-pos)%long)+load_positions.index(set(rocks))

points=sum(num_l-r[0] for r in load_positions[pos_final])

print("Part 2:",points)

