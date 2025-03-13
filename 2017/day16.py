# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 16:03:55 2025

@author: castelf
"""

import re
import time
from collections import deque

inst = open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day16.txt','r').read().split(',')

prog=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

start=time.time()

res=deque([])
while True:
    for i in inst:
        if i[0]=='s': prog=prog[-int(i[1:]):]+prog[:-int(i[1:])]
        elif i[0]=='x': a,b=re.findall('(\d+)/(\d+)', i[1:])[0];prog[int(a)],prog[int(b)]=prog[int(b)],prog[int(a)]
        elif i[0]=='p': a,b=re.findall('(\w)/(\w)', i[1:])[0];a=prog.index(a);b=prog.index(b);\
            prog[a],prog[b]=prog[b],prog[a]
    if ''.join(prog) in res: break
    res.append(''.join(prog))
    
end=time.time()
print(end-start)

print(res[0])
print(res[1000000000%len(res)-1])



