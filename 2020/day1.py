# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 09:38:32 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day1.txt','r') as f: lines=f.readlines()

data=[int(line.strip()) for line in lines]

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]+data[j]==2020:print("Part 1:",data[i]*data[j])
        
for i in range(len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            if (data[i]+data[j]+data[k]==2020):print("Part 2:",data[i]*data[j]*data[k])

