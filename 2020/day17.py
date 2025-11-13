# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 11:12:39 2025

@author: castelf
"""

import numpy as np
import itertools as it

# Reading state

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day17.txt','r') as f: lines=f.readlines()

# lines=['.#.',
# '..#',
# '###']

mat=[list(l.strip()) for l in lines]

# Implementing cubes
padding=16
cube=np.zeros((len(mat)+padding,len(mat)+padding,len(mat)+padding),dtype=bool)
hypercube=np.zeros((len(mat)+padding,len(mat)+padding,len(mat)+padding,len(mat)+padding),dtype=bool)

# Initial state
for i in range(len(mat)):
     for j in range(len(mat[i])):
         if mat[i][j]=='#':
             cube[padding//2+i,padding//2+j,(len(mat)+padding)//2]=True
             hypercube[padding//2+i,padding//2+j,(len(mat)+padding)//2,(len(mat)+padding)//2]=True

# Functions
def voisin_3(pos):
    t=0
    for i in it.product((pos[0]-1,pos[0],pos[0]+1),\
                        (pos[1]-1,pos[1],pos[1]+1),\
                            (pos[2]-1,pos[2],pos[2]+1)):
        if i!=pos and cube[i]:t+=1
    return t

def voisin_4(pos):
    t=0
    for i in it.product((pos[0]-1,pos[0],pos[0]+1),\
                        (pos[1]-1,pos[1],pos[1]+1),\
                            (pos[2]-1,pos[2],pos[2]+1),\
                            (pos[3]-1,pos[3],pos[3]+1)):
        if i!=pos and hypercube[i]:t+=1
    return t

# The loop
num_cycle=6
for c in range(num_cycle):
    
    # Cube
    next_cube=np.zeros((len(mat)+padding,len(mat)+padding,len(mat)+padding),dtype=bool)
    
    for i in it.product(range(np.min(np.where(cube)[0])-1,np.max(np.where(cube)[0])+2),\
                        range(np.min(np.where(cube)[1])-1,np.max(np.where(cube)[1])+2),\
                            range(np.min(np.where(cube)[2])-1,np.max(np.where(cube)[2])+2)):
        if cube[i] and (voisin_3(i)==2 or voisin_3(i)==3):
            next_cube[i]=True
        if not cube[i] and voisin_3(i)==3:
            next_cube[i]=True
    
    cube=next_cube
    
    # Hypercube
    next_hypercube=np.zeros((len(mat)+padding,len(mat)+padding,len(mat)+padding,len(mat)+padding),dtype=bool)
    
    for i in it.product(range(np.min(np.where(hypercube)[0])-1,np.max(np.where(hypercube)[0])+2),\
                        range(np.min(np.where(hypercube)[1])-1,np.max(np.where(hypercube)[1])+2),\
                            range(np.min(np.where(hypercube)[2])-1,np.max(np.where(hypercube)[2])+2),\
                            range(np.min(np.where(hypercube)[3])-1,np.max(np.where(hypercube)[3])+2)):
        if hypercube[i] and (voisin_4(i)==2 or voisin_4(i)==3):
            next_hypercube[i]=True
        if not hypercube[i] and voisin_4(i)==3:
            next_hypercube[i]=True
    
    hypercube=next_hypercube

print("Part 1:",np.sum(cube))
print("Part 2:",np.sum(hypercube))
