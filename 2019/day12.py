# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 13:24:29 2025

@author: castelf
"""
import math
import numpy as np

def ppcm(a,b):
    return a * b // math.gcd(a, b)

# Input from file
#
# <x=-6, y=2, z=-9>
# <x=12, y=-14, z=-4>
# <x=9, y=5, z=-6>
# <x=-1, y=-4, z=9>

initial_a=(-6,2,-9,0,0,0)
initial_b=(12,-14,-4,0,0,0)
initial_c=(9,5,-6,0,0,0)
initial_d=(-1,-4,9,0,0,0)

# Test
#
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>

# initial_a=(-1,0,2,0,0,0)
# initial_b=(2,-10,-7,0,0,0)
# initial_c=(4,-8,8,0,0,0)
# initial_d=(3,5,-1,0,0,0)

# initial_a=(-8,-10,0,0,0,0)
# initial_b=(5,5,10,0,0,0)
# initial_c=(2,-7,3,0,0,0)
# initial_d=(9,-8,-3,0,0,0)

initials=np.vstack((np.array(initial_a),np.array(initial_b),np.array(initial_c),np.array(initial_d)))

class Moon:
    def __init__(self, state):
        self.pos_x = state[0]
        self.pos_y = state[1]
        self.pos_z = state[2]
        self.vel_x = state[3]
        self.vel_y = state[4]
        self.vel_z = state[5]
    
    def attract(self,m1):
        if m1.pos_x>self.pos_x:self.vel_x+=1
        elif m1.pos_x<self.pos_x:self.vel_x-=1
        if m1.pos_y>self.pos_y:self.vel_y+=1
        elif m1.pos_y<self.pos_y:self.vel_y-=1
        if m1.pos_z>self.pos_z:self.vel_z+=1
        elif m1.pos_z<self.pos_z:self.vel_z-=1
    
    def move(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z
        
    def get_energy(self):
        ep = abs(self.pos_x)+abs(self.pos_y)+abs(self.pos_z)
        ec = abs(self.vel_x)+abs(self.vel_y)+abs(self.vel_z)
        return ep*ec
    
    def get_state(self):
        return self.pos_x,self.pos_y,self.pos_z,self.vel_x,self.vel_y,self.vel_z

a=Moon(initial_a)
b=Moon(initial_b)
c=Moon(initial_c)
d=Moon(initial_d)

moons=[a,b,c,d]

period_x=period_y=period_z=0

step=0
while period_x==0 or period_y==0 or period_z==0:
    step+=1
    for m1 in moons:
        for m2 in moons:
            if m1!=m2:
                m1.attract(m2)
    for m1 in moons: m1.move()
    if step==1000:print(sum([m1.get_energy() for m1 in moons]))
    if (period_x==0 and all([m1.get_state()[0] for m1 in moons]==initials[:,0]) and all([m1.get_state()[3] for m1 in moons]==np.zeros(4))):
        period_x=step
    if (period_y==0 and all([m1.get_state()[1] for m1 in moons]==initials[:,1]) and all([m1.get_state()[4] for m1 in moons]==np.zeros(4))):
        period_y=step
    if (period_z==0 and all([m1.get_state()[2] for m1 in moons]==initials[:,2]) and all([m1.get_state()[5] for m1 in moons]==np.zeros(4))):
        period_z=step

print(ppcm(ppcm(period_x,period_y),period_z))



