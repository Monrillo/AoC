# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:38:12 2025

@author: castelf
"""

data=[]
for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day20.txt'):
    a,b=line.strip().split('-')
    data.append([int(a),int(b)])
data=sorted(data)

def test_ip(ip):
    for i in range(len(data)):
        if data[i][0]<=ip<=data[i][1]: return False;break
    return True

candidates=[d[1]+1 for d in data]

valids=[x for x in candidates if test_ip(x) and x<=4294967295]

print(valids[0])
print(len(valids))
