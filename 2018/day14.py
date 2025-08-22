# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 16:49:05 2025

@author: castelf
"""
#Initial
score='37'
r1=0
r2=1

#Input
recipe='765071'

while recipe not in score[-7:]:
    score+=str(int(score[r1]) + int(score[r2]))
    r1=(r1 +1 +int(score[r1])) % len(score)
    r2=(r2 +1 +int(score[r2])) % len(score)

print(score[int(recipe):int(recipe)+10])
print(len(score)-7)
