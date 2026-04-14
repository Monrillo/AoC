# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:42:36 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day15.txt','r') as f: line=f.read()

#line='rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

def hash_script(n,st):
    if len(st)==0: return n
    else:
        return(hash_script(((n+ord(st[0]))*17)%256,st[1:]))

print("Part 1:",sum(hash_script(0, l) for l in line.split(',')))

boxes={}

for l in line.split(','):
    if l.endswith('-'):
        lens=l[:-1]
        k=hash_script(0, lens)
        if k not in boxes.keys():
            pass
        else:
            if any(b[0]==lens for b in boxes[k]):
                for i,b in enumerate(boxes[k]):
                    if b[0]==lens:
                        boxes[k].pop(i)
    else:
        lens,focal=l.split('=')
        k=hash_script(0, lens)
        if k not in boxes.keys():
            boxes[k]=[]
            boxes[k].append([lens,int(focal)])
        else:
            if any(b[0]==lens for b in boxes[k]):
                for b in boxes[k]:
                    if b[0]==lens: b[1]=int(focal)
            else:
                boxes[k].append([lens,int(focal)])
            
focusing=0
for k in boxes.keys():
    for i,b in enumerate(boxes[k]):
        focusing+=(k+1)*(i+1)*b[1]
        
print("Part 2:",focusing)

