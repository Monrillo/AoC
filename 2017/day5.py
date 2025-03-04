# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:00:46 2025

@author: castelf
"""

line=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day5.txt','r').read()
jump=[int(x) for x in line.split()]

jump2=jump.copy()

cpt=0
j=0
while 0<=cpt<len(jump):
    n_cpt=cpt+jump[cpt]
    jump[cpt]+=1
    j+=1
    cpt=n_cpt

print(j)

cpt=0
j=0
while 0<=cpt<len(jump2):
    n_cpt=cpt+jump2[cpt]
    if jump2[cpt]>=3: jump2[cpt]-=1
    else: jump2[cpt]+=1
    j+=1
    cpt=n_cpt

print(j)