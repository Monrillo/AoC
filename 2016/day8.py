# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:12:47 2025

@author: castelf
"""
import numpy as np

matrix=np.zeros((6,50),dtype=int)
#matrix=np.zeros((3,7),dtype=int)

instructions=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day8.txt')]

# instructions=['rect 3x2\n',
# 'rotate column x=1 by 1\n',
# 'rotate row y=0 by 4\n',
# 'rotate column x=1 by 1']

for inst in instructions:
    #inst=inst.split()
    if inst[0]=='rect': matrix[:int(inst[1].split('x')[1]),:int(inst[1].split('x')[0])]=1
    elif inst[0]=='rotate':
        if inst[1]=='row':
            matrix[int(inst[2].split('=')[1]),:]=\
                np.concatenate((matrix[int(inst[2].split('=')[1]),-(int(inst[-1])%matrix.shape[1]):],matrix[int(inst[2].split('=')[1]),:-(int(inst[-1])%matrix.shape[1])]))
        elif inst[1]=='column':
            matrix[:,int(inst[2].split('=')[1])]=\
                np.concatenate((matrix[-(int(inst[-1])%matrix.shape[0]):,int(inst[2].split('=')[1])],matrix[:-(int(inst[-1])%matrix.shape[0]),int(inst[2].split('=')[1])]))
        
print(np.sum(matrix))
matrix=matrix.astype(str)
matrix[np.where(matrix=='1')]='\u2588'
matrix[np.where(matrix=='0')]='\u0020'
for i in range(10):
    print(matrix[:,5*i:5*(i+1)])

