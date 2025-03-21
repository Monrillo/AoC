# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:34:31 2025

@author: castelf
"""

games=[line.strip().split(':')[1].split('; ') for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day2.txt','r')]
res1=0
res2=0
for num,game in enumerate(games):
    good=True
    rm=gm=bm=0
    for s in range(len(game)):
        balls=game[s].split(', ')
        r=g=b=0
        for ball in balls:
            if ball.split()[1]=='red':
                r=int(ball.split()[0])
                if r>rm:rm=r
            elif ball.split()[1]=='green':
                g=int(ball.split()[0])
                if g>gm:gm=g
            elif ball.split()[1]=='blue':
                b=int(ball.split()[0])
                if b>bm:bm=b
        if r>12 or g>13 or b>14:good=False
    res2+=rm*bm*gm
    if good:res1+=(num+1)
print(res1)
print(res2)

