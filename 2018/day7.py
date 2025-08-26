# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 10:32:19 2025

@author: castelf
"""
import networkx as nx

#with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day7.txt','r') as f: lines=f.readlines()

lines=['Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.']

# Implement a directed graph
graph = nx.DiGraph()

# Construct the graph
data=[(line.split()[1],line.split()[7]) for line in lines]
graph.add_edges_from(data)
#nx.draw(graph, with_labels=True, font_weight='bold')

# The result
res=[]

# Start the loop
var=[]
for node in graph.nodes:
    if len(list(graph.predecessors(node)))==0: var.append(node)

#The loop
while len(var)>0:
    var.sort()
    e=var.pop(0)
    if e not in res: res.append(e)
    var_pos=list(graph.successors(e))
    for j in var_pos:
        if all(e in res for e in list(graph.predecessors(j))): var.append(j)

print(''.join(res))
