# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:12:47 2025

@author: castelf
"""
import numpy as np

matrix=np.zeros((6,50),dtype=int)

inst='rotate column x=1 by 1'.split()

instructions=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day8.txt')]
for inst in instructions:
    if inst[0]=='rect': matrix[:int(inst[1].split('x')[1]),:int(inst[1].split('x')[0])]=1
    elif inst[0]=='rotate':
        if inst[1]=='row':
            matrix[:]
        elif inst[1]=='column':
            matrix[:,int(inst[2].split('=')[1])]=\
                np.concatenate((matrix[-int(inst[-1])%6:,int(inst[2].split('=')[1])],matrix[:-int(inst[-1])%6,int(inst[2].split('=')[1])]))
        

instructions[0][1].split('x')
instructions[1]


7%6
