# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:38:37 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day9.txt','r') as f: disk=f.read()

#disk='2333133121414131402'

quantity=[]
values=[]
num=0
for i,d in enumerate(disk):
    quantity.append(int(d))
    if i%2==0:values.append(num)
    else:values.append(None);num+=1

cur=0
while cur<=len(values):
    while values[-1] is None: values.pop(-1);quantity.pop(-1)
    if cur>=len(values):break
    while quantity[cur]==0: values.pop(cur);quantity.pop(cur);cur-=1
    if values[cur] is None:
        if quantity[cur]>=quantity[-1]:
            val=values.pop(-1)
            qu=quantity.pop(-1)
            values.insert(cur,val)
            quantity.insert(cur,qu)
            quantity[cur+1]-=qu
        else :
            quantity[-1]-=quantity[cur]
            values[cur]=values[-1]
    cur+=1

checksum=0
position=0
while quantity:
    qu=quantity.pop(0)
    val=values.pop(0)
    for i in range(qu):
        checksum+=position*val
        position+=1

print("Part 1:",checksum)

quantity=[]
values=[]
num=0
for i,d in enumerate(disk):
    quantity.append(int(d))
    if i%2==0:values.append(num)
    else:values.append(None);num+=1

cur=0
while None in values:
    while values[-1] is None: values.pop(-1);quantity.pop(-1)
    if cur>=len(values):break
    while quantity[cur]==0: values.pop(cur);quantity.pop(cur);cur-=1
    if values[cur] is None:
        found=False
        for i in range(len(quantity)-1,cur,-1):
            if quantity[cur]>=quantity[i]:
                val=values.pop(i)
                qu=quantity.pop(i)
                values.insert(cur,val)
                quantity.insert(cur,qu)
                quantity[cur+1]-=qu
                cur-=1
                found=True
                break
        if not found :
            quantity[-1]-=quantity[cur]
            values[cur]=values[-1]
            cur-=1
    cur+=1

checksum=0
position=0
while quantity:
    qu=quantity.pop(0)
    val=values.pop(0)
    for i in range(qu):
        checksum+=position*val
        position+=1

print("Part 2:",checksum)





