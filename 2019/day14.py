# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 09:52:53 2025

@author: castelf
"""
import math
#import numpy as np
#import pandas as pd

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day14.txt','r') as f: lines=f.readlines()

# lines = ['10 ORE => 10 A',
# '1 ORE => 1 B',
# '7 A, 1 B => 1 C',
# '7 A, 1 C => 1 D',
# '7 A, 1 D => 1 E',
# '7 A, 1 E => 1 FUEL']

# lines = ['9 ORE => 2 A',
# '8 ORE => 3 B',
# '7 ORE => 5 C',
# '3 A, 4 B => 1 AB',
# '5 B, 7 C => 1 BC',
# '4 C, 1 A => 1 CA',
# '2 AB, 3 BC, 4 CA => 1 FUEL']

# lines = ['157 ORE => 5 NZVS',
# '165 ORE => 6 DCFZ',
# '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
# '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
# '179 ORE => 7 PSHF',
# '177 ORE => 5 HKGWZ',
# '7 DCFZ, 7 PSHF => 2 XJWVT',
# '165 ORE => 2 GPVTF',
# '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']

# lines = ['2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
# '17 NVRVD, 3 JNWZP => 8 VPVL',
# '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
# '22 VJHF, 37 MNCFX => 5 FWMGM',
# '139 ORE => 4 NVRVD',
# '144 ORE => 7 JNWZP',
# '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
# '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
# '145 ORE => 6 MNCFX',
# '1 NVRVD => 8 CXFTF',
# '1 VJHF, 6 MNCFX => 4 RFSQX',
# '176 ORE => 6 VJHF']

# lines = ['171 ORE => 8 CNZTR',
# '7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL',
# '114 ORE => 4 BHXH',
# '14 VRPVC => 6 BMBT',
# '6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL',
# '6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT',
# '15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW',
# '13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW',
# '5 BMBT => 4 WPTQ',
# '189 ORE => 9 KTJDG',
# '1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP',
# '12 VRPVC, 27 CNZTR => 2 XDBXC',
# '15 KTJDG, 12 BHXH => 5 XCVML',
# '3 BHXH, 2 VRPVC => 7 MZWV',
# '121 ORE => 7 VRPVC',
# '7 XCVML => 6 RJRHP',
# '5 BHXH, 4 VRPVC => 5 LTCX']

quantity={}
recipe={}
for line in lines:
    quantity[(line.strip().split(' => ')[1].split()[1])] = int(line.strip().split(' => ')[1].split()[0])
    recipe[(line.strip().split(' => ')[1].split()[1])] = [[l.split()[1],int(l.split()[0])] for l in line.strip().split(' => ')[0].split(', ')]

#print(quantity)
#print(recipe)

name=[k for k in quantity.keys()]

def calculate_ore(o):
    inventory=[0 if k!='FUEL' else -o for k in quantity.keys()]
    ore=0
    i=0
    while True:
        if inventory[i]>=0: i+=1
        else:
            q=math.ceil(abs(inventory[i])/quantity[name[i]])
            inventory[i]+=q*quantity[name[i]]
            for ing in recipe[name[i]]:
                if ing[0]=='ORE': ore+=q*ing[1]
                else: inventory[name.index(ing[0])]-=q*ing[1]
            i=0
        if i==len(inventory):break
    return(ore)

print("ORE :",calculate_ore(1))
#for i in range(len(inventory)): print(name[i]," :",inventory[i])

# #first guess
# n=1000000000000//ore

# while ore<=1000000000000:
#     n+=1
#     inventory=[0 if k!='FUEL' else -n for k in quantity.keys()]
#     ore=0
#     i=0
#     while True:
#         if inventory[i]>=0: i+=1
#         else:
#             q=math.ceil(abs(inventory[i])/quantity[name[i]])
#             inventory[i]+=q*quantity[name[i]]
#             for ing in recipe[name[i]]:
#                 if ing[0]=='ORE': ore+=q*ing[1]
#                 else: inventory[name.index(ing[0])]-=q*ing[1]
#             i=0
#         if i==len(inventory):break

# print(n-1)

print(int(int(1000000000000/calculate_ore(1))*(1000000000000 / calculate_ore(int(1000000000000 / calculate_ore(1))))))

# MINUS 1 !!!!!!!!!!!!
