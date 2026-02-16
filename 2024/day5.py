# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:21:15 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day5.txt','r') as f: lines=f.readlines()

updating=False
rules={}
updates=[]
for line in lines:
    if line.strip('\n')=='':updating=True
    else:
        if not updating:
            a,b=line.strip('\n').split('|')
            if int(b) in rules.keys():rules[int(b)].append(int(a))
            else:rules[int(b)]=[int(a)]
        else: updates.append([int(x) for x in line.strip('\n').split(',')])

def check(u):
    return any(any(x in rules[u[i]] for x in u[i+1:]) for i in range(len(u)))

good_updates=[]
incorrect_updates=[]
for upd in updates:
    if not check(upd):good_updates.append(upd)
    else: incorrect_updates.append(upd)

print("Part 1:",sum(good[len(good)//2] for good in good_updates))

for inc in incorrect_updates:
    while check(inc):
        for i in range(len(inc)):
            for j in range(i+1,len(inc)):
                if inc[j] in rules[inc[i]]:inc[i],inc[j]=inc[j],inc[i]
                break
                
print("Part 2:",sum(good[len(good)//2] for good in incorrect_updates))


