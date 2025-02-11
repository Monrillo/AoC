# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:01:35 2025

@author: castelf
"""

def dragon(a):
    b=''
    for c in a:
        if c=='1': b+='0'
        else: b+='1'
    return a+'0'+b[::-1]

def checksum(a):
    res=''
    for i in range(0,len(a),2):
        x,y=a[i:i+2]
        if x==y: res+='1'
        else: res+='0'
    return res

# num='10000'
# size=20
num='10001001100000001'
size=35651584

while len(num)<=size:
    num=dragon(num)

res=checksum(num[:size])

while len(res)%2!=1:
    res=checksum(res)

print(res)
