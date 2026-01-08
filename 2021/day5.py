# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 10:30:12 2026

@author: castelf
"""
from collections import deque,Counter

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day5.txt','r') as f: lines=f.readlines()

# lines=['0,9 -> 5,9',
# '8,0 -> 0,8',
# '9,4 -> 3,4',
# '2,2 -> 2,1',
# '7,0 -> 7,4',
# '6,4 -> 2,0',
# '0,9 -> 2,9',
# '3,4 -> 1,4',
# '0,0 -> 8,8',
# '5,5 -> 8,2']

vents_1=deque([])
vents_2=deque([])

for line in lines:
    a,b=line.strip('\n').split(' -> ')
    a1,a2=a.split(',')
    b1,b2=b.split(',')
    #Considering only horizontal lines
    if a2==b2:
        for i in range(min(int(a1),int(b1)),max(int(a1),int(b1))+1):
            vents_1.append((i,int(a2)))
            vents_2.append((i,int(a2)))
    #Considering only vertical lines
    elif a1==b1:
        for i in range(min(int(a2),int(b2)),max(int(a2),int(b2))+1):
            vents_1.append((int(a1),i))
            vents_2.append((int(a1),i))
    #Considering only diagonal lines
    else:
        if (int(a1)==min(int(a1),int(b1)) and int(a2)==min(int(a2),int(b2))) or (int(b1)==min(int(a1),int(b1)) and int(b2)==min(int(a2),int(b2))):
            #print(line)
            for i in range(abs(int(a1)-int(b1))+1):
                #print((min(int(a1),int(b1))+i,min(int(a2),int(b2))+i))
                vents_2.append((min(int(a1),int(b1))+i,min(int(a2),int(b2))+i))
        else :
            for i in range(abs(int(a1)-int(b1))+1):
                vents_2.append((min(int(a1),int(b1))+i,max(int(a2),int(b2))-i))
        
        
print("Part 1:",sum(1 for x in Counter(vents_1).values() if x>1))
print("Part 2:",sum(1 for x in Counter(vents_2).values() if x>1))
