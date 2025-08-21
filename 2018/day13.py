# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 16:15:18 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day13.txt','r') as f: lines=f.readlines()

import numpy as np

# lines=[
# "/->-\        ",
# "|   |  /----\\",
# "| /-+--+-\  |",
# "| | |  | v  |",
# "\-+-/  \-+--/",
# "  \------/   "]

# lines=[
# "/>-<\  ",
# "|   |  ",
# "| /<+-\\",
# "| | | v",
# "\>+</ |",
# "  |   ^",
# "  \<->/"]

mat=[list(l) for l in lines]
matrix=np.array([l[:150] for l in mat])
#matrix=np.array(mat)

class Cart:
    def __init__(self, pos, di):
        self.pos =  pos
        self.di = di
        self.inter = 'lsr'
        self.dead = False
        
    def turn_l(self):
        self.di=self.di[-1]+self.di[:-1]
    
    def turn_r(self):
        self.di=self.di[1:]+self.di[0]
        
    def intersect(self):
        if self.inter[0]=='l': self.turn_l()
        elif self.inter[0]=='r': self.turn_r()
        self.inter=self.inter[1:]+self.inter[0]
    
    def get_dir(self):
        return self.di[0]
    
    def move(self):
        if self.di[0]=='u':self.pos=(self.pos[0]-1,self.pos[1])
        elif self.di[0]=='d':self.pos=(self.pos[0]+1,self.pos[1])
        elif self.di[0]=='l':self.pos=(self.pos[0],self.pos[1]-1)
        elif self.di[0]=='r':self.pos=(self.pos[0],self.pos[1]+1)
    
    def crash(self):
        self.dead=True

def add_cart(x,y,d):
    ca=Cart((x,y),d)
    if ca.get_dir() in ['l','r']: matrix[ca.pos]='-'
    elif ca.get_dir() in ['u','d']: matrix[ca.pos]='|'
    return ca

carts=[]

while np.where(matrix=='>')[0].size>0:
    carts.append(add_cart(list(np.where(matrix=='>')[0]).pop(0),list(np.where(matrix=='>')[1]).pop(0),'rdlu'))
while np.where(matrix=='<')[0].size>0:
    carts.append(add_cart(list(np.where(matrix=='<')[0]).pop(0),list(np.where(matrix=='<')[1]).pop(0),'lurd'))
while np.where(matrix=='^')[0].size>0:
    carts.append(add_cart(list(np.where(matrix=='^')[0]).pop(0),list(np.where(matrix=='^')[1]).pop(0),'urdl'))
while np.where(matrix=='v')[0].size>0:
    carts.append(add_cart(list(np.where(matrix=='v')[0]).pop(0),list(np.where(matrix=='v')[1]).pop(0),'dlur'))

first_crash=True
while len(carts)>1:
    carts.sort(key=lambda x: x.pos)
    for cart in carts:
        cart.move()
        if matrix[cart.pos]=='+':cart.intersect()
        elif matrix[cart.pos]=='/' and cart.get_dir() in ['u','d']:cart.turn_r()
        elif matrix[cart.pos]=='/' and cart.get_dir()in ['l','r']:cart.turn_l()
        elif matrix[cart.pos]=='\\' and cart.get_dir() in ['u','d']:cart.turn_l()
        elif matrix[cart.pos]=='\\' and cart.get_dir() in ['l','r']:cart.turn_r()
        if [ca.pos for ca in carts].count(cart.pos)==2:
            for ca in carts:
                if ca.pos == cart.pos: ca.crash()
            if first_crash: print(cart.pos); first_crash=False
    if any(c.dead for c in carts): carts=[ca for ca in carts if not ca.dead]

print(carts[0].pos)
