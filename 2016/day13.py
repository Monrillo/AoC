# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:25:20 2025

@author: castelf
"""

import numpy as np

area=np.full((10,10),'.')
odfn=10
finish=(4,7)
# area=np.full((45,45),'.')
# odfn=1358
# finish=(39,31)
for x in range(len(area)):
    for y in range(len(area)):
        num=(x*x + 3*x + 2*x*y + y + y*y)+odfn
        if bin(num)[2:].count('1')%2==1: area[y,x]='#'
print(area)
pos=(1,1)
way=[pos]
way.append((2,1))
def move(w):
    y=w[-1][0];x=w[-1][1]
    pos_m=[]
    if y-1>=0 and area[y-1,x]=='.'and (y-1,x) not in w: pos_m.append((y-1,x))
    if y+1<len(area) and area[y+1,x]=='.'and (y+1,x) not in w: pos_m.append((y+1,x))
    if x-1>=0 and area[y,x-1]=='.'and (y,x-1) not in w: pos_m.append((y,x-1))
    if x+1<len(area) and area[y,x+1]=='.'and (y,x+1) not in w: pos_m.append((y,x+1))
    return pos_m

good_way=[]
bad_way=[]
for i in range(1000000):
    pos=(1,1)
    floor=area.copy()
    floor[pos]='O'
    way=[pos]
    while True:
        pos_move=move(pos[0],pos[1])
        if len(pos_move)==0: bad_way.append(way);break
        elif finish in pos_move: pos=finish;way.append(pos);good_way.append(way);break
        pos=pos_move[np.random.randint(len(pos_move))]
        way.append(pos)
        floor[pos]='O'

l=[len(x) for x in good_way]
np.where(l==np.min(l))[0][0]
res=good_way[np.where(l==np.min(l))[0][0]]
for p in res: area[p]='O'
print(area)
print(np.min(l)-1)