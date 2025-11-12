# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:11:55 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day16.txt','r') as f: lines=f.readlines()

# lines=['class: 1-3 or 5-7',
# 'row: 6-11 or 33-44',
# 'seat: 13-40 or 45-50',
# '',
# 'your ticket:',
# '7,1,14',
# '',
# 'nearby tickets:',
# '7,3,47',
# '40,4,50',
# '55,2,20',
# '38,6,12']

# lines=['class: 0-1 or 4-19',
# 'row: 0-5 or 8-19',
# 'seat: 0-13 or 16-19',
# '',
# 'your ticket:',
# '11,12,13',
# '',
# 'nearby tickets:',
# '3,9,18',
# '15,1,5',
# '5,14,9']

carac={}
tickets=[]
car=True
my_tick=False
other_tick=False

# Initialisation from data
for l in lines:
    if l.strip()=='': car=False; my_tick=False
    elif l.strip()=='your ticket:': my_tick=True
    elif l.strip()=='nearby tickets:': other_tick=True
    else:
        if car: carac[l.strip().split(': ')[0]]=[int(x) for x in re.findall('\d+', l.strip())]
        elif my_tick: my_ticket=[int(x) for x in re.findall('\d+', l.strip())]
        elif other_tick: tickets.append([int(x) for x in re.findall('\d+', l.strip())])

def scan(n):
    res=False
    for c in list(carac.values()):
        if c[0]<=n<=c[1] or c[2]<=n<=c[3]:res=True
    return res

# Part 1
invalid=[t for ti in tickets for t in ti if not scan(t)]
print("Part 1:",sum(invalid))

#Part 2
impossib_carac={x:[] for x in range(len(carac))}
valid_tick=[ti for ti in tickets if all(scan(t) for t in ti)]

for v in valid_tick:
    for i in range(len(v)):
        for c in carac:
            if not carac[c][0]<=v[i]<=carac[c][1] and not carac[c][2]<=v[i]<=carac[c][3]:impossib_carac[i].append(c)
            
#valid_carac={x:[] for x in range(len(carac))}
valid_carac={}
len_impos=[len(impossib_carac[x]) for x in range(len(carac))]
pop_carac=list(carac.keys())
for i in range(len(carac)-1,-1,-1):
    r=[c for c in pop_carac if c not in impossib_carac[len_impos.index(i)]][0]
    c=pop_carac.pop(pop_carac.index(r))
    valid_carac[c]=len_impos.index(i)

resultat=1
for v in valid_carac:
    if v.split(' ')[0]=='departure':resultat*=my_ticket[valid_carac[v]]
print("Part 2:",resultat)