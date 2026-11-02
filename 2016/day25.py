# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:04:04 2026

@author: castelf
"""

ins=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day25.txt','r')]

def toggle(i):
    ins_tgl=ins[reg[i]+cpt]
    if ins_tgl[0]=='inc': ins[reg[i]+cpt][0]='dec'
    elif ins_tgl[0]=='dec' or ins_tgl[0]=='tgl': ins[reg[i]+cpt][0]='inc'
    elif ins_tgl[0]=='jnz': ins[reg[i]+cpt][0]='cpy'
    elif ins_tgl[0]=='cpy': ins[reg[i]+cpt][0]='jnz'

good_signal = [0, 1] * 10

num = 0
transmission = False

while not transmission:
    num += 1
    reg = {'a': num, 'b': 0, 'c': 0, 'd': 0}
    cpt = 0
    output = []
    
    while len(output) < 20:
        l = ins[cpt]
        if l[0] == 'inc': reg[l[1]]+=1
        if l[0] == 'out': output.append(reg[l[1]])
        elif l[0] == 'tgl':
            if reg[l[1]] + cpt<len(ins): toggle(l[1])
            else: pass
        elif l[0] == 'dec': reg[l[1]]-=1
        elif l[0] == 'cpy':
            try:
                try: reg[l[2]] = int(l[1])
                except: reg[l[2]] = reg[l[1]]
            except: pass
        elif l[0] == 'jnz':
            try:
                if int(l[1])!=0:
                    try: cpt+=int(l[2]);continue
                    except: cpt+=reg[l[2]];continue
            except:
                if reg[l[1]]!=0:
                    try: cpt+=int(l[2]);continue
                    except: cpt+=reg[l[2]];continue
        cpt+=1
        
    transmission = output == good_signal

print(num)
