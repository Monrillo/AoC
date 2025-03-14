# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:38:28 2025

@author: castelf
"""

inst=[line.strip().split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day18.txt','r').readlines()]

# Part 1

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

# Part 2

reg1={'p': 0}
reg2={'p': 1}
cpt1=0
cpt2=0
sen1=[]
sen2=[]
res=0
one=True
two=False
while True:
    ins1=inst[cpt1]
    ins2=inst[cpt2]
    if one:
        try: int(ins1[1])
        except:
            try: reg1[ins1[1]]
            except: reg1[ins1[1]]=0 
    if one and ins1[0]=='set':
        try: reg1[ins1[1]]=int(ins1[2])
        except: reg1[ins1[1]]=reg1[ins1[2]]
    elif one and ins1[0]=='add':
        try: reg1[ins1[1]]+=int(ins1[2])
        except: reg1[ins1[1]]+=reg1[ins1[2]]
    elif one and ins1[0]=='mul':
        try: reg1[ins1[1]]*=int(ins1[2])
        except: reg1[ins1[1]]*=reg1[ins1[2]]
    elif one and ins1[0]=='mod':
        try: reg1[ins1[1]]=reg1[ins1[1]]%int(ins1[2])
        except: reg1[ins1[1]]=reg1[ins1[1]]%reg1[ins1[2]]
    elif one and ins1[0]=='snd':
        sen1.append(reg1[ins1[1]])
    elif one and ins1[0]=='rcv':
        try: reg1[ins1[1]]=sen2.pop(0)
        except:
            if len(sen1)>0:one=False;two=True;continue
            else:break
    elif one and ins1[0]=='jgz':
        try: val1=int(ins1[1])
        except: val1=reg1[ins1[1]]
        if val1>0:
            try: cpt1+=int(ins1[2])-1
            except: cpt1+=reg1[ins1[2]]-1
    if one: cpt1+=1

    if two:    
        try: int(ins2[1])
        except:
            try: reg2[ins2[1]]
            except: reg2[ins2[1]]=0    
    if two and ins2[0]=='set':
        try: reg2[ins2[1]]=int(ins2[2])
        except: reg2[ins2[1]]=reg2[ins2[2]]
    elif two and ins2[0]=='add':
        try: reg2[ins2[1]]+=int(ins2[2])
        except: reg2[ins2[1]]+=reg2[ins2[2]]
    elif two and ins2[0]=='mul':
        try: reg2[ins2[1]]*=int(ins2[2])
        except: reg2[ins2[1]]*=reg2[ins2[2]]
    elif two and ins2[0]=='mod':
        try: reg2[ins2[1]]=reg2[ins2[1]]%int(ins2[2])
        except: reg2[ins2[1]]=reg2[ins2[1]]%reg2[ins2[2]]
    elif two and ins2[0]=='snd':
        sen2.append(reg2[ins2[1]]);res+=1
    elif two and ins2[0]=='rcv':
        try: reg2[ins2[1]]=sen1.pop(0)
        except:
            if len(sen2)>0:one=True;two=False;continue
            else:break
    elif two and ins2[0]=='jgz':
        try: val2=int(ins2[1])
        except: val2=reg2[ins2[1]]
        if val2>0:
            try: cpt2+=int(ins2[2])-1
            except: cpt2+=reg2[ins2[2]]-1
    if two: cpt2+=1

print(res)

