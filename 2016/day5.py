# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:26:16 2025

@author: castelf
"""
import hashlib
import numpy as np

n=0
pwd=''
new_pwd=np.zeros(8,dtype=str)
cpt=0
while cpt<8:
    string='reyedfim'+str(n)
    hash = hashlib.md5(string.encode()).hexdigest()
    if hash[:5]=='00000':
        if len(pwd)<8:
            pwd+=hash[5]
        try:
            pos=int(hash[5])
            if new_pwd[pos]=='':
                new_pwd[pos]=hash[6]
                cpt+=1
        except:
            pass
    n+=1

print(pwd)
print(''.join(new_pwd))