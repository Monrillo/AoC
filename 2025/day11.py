# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:25:51 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day11.txt','r') as f: lines=f.readlines()

lines=['aaa: you hhh',
'you: bbb ccc',
'bbb: ddd eee',
'ccc: ddd eee fff',
'ddd: ggg',
'eee: out',
'fff: out',
'ggg: out',
'hhh: ccc fff iii',
'iii: out']

links={}
for line in lines:
    links[line.strip().split(': ')[0]]=line.strip().split(': ')[1].split(' ')

path=0
while len(links['you'])>0:
    l=links['you'].pop(0)
    if l=='out': path+=1
    else: links['you'].extend(links[l])
            
print("Part 1:",path)

lines=['svr: aaa bbb',
'aaa: fft',
'fft: ccc',
'bbb: tty',
'tty: ccc',
'ccc: ddd eee',
'ddd: hub',
'hub: fff',
'eee: dac',
'dac: fff',
'fff: ggg hhh',
'ggg: out',
'hhh: out']

links={}
for line in lines:
    links[line.strip().split(': ')[0]]=line.strip().split(': ')[1].split(' ')


from collections import deque

arrival=[]

# First paths beginning from dac passing through fft

path=deque([[s] for s in links['dac']])
while path:
    p=path.popleft()
    if p[-1]=='out':
        if 'fft' in p: arrival.append(p)
    else:
        for w in links[p[-1]]: path.appendleft(p+[w])

# Then paths beginning from fft passing through dac

path=deque([[s] for s in links['fft']])
while path:
    p=path.popleft()
    if p[-1]=='out':
        if 'dac' in p: arrival.append(p)
    else:
        for w in links[p[-1]]: path.appendleft(p+[w])



path=deque([[s] for s in links['svr']])
arrival=0

while path:
    p=path.popleft()
    if p[-1]=='out':
        if ('dac' in p and 'fft' in p):arrival+=1
    else:
        for w in links[p[-1]]: path.appendleft(p+[w])

print("Part 2:",arrival)


len(path)
len(arrival)
