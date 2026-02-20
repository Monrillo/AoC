# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:39:18 2026

@author: castelf
"""
#import numpy as np
#matrix=np.array([list(l.strip('\n')) for l in lines])

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day8.txt','r') as f: lines=f.readlines()

# lines=['............',
# '........0...',
# '.....0......',
# '.......0....',
# '....0.......',
# '......A.....',
# '............',
# '............',
# '........A...',
# '.........A..',
# '............',
# '............']

matrix=[list(l.strip('\n')) for l in lines]
ligne=len(matrix)
colonne=len(matrix[0])

antennas={}
for l in range(ligne):
    for c in range(colonne):
        if matrix[l][c]!='.':
            ant=matrix[l][c]
            if ant in antennas.keys():antennas[ant].append((l,c))
            else: antennas[ant]=[(l,c)]

def interfere(p1,p2):
    x=abs(p1[0]-p2[0])
    y=abs(p1[1]-p2[1])
    a1=(-x if p1[0]==min(p1[0],p2[0]) else x,-y if p1[1]==min(p1[1],p2[1]) else y)
    a2=(-x if p2[0]==min(p1[0],p2[0]) else x,-y if p2[1]==min(p1[1],p2[1]) else y)
    return a1,a2

antinodes_1=set()
antinodes_2=set()
for a in antennas:
    for i in range(len(antennas[a])-1):
        for j in range(i+1,len(antennas[a])):
            a1=antennas[a][i]
            a2=antennas[a][j]
            if 0<=a1[0]<ligne and 0<=a1[1]<colonne:antinodes_2.add(a1)
            if 0<=a2[0]<ligne and 0<=a2[1]<colonne:antinodes_2.add(a2)
            g1,g2=interfere(a1,a2)
            a1=(a1[0]+g1[0],a1[1]+g1[1])
            a2=(a2[0]+g2[0],a2[1]+g2[1])
            if 0<=a1[0]<ligne and 0<=a1[1]<colonne:antinodes_1.add(a1);antinodes_2.add(a1)
            while 0<=a1[0]<ligne and 0<=a1[1]<colonne:
                a1=(a1[0]+g1[0],a1[1]+g1[1])
                if 0<=a1[0]<ligne and 0<=a1[1]<colonne:antinodes_2.add(a1)
            if 0<=a2[0]<ligne and 0<=a2[1]<colonne:antinodes_1.add(a2);antinodes_2.add(a2)
            while 0<=a2[0]<ligne and 0<=a2[1]<colonne:
                a2=(a2[0]+g2[0],a2[1]+g2[1])
                if 0<=a2[0]<ligne and 0<=a2[1]<colonne:antinodes_2.add(a2)

print("Part 1:",len(antinodes_1))

print("Part 2:",len(antinodes_2))

