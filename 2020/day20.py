# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 15:48:01 2025

@author: castelf
"""

import numpy as np
import itertools as it
import re

#with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day20test.txt','r') as f: lines=f.readlines()
with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day20.txt','r') as f: lines=f.readlines()

tiles=[]
tiles_id=[]
tiles_voisin={}
ops = [(0, slice(None)),(-1, slice(None)),(slice(None), 0),(slice(None), -1)]
mat=[] # juste pour enlever l'alarme code analysis

def check(t1,t2):
    res=0
    res+=sum(np.array_equiv(t1[i[0]], t2[i[1]]) for i in it.product(ops, repeat=2))
    res+=sum(np.array_equiv(np.flip(t1[i[0]]), t2[i[1]]) for i in it.product(ops, repeat=2))
    return res

def check_tile(l1,t2):
    good=False
    for k in range(4):
        if np.array_equiv(l1, np.rot90(t2,k=k)[:,0]):
            good=True
            res=np.rot90(t2,k=k)
            break
    if not good:
        for k in range(4):
            if np.array_equiv(l1, np.rot90(np.fliplr(t2),k=k)[:,0]):
                good=True
                res=np.rot90(np.fliplr(t2),k=k)
                break
    if good:return good,res
    else: return good,None

def check_first(bl,t2):
    good=False
    for k in range(4):
        if np.array_equiv(bl, np.rot90(t2,k=k)[0,:]):
            good=True
            res=np.rot90(t2,k=k)
            break
    if not good:
        for k in range(4):
            if np.array_equiv(bl, np.rot90(np.fliplr(t2),k=k)[0,:]):
                good=True
                res=np.rot90(np.fliplr(t2),k=k)
                break
    if good:return good,res
    else: return good,None

for line in lines:
    if line.strip()=='': tiles.append(np.array(mat))
    elif line.strip()[0]=='T':
        mat=[]
        tiles_id.append(int(line.strip()[5:9]))
        tiles_voisin[int(line.strip()[5:9])]=[]
    else: mat.append(list(line.strip()))
tiles.append(np.array(mat))

for i in range(len(tiles)):
    for j in range(len(tiles)):
        if i!=j and check(tiles[i],tiles[j])==1:
            tiles_voisin[tiles_id[i]].append(tiles_id[j])

corner=[]
bord=[]
resultat=1
for k in tiles_voisin:
    if len(tiles_voisin[k])==2: resultat*=k;corner.append(k)
    elif len(tiles_voisin[k])==3:bord.append(k)
print("Part 1:",resultat)

longueur=int(np.sqrt(len(tiles)))
image=np.zeros((longueur,longueur),dtype=int)

# Premier coin
image[0,0]=corner[0]
voisins=tiles_voisin.pop(corner[0])

# Initialisation
image[0,1]=voisins[0];image[1,0]=voisins[1]

# Première bande
for i in range(1,longueur-2):
    p=image[0,i]
    voisins=tiles_voisin.pop(p)
    for v in voisins:
        if v in image: continue
        elif v in bord: image[0,i+1]=v
        else: image[1,i]=v

# Second coin
voisins=tiles_voisin.pop(image[0,longueur-2])
for v in voisins:
    if v in image: continue
    elif v in corner: image[0,longueur-1]=v
    else: image[1,longueur-2]=v
voisins=tiles_voisin.pop(image[0,longueur-1])
if voisins[0] in image: image[1,longueur-1]=voisins[1]
else: image[1,longueur-1]=voisins[0]

# Autre bande
for l in range(1,longueur):
    for i in range(0,longueur):
        p=image[l,i]
        voisins=tiles_voisin.pop(p)
        for v in voisins:
            if v in image: continue
            else: image[l+1,i]=v

# i=1
# # Autre bande
# for l in range(1,longueur-2):
#     voisins=tiles_voisin.pop(image[l,0])
#     for v in voisins:
#         if v in image: continue
#         elif v in bord: image[l+1,0]=v
#         else: image[l,1]=v
#     for i in range(1,longueur-2):
#         p=image[l,i]
#         voisins=tiles_voisin.pop(p)
#         for v in voisins:
#             if v in image: continue
#             elif image[l-1,i+1] in tiles_voisin[v]: image[l,i+1]=v
#             else: image[l+1,i]=v
#     voisins=tiles_voisin.pop(image[l,longueur-2])
#     for v in voisins:
#         if v in image: continue
#         elif v in bord: image[l,longueur-1]=v
#         else: image[l+1,longueur-2]=v
#     voisins=tiles_voisin.pop(image[l,longueur-1])
#     if voisins[0] in image: image[l+1,longueur-1]=voisins[1]
#     else: image[l+1,longueur-1]=voisins[0]

# # Dernière bande
# voisins=tiles_voisin.pop(image[longueur-2,0])
# for v in voisins:
#     if v in image: continue
#     elif v in corner: image[longueur-1,0]=v
    
# for i in range(0,longueur-1):
#     p=image[longueur-1,i]
#     voisins=tiles_voisin.pop(p)
#     for v in voisins:
#         if v in image: continue
#         else: image[longueur-1,i+1]=v

# The entire matrix

# Première ligne
t1=tiles[tiles_id.index(image[0,0])]
t2=tiles[tiles_id.index(image[0,1])]
init=False
while not init:
    for k in range(4):
        if not init and check_tile(np.rot90(t1,k=k)[:,-1], t2)[0]:
            line=np.concatenate((np.rot90(t1,k=k),check_tile(np.rot90(t1,k=k)[:,-1], t2)[1]),axis=1)
            init=True
    for k in range(4):
        if not init and check_tile(np.rot90(np.flip(t1),k=k)[:,-1], t2)[0]:
            line=np.concatenate((np.rot90(np.flip(t1),k=k),check_tile(np.rot90(t1,k=k)[:,-1], t2)[1]),axis=1)
            init=True
    
for i in range(2,longueur):
    tile=tiles[tiles_id.index(image[0,i])]
    if check_tile(line[:,-1], tile)[0]:line=np.concatenate((line,check_tile(line[:,-1], tile)[1]),axis=1)
    else:
        line=np.flipud(line)
        line=np.concatenate((line,check_tile(line[:,-1], tile)[1]),axis=1)

matrix=line

# Deuxième ligne
tile=tiles[tiles_id.index(image[1,0])]
if check_first(matrix[-1,:10], tile)[0]:line=check_first(matrix[-1,:10], tile)[1]
else:
    matrix=np.flipud(matrix)
    line=check_first(matrix[-1,:10], tile)[1]
for i in range(1,longueur):
    tile=tiles[tiles_id.index(image[1,i])]
    line=np.concatenate((line,check_tile(line[:,-1], tile)[1]),axis=1)
matrix=np.concatenate((matrix,line),axis=0)

# Autre ligne
for l in range(2,longueur):
    tile=tiles[tiles_id.index(image[l,0])]
    line=check_first(matrix[-1,:10], tile)[1]
    for i in range(1,longueur):
        tile=tiles[tiles_id.index(image[l,i])]
        line=np.concatenate((line,check_tile(line[:,-1], tile)[1]),axis=1)
    matrix=np.concatenate((matrix,line),axis=0)

# Matrice réduite
cut_matrix=np.zeros((matrix.shape[0]-2*longueur,matrix.shape[1]-2*longueur),dtype=str)
for l in range(longueur):
    for c in range(longueur):
        cut_matrix[l*8:(l+1)*8,c*8:(c+1)*8]=matrix[(l*10)+1:(l*10)+9,(c*10)+1:(c*10)+9]

# Sea monster
monster='                  # '+'#    ##    ##    ###'+' #  #  #  #  #  #   '
pattern=[m.start() for m in re.finditer('#',monster)]

def scan(cm):
    num_mons=0
    for l in range(cm.shape[0]-3):
        for c in range(cm.shape[1]-20):
            zoom=cm[l:l+3,c:c+20]
            phrase=''.join(list(zoom[0])+list(zoom[1])+list(zoom[2]))
            pat=[m.start() for m in re.finditer('#',phrase)]
            if all(p in pat for p in pattern):num_mons+=1
    return num_mons

resultat=0
while resultat==0:
    for k in range(4):
        resultat=scan(np.rot90(cut_matrix,k=k))
        if resultat>0:break
        resultat=scan(np.rot90(np.fliplr(cut_matrix),k=k))
        if resultat>0:break

rough=len(np.where(cut_matrix=='#')[0])-resultat*len(pattern)

print("Part 2:",rough)
