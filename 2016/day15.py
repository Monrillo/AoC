# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:57:12 2025

@author: castelf
"""

disc={}
for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day15.txt'):
    disc[int(line.split()[1][1:])]=(int(line.split()[-1][:-1]),int(line.split()[3]))

# d_1=4 # 5 positions
# d_2=1 # 2 positions

# disc={}
# disc[1]=(4,5)
# disc[2]=(1,2)

time=0
while True:
    res=0
    for k in disc.keys(): res+=(disc[k][0]+k+time)%disc[k][1]
    if res==0: print('p1 : '+str(time));break
    time+=1

disc[len(disc)+1]=(0,11)

time=0
while True:
    res=0
    for k in disc.keys(): res+=(disc[k][0]+k+time)%disc[k][1]
    if res==0: print('p2 : '+str(time));break
    time+=1