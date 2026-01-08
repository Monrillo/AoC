# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 11:29:28 2026

@author: castelf
"""
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day4.txt','r') as f: lines=f.readlines()

# lines=['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
# '',
# '22 13 17 11  0',
# ' 8  2 23  4 24',
# '21  9 14 16  7',
# ' 6 10  3 18  5',
# ' 1 12 20 15 19',
# '',
# ' 3 15  0  2 22',
# ' 9 18 13 17  5',
# '19  8  7 25 23',
# '20 11 10 24  4',
# '14 21 16 12  6',
# '',
# '14 21 17 24  4',
# '10 16 15  9 19',
# '18  8 23 26 20',
# '22 11 13  6  5',
# ' 2  0 12  3  7']

tirage=[int(x) for x in lines[0].strip('\n').split(',')]
cards=[]
mat=[]

for line in lines[2:]:
    if line.strip('\n')=='':
        card= {'card': np.array(mat), 'bingo':False}
        cards.append(card)
        mat=[]
    else: mat.append([int(x) for x in line.strip('\n').split()])
card= {'card': np.array(mat), 'bingo':False}
cards.append(card)

results=[]

for t in tirage:
    for c in cards:
        if not c['bingo']:
            c['card'][c['card']==t]=-1
            if any(np.sum(c['card'],axis=0)==-5) or any(np.sum(c['card'],axis=1)==-5):
                c['card'][c['card']==-1]=0
                results.append(np.sum(c['card'])*t)
                c['bingo']=True


print("Part 1:", results[0])

print("Part 2:", results[-1])
