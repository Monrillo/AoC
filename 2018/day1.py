# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 13:37:46 2025

@author: castelf
"""

import itertools as it

liste=[int(l) for l in open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day1.txt','r')]
print(sum(liste))

freq=0
liste_freq=set()
for num in it.cycle(liste):
    freq+=num
    if freq in liste_freq:print(freq);break
    liste_freq.add(freq)
