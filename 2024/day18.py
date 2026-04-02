# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:38:18 2026

@author: castelf
"""
from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day18.txt','r') as f: lines=f.readlines()

# lines=['5,4',
# '4,2',
# '4,5',
# '3,0',
# '2,1',
# '6,3',
# '2,4',
# '1,5',
# '0,6',
# '3,3',
# '2,6',
# '5,1',
# '1,2',
# '5,5',
# '2,5',
# '6,5',
# '1,4',
# '0,4',
# '6,4',
# '1,1',
# '6,1',
# '1,0',
# '0,5',
# '1,6',
# '2,0']

corrupted=[(int(line.strip('\n').split(',')[0]),int(line.strip('\n').split(',')[1])) for line in lines]

def tracking(size,blocks):
    carte={}
    for l in range(size):
        for c in range(size):
            if l==0 or l==size-1 or c==0 or c==size-1:
                carte[(l,c)]='#'
            else:
                carte[(l,c)]=1000000
    for b in blocks:
        carte[(b[0]+1,b[1]+1)]='#'
    
    start=(1,1)
    end=(size-2,size-2)
    
    trackers=deque([(start,0)]) # position (l,c), score
    
    while trackers:    
        pos,score=trackers.popleft()
        if isinstance(carte[pos],int) and score<carte[pos]:
            carte[pos]=score
            trackers.append(((pos[0]+1,pos[1]),score+1))
            trackers.append(((pos[0]-1,pos[1]),score+1))
            trackers.append(((pos[0],pos[1]+1),score+1))
            trackers.append(((pos[0],pos[1]-1),score+1))
    
    return carte[end]

# print("Part 1:",tracking(9,corrupted[:12]))

# for i in range(12,len(corrupted)):
#     if tracking(9,corrupted[:i])==1000000:
#         print("Part 2:",corrupted[i-1])
#         break


print("Part 1:",tracking(73,corrupted[:1024]))

for i in range(1024,len(corrupted)):
    if tracking(73,corrupted[:i])==1000000:
        print("Part 2:",corrupted[i-1])
        break







