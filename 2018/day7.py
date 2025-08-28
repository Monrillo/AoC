# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 10:32:19 2025

@author: castelf
"""
import networkx as nx

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day7.txt','r') as f: lines=f.readlines()

# lines=['Step C must be finished before step A can begin.',
# 'Step C must be finished before step F can begin.',
# 'Step A must be finished before step B can begin.',
# 'Step A must be finished before step D can begin.',
# 'Step B must be finished before step E can begin.',
# 'Step D must be finished before step E can begin.',
# 'Step F must be finished before step E can begin.']

# Implement a directed graph
graph = nx.DiGraph()

# Construct the graph
data=[(line.split()[1],line.split()[7]) for line in lines]
graph.add_edges_from(data)
#nx.draw(graph, with_labels=True, font_weight='bold')

# The result
res=[]

# Start the loop
sec=0
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

#Workers
num_w=5
workers={p:[] for p in range(num_w)}

# The result
res=[]

# Start the loop
sec=0
var=[]
for node in graph.nodes:
    if len(list(graph.predecessors(node)))==0: var.append(node)
var.sort()
for p in range(num_w):
    if not workers[p] and len(var)>0:
        e=var.pop(0)
        workers[p]=[e,ord(e)-4]

# print("var :",var)
# print("res :",res)
# print(sec, workers)

#The loop
while any(workers[p] for p in range(num_w)):
    sec+=1
    var.sort()
    for p in range(num_w):
        if workers[p]:
            if workers[p][1]==0:
                sec-=1
                e=workers[p][0]
                workers[p]=[]
                res.append(e)
                var_pos=list(graph.successors(e))
                for j in var_pos:
                    if all(e in res for e in list(graph.predecessors(j))): var.append(j)
    for p in range(num_w):
        if not workers[p] and len(var)>0:
            e=var.pop(0)
            if e not in res: workers[p]=[e,ord(e)-64]
        elif workers[p]:
             workers[p][1]-=1
    #print("var :",var)
    #print("res :",res)
    #print(sec, workers)
    
print(sec+1)

#Solution

from collections import defaultdict, deque
# Edges
E = defaultdict(list)
# In-degree
D = defaultdict(int)
for line in lines:
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y] += 1

for k in E:
    E[k] = sorted(E[k])

# time
t = 0
# Events
EV = []
# Work queue
Q = []
def add_task(x):
    Q.append(x)
def start_work():
    global Q
    while len(EV) < 5 and Q:
        x = min(Q)
        Q = [y for y in Q if y!=x]
        print ('Starting {} at {}'.format(x, t))
        EV.append((t+61+ord(x)-ord('A'), x))

for k in E:
    if D[k] == 0:
        add_task(k)
start_work()

while EV or Q:
    t, x = min(EV)
    print (t,x)
    EV = [y for y in EV if y!=(t,x)]
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            add_task(y)
    start_work()

print (t)
