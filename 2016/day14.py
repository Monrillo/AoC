# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:06:34 2025

@author: castelf
"""

import hashlib
import re
#import numpy as np

salt='abc'
n=0
triple=[]
key_pad=[]

while len(key_pad)<64:
    string=salt+str(n)
    h = hashlib.md5(string.encode()).hexdigest()
    trip=re.search(r'(\w)(\1)(\1)',h)
    for key in triple:
        if key[0]*5 in h: key_pad.append(key[1]);triple.remove(key);continue
        if (n-key[1])>1000: triple.remove(key)
    if trip: triple.append([trip.group()[0],n])
    n+=1
    
print(sorted(key_pad))
len(key_pad)


for i in range(1000):
    string=salt+str(n)
    h = hashlib.md5(string.encode()).hexdigest()
    trip=re.search(r'(\w)(\1)(\1)',h)
    for key in triple:
        if key[0]*5 in h: key_pad.append(key);triple.remove(key);continue
        if (n-key[1])>1000: triple.remove(key)
    if trip: triple.append([trip.group()[0],n])
    n+=1


string=salt+str(39)
h = hashlib.md5(string.encode()).hexdigest()
print(h)