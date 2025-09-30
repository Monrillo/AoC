# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 10:50:11 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day10.txt','r') as f: lines=f.readlines()

# lines=['16',
# '10',
# '15',
# '5',
# '1',
# '11',
# '7',
# '19',
# '6',
# '12',
# '4']

# lines=['28',
# '33',
# '18',
# '42',
# '31',
# '14',
# '46',
# '20',
# '48',
# '47',
# '24',
# '23',
# '49',
# '45',
# '19',
# '38',
# '39',
# '11',
# '1',
# '32',
# '25',
# '35',
# '8',
# '17',
# '7',
# '9',
# '4',
# '2',
# '34',
# '10',
# '3']

jolts=np.array(sorted([int(l.strip()) for l in lines]))
jolts=np.append(0,jolts)
jolts=np.append(jolts,jolts[-1]+3)
num,counts=np.unique(np.diff(jolts), return_counts=True)
print("Part 1:",counts[0]*counts[1])

# Graph
graph={}
for x in jolts:
    graph[x]=set([i for i in range(x+1,x+4) if i in jolts])

# Depth first counter (DFS)
def dfc(G,v,M={}):
    if v in M: return M[v]
    elif G[v]: M[v]=sum(dfc(G,x,M) for x in G[v]);return M[v]
    else: return 1

print("Part 2:",dfc(graph,0))

