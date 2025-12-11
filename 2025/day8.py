# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 16:10:38 2025

@author: castelf
"""
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day8.txt','r') as f: lines=f.readlines()

# lines=['162,817,812',
# '57,618,57',
# '906,360,560',
# '592,479,940',
# '352,342,300',
# '466,668,158',
# '542,29,236',
# '431,825,988',
# '739,650,466',
# '52,470,668',
# '216,146,977',
# '819,987,18',
# '117,168,530',
# '805,96,715',
# '346,949,466',
# '970,615,88',
# '941,993,340',
# '862,61,35',
# '984,92,344',
# '425,690,689']

junction=np.array([[int(x) for x in l.strip('\n').split(',')] for l in lines],dtype=np.int64)
distance=np.zeros((len(junction),len(junction)),dtype=float)

# def dist(j1,j2):
#     x1,y1,z1=j1
#     x2,y2,z2=j2
#     return np.sqrt(abs(x2-x1)+abs(y2-y1)+abs(z2-z1))

for l in range(len(junction)-1):
    for c in range(l+1,len(junction)):
        distance[l][c]=np.linalg.norm(junction[l]-junction[c])
maxi=np.max(distance)+1
distance[distance==0.]=maxi

circuits=[]
n=0
while True:
    n+=1
    f=np.where(distance==np.min(distance))[0][0]
    s=np.where(distance==np.min(distance))[1][0]
    distance[f,s]=maxi
    
    pf=-1
    ps=-1
    for i,c in enumerate(circuits):
        if f in c and pf==-1:pf=i
        if s in c and ps==-1:ps=i
    
    if pf==-1 and ps==-1: circuits.append([f,s])
    elif pf==-1 and ps!=-1: circuits[ps].append(f)
    elif pf!=-1 and ps==-1: circuits[pf].append(s)
    elif pf!=-1 and ps!=-1 and pf!=ps:
        circuits[pf]+=circuits[ps]
        circuits.pop(ps)
    
    if n==1000:size=sorted([len(c) for c in circuits])
        
    if len(circuits[0])>=len(junction):break

print("Part 1:",size[-3]*size[-2]*size[-1])

print("Part 2:",junction[f][0]*junction[s][0])
