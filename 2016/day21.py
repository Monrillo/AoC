# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:59:50 2025

@author: castelf
"""

def swap(x,y,pwd): return pwd[:min(x,y)]+pwd[max(x,y)]+pwd[min(x,y)+1:max(x,y)]+pwd[min(x,y)]+pwd[max(x,y)+1:]
def reverse(x,y,pwd): return pwd[:min(x,y)]+pwd[min(x,y):max(x,y)+1][::-1]+pwd[max(x,y)+1:]
def rotatel(x,pwd): return pwd[x%len(pwd):]+pwd[:x%len(pwd)]
def rotater(x,pwd): return pwd[-x%len(pwd):]+pwd[:-x%len(pwd)]
def move(x,y,pwd):
    if y>x: return pwd[:x]+pwd[x+1:y+1]+pwd[x]+pwd[y+1:]
    elif x>y: return pwd[:y]+pwd[x]+pwd[y:x]+pwd[x+1:]
def rotateb(x,pwd):
    if pwd.find(x)>=4: return rotater(pwd.find(x)+2,pwd)
    else: return rotater(pwd.find(x)+1,pwd)
inv={1:1, 3:2, 5:3, 7:4, 2:6, 4:7, 6:8, 0:9}
def invrotateb(x,pwd): return rotatel(inv[pwd.find(x)],pwd)

instructions=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day21.txt')] 

pwd='abcdefgh'
for ins in instructions:
    if ins[0]=='swap' and ins[1]=='position': pwd=swap(int(ins[2]),int(ins[5]),pwd)
    elif ins[0]=='swap' and ins[1]=='letter': pwd=swap(pwd.find(ins[2]),pwd.find(ins[5]),pwd)
    elif ins[0]=='reverse': pwd=reverse(int(ins[2]),int(ins[4]),pwd)
    elif ins[0]=='rotate' and ins[1]=='left': pwd=rotatel(int(ins[2]),pwd)
    elif ins[0]=='rotate' and ins[1]=='right': pwd=rotater(int(ins[2]),pwd)
    elif ins[0]=='rotate' and ins[1]=='based': pwd=rotateb(ins[6],pwd)
    elif ins[0]=='move': pwd=move(int(ins[2]),int(ins[5]),pwd)
print(pwd)

pwd='fbgdceah'
for ins in instructions[::-1]:
    if ins[0]=='swap' and ins[1]=='position': pwd=swap(int(ins[5]),int(ins[2]),pwd)
    elif ins[0]=='swap' and ins[1]=='letter': pwd=swap(pwd.find(ins[5]),pwd.find(ins[2]),pwd)
    elif ins[0]=='reverse': pwd=reverse(int(ins[2]),int(ins[4]),pwd)
    elif ins[0]=='rotate' and ins[1]=='left': pwd=rotater(int(ins[2]),pwd)
    elif ins[0]=='rotate' and ins[1]=='right': pwd=rotatel(int(ins[2]),pwd)
    elif ins[0]=='rotate' and ins[1]=='based': pwd=invrotateb(ins[6],pwd)
    elif ins[0]=='move': pwd=move(int(ins[(5)]),int(ins[2]),pwd)
print(pwd)
