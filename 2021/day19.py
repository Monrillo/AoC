# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 09:41:15 2026

@author: castelf
"""
import re
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day19.txt','r') as f: lines=f.readlines()

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day19test.txt','r') as f: lines=f.readlines()

lines=['--- scanner 0 ---',
'0,2',
'4,1',
'3,3',
'',
'--- scanner 1 ---',
'-1,-1',
'-5,0',
'-2,1']

scanner={}
for line in lines:
    if line.startswith('---'):
        scan=int(re.findall(r'\d+', line.strip('\n'))[0])
        scanner[scan]=[]
    elif line.strip('\n')=='':
        scanner[scan]=np.array(scanner[scan])
    else:
        scanner[scan].append([int(x) for x in re.findall(r'-?\d+', line.strip('\n'))])
scanner[scan]=np.array(scanner[scan])

position=[]
for s in range(1,5):
    res=[]
    for i in range(-1500,1500):
        for c in range(3):
            if sum(1 for x in scanner[s-1][:,c]+i if x in scanner[s][:,c])>10:
                res.append(-i)
                break
            elif sum(1 for x in scanner[s-1][:,c]*-1+i if x in scanner[s][:,c])>10:
                res.append(i)
                break
    position.append(res)
        



sum(1 for x in scanner[0][:,1]*-1-1246 if x in scanner[1][:,1])

lines=['-618,-824,-621',
'-537,-823,-458',
'-447,-329,318',
'404,-588,-901',
'544,-627,-890',
'528,-643,409',
'-661,-816,-575',
'390,-675,-793',
'423,-701,434',
'-345,-311,381',
'459,-707,401',
'-485,-357,347']

test1=np.array([[int(x) for x in line.split(',')] for line in lines])

lines=['686,422,578',
'605,423,415',
'515,917,-361',
'-336,658,858',
'-476,619,847',
'-460,603,-452',
'729,430,532',
'-322,571,750',
'-355,545,-477',
'413,935,-424',
'-391,539,-444',
'553,889,-390']

test2=np.array([[int(x) for x in line.split(',')] for line in lines])

sum(test1[:,0]*-1+68==test2[:,0])

sum(scanner[0][:,0]*-1+68==scanner[1][:,0])

sum(1 for x in scanner[0][:,0]*-1+68 if x in scanner[1][:,0])

scanner[0].sort()


sum(set(scanner[0][:,0]*-1+68)==set(scanner[1][:,0]))

Counter(scanner[0][:,0]) == Counter(scanner[1][:,0])

scanner[0].sort()

np.array_equal(test[:,0], scanner[1][:,0])

from collections import Counter
test[:,0]==scanner[1][:,0]
Counter(test[:,0]) == Counter(scanner[1][:,0])








