# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:45:38 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day17.txt','r') as f: lines=f.readlines()

# lines=['2413432311323',
# '3215453535623',
# '3255245654254',
# '3446585845452',
# '4546657867536',
# '1438598798454',
# '4457876987766',
# '3637877979653',
# '4654967986887',
# '4564679986453',
# '1224686865563',
# '2546548887735',
# '4322674655533']

land = {}
for l,line in enumerate(lines):
    for c,el in enumerate(list(line.strip('\n'))):
        land[l,c]=[int(el),None]
        
num_l=len(lines)
num_c=len(lines[0].strip('\n'))

# headings=[ > , v , < , ^ ]
headings=[[0,1],[1,0],[0,-1],[-1,0]]

trackers=[((0,0),0,0,2)] # position (l,c), head, repetition in same direction, score

while trackers:    
    pos,head,rep,score=trackers.pop(0)
    if 0<=pos[0]<num_l and 0<=pos[1]<num_c:
        if land[pos][1] is None or score<land[pos][1]:
            land[pos][1]=score
            score+=land[pos][0]
            # New positions
            if rep<=3:trackers.append(((pos[0]+headings[head][0],pos[1]+headings[head][1]),head,rep+1,score))
            trackers.append(((pos[0]+headings[(head-1)%4][0],pos[1]+headings[(head-1)%4][1]),(head-1)%4,0,score))
            trackers.append(((pos[0]+headings[(head+1)%4][0],pos[1]+headings[(head+1)%4][1]),(head+1)%4,0,score))


print("Part 1:",sum(land[(num_l-1,num_c-1)]))

