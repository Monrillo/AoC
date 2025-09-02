# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 14:45:34 2025

@author: castelf
"""

import networkx as nx

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day6.txt','r') as f: lines=f.readlines()

# lines=['COM)B',
# 'B)C',
# 'C)D',
# 'D)E',
# 'E)F',
# 'B)G',
# 'G)H',
# 'D)I',
# 'E)J',
# 'J)K',
# 'K)L']

# lines=['COM)B',
# 'B)C',
# 'C)D',
# 'D)E',
# 'E)F',
# 'B)G',
# 'G)H',
# 'D)I',
# 'E)J',
# 'J)K',
# 'K)L',
# 'K)YOU',
# 'I)SAN']

# Implement a directed graph
graph = nx.DiGraph()

# Construct the graph
data=[(line.strip().split(')')[0],line.strip().split(')')[1]) for line in lines]
graph.add_edges_from(data)

#nx.draw(graph, with_labels=True, font_weight='bold')

total=0
for node in graph.nodes:
    ancestors = nx.ancestors(graph, node)
    total+=len(ancestors)
print(total)

graph2 = nx.Graph()

# Construct the undirected graph
graph2.add_edges_from(data)

# -1 because we want the number od edges and not the number of nodes
# -2 bacause we want YOU to robit with SAN
print(len(nx.shortest_path(graph2, 'YOU', 'SAN'))-3)