# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 13:24:29 2025

@author: castelf
"""

# Input from file
#
# <x=-6, y=2, z=-9>
# <x=12, y=-14, z=-4>
# <x=9, y=5, z=-6>
# <x=-1, y=-4, z=9>

# Test
#
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>

class Moon:
    def __init__(self, pos_x, pos_y, pos_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
    
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

a=Moon(-6,2,-9)
b=Moon(12,-14,-4)
c=Moon(9,5,-6)
d=Moon(-1,-4,9)

moons=[a,b,c,d]

for _ in range(1000):
    for m1 in moons:
        for m2 in moons:
            if m1!=m2:
                m1.attract(m2)
    for m1 in moons: m1.move()
total_energy=0
for m1 in moons: total_energy+=m1.get_energy()

print(total_energy)
