# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 10:13:11 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day13.txt','r') as f: lines=f.readlines()

# lines=['6,10',
# '0,14',
# '9,10',
# '0,3',
# '10,4',
# '4,11',
# '6,0',
# '6,12',
# '4,1',
# '0,13',
# '10,12',
# '3,4',
# '3,0',
# '8,4',
# '1,10',
# '2,14',
# '8,10',
# '9,0',
# '',
# 'fold along y=7',
# 'fold along x=5']

fold=False
points=set()
folding=[]
for line in lines:
    if line.strip('\n')=='':fold=True
    else:
        if not fold:
            points.add((int(line.strip('\n').split(',')[0]),int(line.strip('\n').split(',')[1])))
        else:
            folding.append([line.strip('\n').strip('fold along ').split('=')[0],int(line.strip('\n').strip('fold along ').split('=')[1])])

for step,f in enumerate(folding):
    new_points=set()
    for p in list(points):
        if f[0]=='x' and p[0]>f[1]:new_points.add((2*f[1]-p[0],p[1]))
        elif f[0]=='y' and p[1]>f[1]:new_points.add((p[0],2*f[1]-p[1]))
        else: new_points.add((p[0],p[1]))
    points=new_points.copy()
    if step==0:result_1=len(points)

print("Part 1:",result_1)  

points=np.array(list(points))
matrix=np.full((np.max(points[:,0]+1),np.max(points[:,1]+1)),'.')
matrix[points[:,0],points[:,1]]='#'
matrix=matrix.T

pos=0
for i in range(matrix.shape[1]):
    if np.array_equiv(matrix[:,i],np.full((matrix.shape[0],1),'.')):
        print(matrix[:,pos:i])
        print(' ')
        pos=i+1
print(matrix[:,pos:])

matrix[:,0]
