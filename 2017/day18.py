# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:38:28 2025

@author: castelf
"""

inst=[line.strip().split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day18.txt','r').readlines()]
reg={}
sound=0
recover=0
cpt=0
while recover==0:
    ins=inst[cpt]
    try: int(ins[1])
    except:
        try: reg[ins[1]]
        except: reg[ins[1]]=0    
    if ins[0]=='set':
        try: reg[ins[1]]=int(ins[2])
        except: reg[ins[1]]=reg[ins[2]]
    elif ins[0]=='add':
        try: reg[ins[1]]+=int(ins[2])
        except: reg[ins[1]]+=reg[ins[2]]
    elif ins[0]=='mul':
        try: reg[ins[1]]*=int(ins[2])
        except: reg[ins[1]]*=reg[ins[2]]
    elif ins[0]=='mod':
        try: reg[ins[1]]=reg[ins[1]]%int(ins[2])
        except: reg[ins[1]]=reg[ins[1]]%reg[ins[2]]
    elif ins[0]=='snd':
        sound=reg[ins[1]]
    elif ins[0]=='rcv':
        recover=sound
    elif ins[0]=='jgz':
        try: val=int(ins[1])
        except: val=reg[ins[1]]
        if val>0:
            try: cpt+=int(ins[2]);continue
            except: cpt+=reg[ins[2]];continue
    cpt+=1

print(recover)

