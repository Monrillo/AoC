# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:41:56 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day16.txt','r') as f: lines=f.readlines()

# lines=['.|...\\....',
# '|.-.\\.....',
# '.....|-...',
# '........|.',
# '..........',
# '.........\\',
# '..../.\\\\..',
# '.-.-/..|..',
# '.|....-|.\\',
# '..//.|....']

contraption = {}

for l,line in enumerate(lines):
    for c,el in enumerate(list(line.strip('\n'))):
        contraption[l,c]=[el,set()]

dim=len(lines)

# headings=[ > , v , < , ^ ]
headings=[[0,1],[1,0],[0,-1],[-1,0]]

energized=[]

for n in range(4):
    for l in range(dim):
        for el in contraption: contraption[el][1]=set()
        if n==0: beams=[((l,0),0)] # position (l,c), 
        elif n==1: beams=[((0,l),1)] # position (l,c), direction
        elif n==2: beams=[((l,dim-1),2)] # position (l,c), direction
        elif n==3: beams=[((dim-1,l),3)] # position (l,c), direction
        while beams:    
            pos,head=beams.pop(0)
            if 0<=pos[0]<dim and 0<=pos[1]<dim and not head in contraption[pos][1]:
                contraption[pos][1].add(head)
                if contraption[pos][0]=='/':
                    if head==0 : head=3
                    elif head==1 : head=2
                    elif head==2 : head=1
                    elif head==3 : head=0
                    beams.append(((pos[0]+headings[head][0],pos[1]+headings[head][1]),head))
                elif contraption[pos][0]=='\\':
                    if head==0 : head=1
                    elif head==1 : head=0
                    elif head==2 : head=3
                    elif head==3 : head=2
                    beams.append(((pos[0]+headings[head][0],pos[1]+headings[head][1]),head))
                elif contraption[pos][0]=='|':
                    beams.append(((pos[0]+headings[1][0],pos[1]+headings[1][1]),1))
                    beams.append(((pos[0]+headings[3][0],pos[1]+headings[3][1]),3))
                elif contraption[pos][0]=='-':
                    beams.append(((pos[0]+headings[0][0],pos[1]+headings[0][1]),0))
                    beams.append(((pos[0]+headings[2][0],pos[1]+headings[2][1]),2))
                else:
                    beams.append(((pos[0]+headings[head][0],pos[1]+headings[head][1]),head))
        energized.append(sum(1 for el in contraption if len(contraption[el][1])>0))

print("Part 1:",energized[0])

print("Part 2:",max(energized))
           

