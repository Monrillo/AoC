# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:59:50 2025

@author: castelf
"""

test='abcde'

def swapp(x,y,pwd): return pwd[:min(x,y)]+pwd[max(x,y)]+pwd[min(x,y)+1:max(x,y)]+pwd[min(x,y)]+pwd[max(x,y)+1:]
def swapl(x,y,pwd): return swapp(pwd.find(x),pwd.find(y),pwd)
def reverse(x,y,pwd): return pwd[:min(x,y)]+pwd[min(x,y):max(x,y)+1][::-1]+pwd[max(x,y)+1:]
def rotatel(x,pwd): return pwd[x:]+pwd[:x]
def rotater(x,pwd): return pwd[-x:]+pwd[:-x]
def move(x,y,pwd):
    if y>x: return pwd[:x]+pwd[x+1:y+1]+pwd[x]+pwd[y+1:]
    elif x>y: return pwd[:y]+pwd[x]+pwd[y:x]+pwd[x+1:]
    
    
    
pwd='abdec'
x=3
y=0
move(x,y,pwd)
