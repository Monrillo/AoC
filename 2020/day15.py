# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:57:25 2025

@author: castelf
"""

from collections import deque

num=deque([0,13,1,16,6,17])
num.reverse()
speak=set(list(num)[1:])

for i in range(len(num),30000000):
    if num[0] in speak:
        num.appendleft(num.index(num[0],1))
    else:
        speak.add(num[0])
        num.appendleft(0)
        

print(num[0])

# It works this the solution below ...

numbers = [0,13,1,16,6,17]
turn = 1
ult = {}
penul = {}

# seed the tables
for i in range(len(numbers)):
    ult[numbers[i]] = turn
    penul[numbers[i]] = 0
    turn += 1
    
target = numbers[-1]
while turn <= 30000000:
    if penul[target] == 0: # first time spoken
        target = 0
        penul[target] = ult[target]
        ult[target] = turn
    else:
        num = ult[target] - penul[target]
        target = num
        if target not in ult.keys():
            penul[target] = 0
            ult[target] = turn
        else:
            penul[target] = ult[target]
            ult[target] = turn
    turn += 1
print(target)