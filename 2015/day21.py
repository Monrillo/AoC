# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:37:05 2025

@author: castelf
"""

import itertools as it

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

class Object:
    def __init__(self, cost, damage, armor):
        self.damage = damage
        self.armor = armor
        self.cost = cost
    
    def get_cost(self): return self.cost
        
Dagger=Object(8,4,0)
Shortsword=Object(10,5,0)
Warhammer=Object(25,6,0)
Longsword=Object(40,7,0)
Greataxe=Object(74,8,0)

Weapons=[Dagger,Shortsword,Warhammer,Longsword,Greataxe]

No_armor=Object(0,0,0)
Leather=Object(13,0,1)
Chainmail=Object(31,0,2)
Splintmail=Object(53,0,3)
Bandedmail=Object(75,0,4)
Platemail=Object(102,0,5)

Armor=[No_armor,Leather,Chainmail,Splintmail,Bandedmail,Platemail]

No_ring_l=Object(0,0,0)
No_ring_r=Object(0,0,0)
Dam_1=Object(25,1,0)
Dam_2=Object(50,2,0)
Dam_3=Object(100,3,0)
Def_1=Object(20,0,1)
Def_2=Object(40,0,2)
Def_3=Object(80,0,3)

Rings=[No_ring_l,No_ring_r,Dam_1,Dam_2,Dam_3,Def_1,Def_2,Def_3]
Ring_1=[]
Ring_2=[]
for a,b in it.combinations(Rings, 2):Ring_1.append(a);Ring_2.append(b)

combinations = it.product(Weapons,Armor,Ring_1,Ring_2)

class Person:
    def __init__(self, damage, armor, health):
        self.damage = damage
        self.armor = armor
        self.health = health
    
    def hit(self, dam): self.health-=max(dam-self.armor,1)
    
    def attack(self): return self.damage
    
    def alive(self): return self.health>0


class Human(Person):
    def equip(self, Object):
        self.damage+=Object.damage
        self.armor+=Object.armor

winning=[]
lost=[]
for comb in combinations:
    cost=0
    boss=Person(8,1,104)
    player=Human(0,0,100)
    for item in comb:
        player.equip(item)
        cost+=item.get_cost()
        
    while True:
        boss.hit(player.attack())
        if not boss.alive(): win=True;break
        elif boss.alive():
            player.hit(boss.attack())
            if not player.alive(): win=False;break
    
    if win:winning.append(cost)
    else: lost.append(cost)

print(min(winning))
print(max(lost))
