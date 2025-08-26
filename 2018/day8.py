# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 14:14:20 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day8.txt','r') as f: data=[int(x) for x in f.read().split()]

#data=[2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]

# Solution Part1 without Recursion
#
# metadata=0

# while len(data)>0:
#     pos=data.index(0)
#     for _ in range(data[pos+1]):
#         metadata+=data.pop(pos+2)
#     data.pop(pos+1)
#     data.pop(pos)
#     if pos>0:data[pos-2]-=1

# print("Part 1 :",metadata)


# Solution with input from Internet solution, with Recursion !

def meta(d):
    node=d.pop(0)
    entries=d.pop(0)
    chnodes=[meta(d) for _ in range(node)]
    metadata=[d.pop(0) for _ in range(entries)]
    return sum(chnodes) + sum(metadata)

def node_val(d):
    node=d.pop(0)
    entries=d.pop(0)
    chnodes=[node_val(d) for _ in range(node)]
    metadata=[d.pop(0) for _ in range(entries)]
    if node==0: return sum(metadata)
    else: return sum([chnodes[m-1] if m-1<len(chnodes) else 0 for m in metadata])

data1=data.copy()
print(meta(data1))

data2=data.copy()
print(node_val(data2))