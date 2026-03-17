# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:53:41 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day15.txt','r') as f: lines=f.readlines()

# lines=['########',
# '#..O.O.#',
# '##@.O..#',
# '#...O..#',
# '#.#.O..#',
# '#...O..#',
# '#......#',
# '########',
# '',
# '<^^>>>vv<v>>v<<']

# lines=['##########',
# '#..O..O.O#',
# '#......O.#',
# '#.OO..O.O#',
# '#..O@..O.#',
# '#O#..O...#',
# '#O..O..O.#',
# '#.OO.O.OO#',
# '#....O...#',
# '##########',
# '',
# '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^',
# 'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v',
# '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<',
# '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^',
# '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><',
# '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^',
# '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^',
# '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>',
# '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>',
# 'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^']

for i,l in enumerate(lines):
    if l.strip('\n')=='':
        sep=i

warehouse=[list(l.strip('\n')) for l in lines[:sep]]
num_l=len(warehouse)
num_c=len(warehouse[0])
for l in range(num_l):
    for c in range(num_c):
        if warehouse[l][c]=='@':
            pos=[l,c]
            warehouse[l][c]='.'
movement=list(''.join([l.strip('\n') for l in lines[sep:]]))

def step(p,mat,move):
    if move=='<': direc=[0,-1]
    elif move=='^': direc=[-1,0]
    elif move=='>': direc=[0,1]
    elif move=='v': direc=[1,0]
    new_pos=[p[0]+direc[0],p[1]+direc[1]]
    
    if mat[new_pos[0]][new_pos[1]]=='.':
        return new_pos,mat
    elif mat[new_pos[0]][new_pos[1]]=='#':
        return p,mat
    elif mat[new_pos[0]][new_pos[1]]=='O':
        liste=[]
        while mat[new_pos[0]][new_pos[1]]=='O':
            liste.append(new_pos)
            new_pos=[new_pos[0]+direc[0],new_pos[1]+direc[1]]
        if mat[new_pos[0]][new_pos[1]]=='#':
            return p,mat
        elif mat[new_pos[0]][new_pos[1]]=='.':
            for l in list(liste):
                mat[l[0]+direc[0]][l[1]+direc[1]]='O'
            new_pos=[p[0]+direc[0],p[1]+direc[1]]
            mat[new_pos[0]][new_pos[1]]='.'
            return new_pos,mat

for m in movement:
    pos,warehouse=step(pos, warehouse, m)

gps=0
for l in range(num_l):
    for c in range(num_c):
        if warehouse[l][c]=='O':
            gps+=l*100+c

print("Part 1:",gps)

# lines=['#######',
# '#...#.#',
# '#.....#',
# '#..OO@#',
# '#..O..#',
# '#.....#',
# '#######',
# '',
# '<vv<<^^<<^^']

for i,l in enumerate(lines):
    if l.strip('\n')=='':
        sep=i

warehouse=[]
for l in lines[:sep]:
    line=[]
    for el in list(l.strip('\n')):
        if el=='#' or el=='.': line.append(el);line.append(el)
        elif el=='@': line.append(el);line.append('.')
        elif el=='O': line.append('[');line.append(']')
    warehouse.append(line)
movement=list(''.join([l.strip('\n') for l in lines[sep:]]))

num_l=len(warehouse)
num_c=len(warehouse[0])
for l in range(num_l):
    for c in range(num_c):
        if warehouse[l][c]=='@':
            pos=[l,c]
            warehouse[l][c]='.'

def tracker(po,di,mat):
    if mat[po[0]+di[0]][po[1]+di[1]]=='.': return True
    elif mat[po[0]+di[0]][po[1]+di[1]]=='#': return False
    elif mat[po[0]+di[0]][po[1]+di[1]]=='[': return tracker([po[0]+di[0],po[1]+di[1]],di,mat) and tracker([po[0]+di[0],po[1]+1+di[1]],di,mat)
    elif mat[po[0]+di[0]][po[1]+di[1]]==']': return tracker([po[0]+di[0],po[1]+di[1]],di,mat) and tracker([po[0]+di[0],po[1]-1+di[1]],di,mat)

# di=direc
# po=new_pos
# mat=warehouse

def browser(po,di,mat):
    if mat[po[0]][po[1]]=='[':
        bag=[(mat[po[0]][po[1]],[po[0],po[1]]),(mat[po[0]][po[1]+1],[po[0],po[1]+1])]
        possib=[[po[0]+di[0],po[1]+di[1]],[po[0]+di[0],po[1]+1+di[1]]]
    elif mat[po[0]][po[1]]==']':
        bag=[(mat[po[0]][po[1]],[po[0],po[1]]),(mat[po[0]][po[1]-1],[po[0],po[1]-1])]
        possib=[[po[0]+di[0],po[1]+di[1]],[po[0]+di[0],po[1]-1+di[1]]]
    while possib:
        possi=possib.pop(0)
        if mat[possi[0]][possi[1]]=='[':
            bag.append([mat[possi[0]][possi[1]],[possi[0],possi[1]]])
            bag.append([mat[possi[0]][possi[1]+1],[possi[0],possi[1]+1]])
            possib.append([possi[0]+di[0],possi[1]+di[1]])
            possib.append([possi[0]+di[0],possi[1]+1+di[1]])
        elif mat[possi[0]][possi[1]]==']':
            bag.append([mat[possi[0]][possi[1]],[possi[0],possi[1]]])
            bag.append([mat[possi[0]][possi[1]-1],[possi[0],possi[1]-1]])
            possib.append([possi[0]+di[0],possi[1]+di[1]])
            possib.append([possi[0]+di[0],possi[1]-1+di[1]])
    return bag

def step_2(p,mat,move):
    if move=='<': direc=[0,-1];h=True
    elif move=='^': direc=[-1,0];h=False
    elif move=='>': direc=[0,1];h=True
    elif move=='v': direc=[1,0];h=False
    new_pos=[p[0]+direc[0],p[1]+direc[1]]
    
    if mat[new_pos[0]][new_pos[1]]=='.':
        return new_pos,mat
    elif mat[new_pos[0]][new_pos[1]]=='#':
        return p,mat
    else:
        if h:
            liste=[]
            while mat[new_pos[0]][new_pos[1]]=='[' or mat[new_pos[0]][new_pos[1]]==']':
                elem=mat[new_pos[0]][new_pos[1]]
                liste.append((elem,new_pos))
                new_pos=[new_pos[0]+direc[0],new_pos[1]+direc[1]]
            if mat[new_pos[0]][new_pos[1]]=='#':
                return p,mat
            elif mat[new_pos[0]][new_pos[1]]=='.':
                for l in list(liste):
                    mat[l[1][0]+direc[0]][l[1][1]+direc[1]]=l[0]
                new_pos=[p[0]+direc[0],p[1]+direc[1]]
                mat[new_pos[0]][new_pos[1]]='.'
                return new_pos,mat
        elif not h:
            if tracker(p, direc, mat):
                liste=browser(new_pos, direc, mat)
                for l in list(liste):
                    mat[l[1][0]][l[1][1]]='.'
                for l in list(liste):
                    mat[l[1][0]+direc[0]][l[1][1]+direc[1]]=l[0]
                new_pos=[p[0]+direc[0],p[1]+direc[1]]
                #mat[new_pos[0]][new_pos[1]]='.'
                return new_pos,mat
            else:
                return p,mat

# move=movement[5]
# p=pos
# mat=warehouse
# l=liste[0]

# for i in range(5):
#     pos,warehouse=step_2(pos, warehouse, movement[i])

# m=movement[7]

for m in movement:
    pos,warehouse=step_2(pos, warehouse, m)
    
gps=0
for l in range(num_l):
    for c in range(num_c):
        if warehouse[l][c]=='[':
            gps+=l*100+c

print("Part 2:",gps)
