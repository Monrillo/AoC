# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 15:12:39 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day7.txt','r') as f: lines=f.readlines()

# lines=['light red bags contain 1 bright white bag, 2 muted yellow bags.',
# 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
# 'bright white bags contain 1 shiny gold bag.',
# 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
# 'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
# 'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
# 'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
# 'faded blue bags contain no other bags.',
# 'dotted black bags contain no other bags.']

# lines=['shiny gold bags contain 2 dark red bags.',
# 'dark red bags contain 2 dark orange bags.',
# 'dark orange bags contain 2 dark yellow bags.',
# 'dark yellow bags contain 2 dark green bags.',
# 'dark green bags contain 2 dark blue bags.',
# 'dark blue bags contain 2 dark violet bags.',
# 'dark violet bags contain no other bags.']

# Initialisation of bags
bags={}
quantity={}
for line in lines:
    words=line.strip().split()
    if words[4]=='no':
        bags[words[0]+' '+words[1]]=[]
        quantity[words[0]+' '+words[1]]=[1]
    else:
        bags[words[0]+' '+words[1]]=[words[i+1]+' '+words[i+2] for i in range(4,len(words),4)]
        quantity[words[0]+' '+words[1]]=[int(words[i]) for i in range(4,len(words),4)]

# Loop
possible=['shiny gold']
res=[]
while len(possible)>0:
    b=possible.pop()
    for k in list(bags.keys()):
        if b in bags[k] and k not in res : possible.append(k);res.append(k)

print("Part 1:",len(res))

def numbag(n):
    if len(bags[n])>0: return sum([quantity[n][i]*numbag(bags[n][i]) for i in range(len(bags[n]))])+1 
    else: return quantity[n][0]

print("Part 2:",numbag('shiny gold')-1)

