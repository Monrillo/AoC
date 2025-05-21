# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 14:38:00 2025

@author: castelf
"""

import numpy as np
import re

lines=['[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up']

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day4.txt','r') as f: lines=f.readlines()

guard_table=[]
guard_list={}

for line in lines:
    y,mo,d,h,mi=re.findall(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)[0]
    if h=='23': d=int(d)+1
    if re.search(r'Guard', line):
        guard=int(re.search('\#(\d+)', line).group()[1:])
        guard_list[guard]=0
        guard_table.append([guard,int(mo),int(d),set()])

guard_table=np.array(guard_table)

for line in lines:
    y,mo,d,h,mi=re.findall(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)[0]
    if not re.search(r'Guard', line):
        if any(np.logical_and(guard_table[:,1]==int(mo),guard_table[:,2]==int(d))):
            guard_table[np.logical_and(guard_table[:,1]==int(mo),guard_table[:,2]==int(d))][:,3][0].add(int(mi))

for g in list(guard_list):
    for ronde in guard_table[(guard_table[:,0]==g)]:
        for a,b in zip(sorted(ronde[3])[::2],sorted(ronde[3])[1::2]):
            guard_list[g]+=b-a    
guard=max(guard_list, key=guard_list.get)

sleep=np.zeros(60)
for minute in range(60):
    s=0
    for ronde in guard_table[(guard_table[:,0]==guard)]:
            for a,b in zip(sorted(ronde[3])[::2],sorted(ronde[3])[1::2]):
                if a<=minute<b:s+=1
    sleep[minute]=s
minute=np.argmax(sleep)

# Strategy 1
print(guard*minute)

sleep=np.zeros(60)
for minute in range(60):
    s=0
    for ronde in guard_table:
            for a,b in zip(sorted(ronde[3])[::2],sorted(ronde[3])[1::2]):
                if a<=minute<b:s+=1
    sleep[minute]=s
minute=np.argmax(sleep)

for g in list(guard_list):
    m=0
    for ronde in guard_table[(guard_table[:,0]==g)]:
        for a,b in zip(sorted(ronde[3])[::2],sorted(ronde[3])[1::2]):
            if a<=minute<b:m+=1   
    guard_list[g]=m
guard=max(guard_list, key=guard_list.get)

# Strategy 2
print(guard*minute)


inp=open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day4.txt','r').read()

import collections
import dateutil

guards = collections.defaultdict(list)
times = collections.defaultdict(int)

for line in sorted(inp.splitlines()):
    time, action = line.split('] ')

    time = dateutil.parser.parse(time[1:])

    if action.startswith('Guard'):
        guard = int(action.split()[1][1:])
    elif action == 'falls asleep':
        start = time
    elif action == 'wakes up':
        end = time
        guards[guard].append((start.minute, end.minute))
        times[guard] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60)], key=lambda i: i[1])

print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('part 2:', guard * minute)