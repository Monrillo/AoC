# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 13:07:37 2026

@author: castelf
"""

test='target area: x=20..30, y=-10..-5'

inp='target area: x=253..280, y=-73..-46'

class Bullet:
    
    def __init__(self,vx,vy):
        self.x = 0
        self.y = 0
        self.out = False
        self.touch = False
        self.vx = vx
        self.vy = vy
        self.height = [self.y]
    
    def step(self):
        self.x+=self.vx
        self.y+=self.vy
        self.vy-=1
        if self.vx>0:self.vx-=1
        self.height.append(self.y)
        
    def check(self):
        if self.x>280 or self.y<-73:self.out=True
        elif 253<=self.x<=280 and -73<=self.y<=-46:self.touch=True

    #def check(self):
    #    if self.x>30 or self.y<-10:self.out=True
    #    elif 20<=self.x<=30 and -10<=self.y<=-5:self.touch=True
    
    def launch(self):
        while not self.out and not self.touch:
            self.step()
            self.check()
    
    def get_max(self):
        return max(self.height)


if __name__ == '__main__':
    height=[]
    for x in range(1000):
        for y in range(-100,1000):
            b=Bullet(x,y)
            b.launch()
            if b.touch:height.append(b.get_max())
    print("Part 1:",max(height))
    print("Part 2:",len(height))