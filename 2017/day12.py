# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 15:08:50 2025

@author: castelf
"""

import networkx as nx

lines=open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day12.txt','r').readlines()

# lines=['0 <-> 2',
# '1 <-> 1',
# '2 <-> 0, 3, 4',
# '3 <-> 2, 4',
# '4 <-> 2, 3, 6',
# '5 <-> 6',
# '6 <-> 4, 5']

g=nx.Graph()
for line in lines:
    val=line.split(' <-> ')
    g.add_node(int(val[0]))
    for i in val[1].split(', '): g.add_edge(int(val[0]),int(i))

print(len(nx.node_connected_component(g,0)))
print(nx.number_connected_components(g))
