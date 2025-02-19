# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:59:16 2025

@author: castelf
"""

ins=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day23.txt','r')]

# lines=['cpy b c',
# 'inc a',
# 'dec c',
# 'jnz c -2',
# 'dec d',
# 'jnz d -5']

# ins=[line.split() for line in lines]


def toggle(i):
    ins_tgl=ins[reg[i]+cpt]
    if ins_tgl[0]=='inc': ins[reg[i]+cpt][0]='dec'
    elif ins_tgl[0]=='dec' or ins_tgl[0]=='tgl': ins[reg[i]+cpt][0]='inc'
    elif ins_tgl[0]=='jnz': ins[reg[i]+cpt][0]='cpy'
    elif ins_tgl[0]=='cpy': ins[reg[i]+cpt][0]='jnz'
    
    
#Part 1
#reg={'a':7,'b':0,'c':0,'d':0}
#Part 2
reg={'a':12,'b':0,'c':0,'d':0}
cpt=0
while cpt<len(ins):
    # The multiply loop avoid !
    # cpy b c
    # inc a
    # dec c
    # jnz c -2
    # dec d
    # jnz d -5
    if cpt==4: reg['a']=reg['b']*reg['d'];reg['c']=0;reg['d'];cpt=10;continue
    l=ins[cpt]
    if l[0]=='inc': reg[l[1]]+=1
    elif l[0]=='tgl':
        if reg[l[1]]+cpt<len(ins): toggle(l[1])
        else: pass
    elif l[0]=='dec': reg[l[1]]-=1
    elif l[0]=='cpy':
        try:
            try: reg[l[2]]=int(l[1])
            except: reg[l[2]]=reg[l[1]]
        except: pass
    elif l[0]=='jnz':
        try:
            if int(l[1])!=0:
                try: cpt+=int(l[2]);continue
                except: cpt+=reg[l[2]];continue
        except:
            if reg[l[1]]!=0:
                try: cpt+=int(l[2]);continue
                except: cpt+=reg[l[2]];continue
    cpt+=1
print(reg['a'])

