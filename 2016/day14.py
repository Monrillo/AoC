# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:06:34 2025

@author: castelf
"""

from hashlib import md5
import re
#import numpy as np

#salt='abc'
salt='ihaygndm'
n=0
triple=[]
key_pad=[]
debug=[]

while len(key_pad)<64:
    string=salt+str(n)
    h = md5(string.encode()).hexdigest()
    for _ in range(2016): h=md5(h.encode()).hexdigest()
    trip=re.search(r'(\w)(\1)(\1)',h)
    for key in triple:
        if (key[0]*5 in h) and ((n-key[1])<=1000): key_pad.append(key[1]);debug.append((key,n,(n-key[1])))
    if trip: triple.append([trip.group()[0],n])
    n+=1
    
print(sorted(key_pad)[63])

