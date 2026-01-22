# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 14:07:23 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day12.txt','r') as f: lines=f.readlines()

# lines=['start-A',
# 'start-b',
# 'A-c',
# 'A-b',
# 'b-d',
# 'A-end',
# 'b-end']

# lines=['dc-end',
# 'HN-start',
# 'start-kj',
# 'dc-start',
# 'dc-HN',
# 'LN-dc',
# 'HN-end',
# 'kj-sa',
# 'kj-HN',
# 'kj-dc']

links=[l.strip('\n').split('-') for l in lines]

path=[['start']]
good_path=[]

while len(path)>0:
    p=path.pop(0)
    if p[-1]=='end':good_path.append(p)
    else:
        for l in links:
            if p[-1]==l[0] and not (l[1][0] in 'abcdefghijklmnopqrstuvwxyz' and l[1] in p):path.append(p+[l[1]])
            elif p[-1]==l[1] and not (l[0][0] in 'abcdefghijklmnopqrstuvwxyz' and l[0] in p):path.append(p+[l[0]])
    
print("Part 1:",len(good_path))

path=[['start']]
good_path=[]

while len(path)>0:
    p=path.pop(0)
    if p[-1]=='end':good_path.append(p)
    else:
        for l in links:
            if p[-1]==l[0] and l[1]!='start' and not (l[1][0] in 'abcdefghijklmnopqrstuvwxyz' and l[1] in p and any(p.count(x)>1 for x in p if x[0] in 'abcdefghijklmnopqrstuvwxyz')):path.append(p+[l[1]])
            elif p[-1]==l[1] and l[0]!='start' and not (l[0][0] in 'abcdefghijklmnopqrstuvwxyz' and l[0] in p and any(p.count(x)>1 for x in p if x[0] in 'abcdefghijklmnopqrstuvwxyz')):path.append(p+[l[0]])
    
print("Part 2:",len(good_path))


