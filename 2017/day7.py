# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 13:52:35 2025

@author: castelf
"""
import re
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day7.txt','r') as f: lines=f.readlines()

nodes=[]
score=[]
fils=[]
for line in lines:
    ins=line.strip().split(' -> ')
    x=re.findall(r'(\w+) \((\d+)\)',ins[0])
    node,num=x[0]
    nodes.append(node)
    score.append(int(num))
    if len(ins)==2: fils.append(ins[1])
    else: fils.append('')
progs=''.join(fils)
nodes=np.array(nodes)

res1=''
for node in nodes:
    if node not in progs: res1+=node
print(res1)

# score_f=[]
# for f in fils[np.where(nodes==res1)[0][0]].split(', '):
#     sc=[]
#     for n in fils[np.where(nodes==f)[0][0]].split(', '): sc.append(score[np.where(nodes==n)[0][0]])
#     score_f.append(sc)
# print(score_f)
    
score_f=[]
for f in fils:
    n_sp=f.split(', ')
    sc=[]
    for n in n_sp: sc.append(score[np.where(nodes==n)[0][0]])
    score_f.append(sc)

res=[]
for i,s in enumerate(score_f):
    if all(x==s[0] for x in s): res.append(sum(s)+score[i])
    else: res.append(0)

s=score_f[0]
(score[0])
len(res)




import re, collections

with open("C:\\Users\castelf\Documents\GitHub\AoC\\2017\day7.txt") as fp:
    text = fp.read()

weight = {}
children = {}
for line in text.strip().splitlines():
    label, n, *xs = re.findall(r'\w+', line)
    weight[label] = int(n)
    children[label] = tuple(xs)

root, = set(weight) - {c for cs in children.values() for c in cs}

def total_weight(label):
    sub = [total_weight(c) for c in children[label]]
    if len(set(sub)) > 1:
        (target, _), (failure, _) = collections.Counter(sub).most_common()
        print(target - failure + weight[children[label][sub.index(failure)]])
        return weight[label] + sum(sub)
    return weight[label] + sum(sub)

print(total_weight(root))


import networkx as nx

graph = nx.DiGraph()

# Build the graph of programs
for line in lines:
    name = line.split()[0]

    graph.add_node(name, weight=int(line.split()[1].strip('()')))

    if '->' in line:
        children = [n.strip() for n in line.split('->')[1].split(',')]

        for child in children:
            graph.add_edge(name, child)

# Topological sort to find the root of the tree
ordered = list(nx.topological_sort(graph))

print('PART 1:', ordered[0])

# Keep track of each node's total weight (itself + its children)
weights = {}

# Going backwards (starting from the leaves)
for node in reversed(ordered):
    # Start with this nodes own weight
    total = graph.nodes[node]['weight']

    counts = collections.Counter(weights[child] for child in graph[node])
    unbalanced = None

    for child in graph[node]:
        # If this child's weight is different than others, we've found it
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        diff = weights[unbalanced] - val
        print('PART 2:', graph.nodes[unbalanced]['weight'] - diff)
        break

    # Store the total weight of the node
    weights[node] = total






















