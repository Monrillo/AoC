# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 15:08:02 2025

@author: castelf
"""
import time

# a=65
# b=8921

a=516
b=190

# start=time.time()

# res=0
# for _ in range(int(4e7)):
#     a=(a*16807)%2147483647
#     b=(b*48271)%2147483647
#     if bin(a)[-16:]==bin(b)[-16:]: res+=1

# end=time.time()
# print(res)
# print(end-start)

def gena(a):
    while True:
        a=(a*16807)%2147483647
        if a%4==0: break
    return a

def genb(b):
    while True:
        b=(b*48271)%2147483647
        if b%8==0: break
    return b

start=time.time()

res2=0
for _ in range(int(5e6)):
    a=gena(a)
    b=genb(b)
    if bin(a)[-16:]==bin(b)[-16:]: res2+=1

end=time.time()
print(res2)
print(end-start)
