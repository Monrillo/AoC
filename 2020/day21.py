# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 09:20:18 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day21.txt','r') as f: lines=f.readlines()

# lines=['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
# 'trh fvjkl sbzzf mxmxvkd (contains dairy)',
# 'sqjhc fvjkl (contains soy)',
# 'sqjhc mxmxvkd sbzzf (contains fish)']

recipe=[]
for line in lines:
    food=line.strip().split()
    sep=food.index('(contains')
    recipe.append([food[:sep],[x[:-1] for x in food[sep+1:]]])

ingredients=[]
allergens={}

for r in recipe:
    for a in r[1]:
        if a not in allergens.keys(): allergens[a]=[]
        allergens[a].append(r[0])
    for x in r[0]:
        if x not in ingredients: ingredients.append(x)

for a in allergens:
    allergens[a]=[i for i in allergens[a][0] if all(i in allergens[a][j] for j in range(len(allergens[a])))]

while any(len(allergens[a])>1 for a in allergens):
    for a in allergens:
        if len(allergens[a])==1:
            k=allergens[a][0]
            for b in allergens:
                if b!=a and k in allergens[b]:allergens[b].remove(k)
            
good_ingredients=ingredients.copy()
for a in allergens: good_ingredients.remove(allergens[a][0])

print("Part 1:", sum(g in r[0] for g in good_ingredients for r in recipe))

print("Part 2:", ''.join([allergens[a][0]+',' for a in sorted(list(allergens.keys()))])[:-1])
