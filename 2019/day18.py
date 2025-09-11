# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 11:53:01 2025

@author: castelf
"""
import networkx as nx
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day18.txt','r') as f: lines=f.readlines()

lines = ['#########',
'#b.A.@.a#',
'#########']

matrix=[]
for l in lines: matrix.append([x for x in list(l.strip())])
matrix=np.array(matrix)

keys=list('abcdefghijklmnopqrstuvwxyz')
doors=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

pos=(np.where(matrix=='@')[0][0],np.where(matrix=='@')[1][0])
matrix[pos]='.'

key_list=[]
for k in keys:
    if len(np.where(matrix==k)[0])>0:key_list.append((np.where(matrix==k)[0][0],np.where(matrix==k)[1][0]))

G = nx.Graph()


