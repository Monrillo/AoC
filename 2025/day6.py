# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 15:43:52 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day6.txt','r') as f: lines=f.readlines()

mat=[list(l.strip().split()) for l in lines]
ops=mat[4]
res=[eval(mat[0][i]+ops[i]+mat[1][i]+ops[i]+mat[2][i]+ops[i]+mat[3][i]) for i in range(len(mat[0]))]

print("Part 1:",sum(res))

# lines=['123 328  51 64 ',
# ' 45 64  387 23 ',
# '  6 98  215 314',
# '               ',
# '*   +   *   +  ']

mat_2=[l.strip('\n') for l in lines]
ops_2=mat_2[4]
resultat_2=0
nums=[]
for i in range(len(ops_2)-1,-1,-1):
    if ops_2[i]!=' ':
        nums.append(''.join([mat_2[j][i] for j in range(len(mat_2)-1)]).strip())
        resultat_2+=eval(''.join(n+ops_2[i] for n in nums)[:-1])
    elif mat_2[0][i]==mat_2[1][i]==mat_2[2][i]==mat_2[3][i]==ops_2[i]==' ':
        nums=[]
    else:
        nums.append(''.join([mat_2[j][i] for j in range(len(mat_2)-1)]).strip())
        
print("Part 2:",resultat_2)
