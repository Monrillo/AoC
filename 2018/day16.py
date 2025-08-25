# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:23:31 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day16.txt','r') as f: lines=f.readlines()

# Before: [3, 2, 1, 1]
# 9 2 1 2
# After:  [3, 2, 2, 1]

# reg_in=[3, 2, 1, 1]
# calcul=['9', '2', '1', '2']
# reg_out=[3, 2, 2, 1]

def addr(reg,a,b,c):reg[c]=reg[a]+reg[b]
def addi(reg,a,b,c):reg[c]=reg[a]+b
def mulr(reg,a,b,c):reg[c]=reg[a]*reg[b]
def muli(reg,a,b,c):reg[c]=reg[a]*b
def banr(reg,a,b,c):reg[c]=reg[a]&reg[b]
def bani(reg,a,b,c):reg[c]=reg[a]&b
def borr(reg,a,b,c):reg[c]=reg[a]|reg[b]
def bori(reg,a,b,c):reg[c]=reg[a]|b
def setr(reg,a,b,c):reg[c]=reg[a]
def seti(reg,a,b,c):reg[c]=a
def gtir(reg,a,b,c):
    if a>reg[b]:reg[c]=1
    else: reg[c]=0
def gtri(reg,a,b,c):
    if reg[a]>b:reg[c]=1
    else: reg[c]=0
def gtrr(reg,a,b,c):
    if reg[a]>reg[b]:reg[c]=1
    else: reg[c]=0
def eqir(reg,a,b,c):
    if a==reg[b]:reg[c]=1
    else: reg[c]=0
def eqri(reg,a,b,c):
    if reg[a]==b:reg[c]=1
    else: reg[c]=0
def eqrr(reg,a,b,c):
    if reg[a]==reg[b]:reg[c]=1
    else: reg[c]=0

fonctions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

reg_func={}
for i in range(16):
    reg_func[str(i)]=fonctions

def test_func(reg_input,calc,reg_output,pool_f):
    good_fonctions=[]
    for func in pool_f:
        reg=reg_input.copy()
        func(reg,int(calc[1]),int(calc[2]),int(calc[3]))
        if reg==reg_output:good_fonctions.append(func)
    return good_fonctions

res_1=0
for i in range(len(lines)-2):
    a=lines[i]
    b=lines[i+1]
    c=lines[i+2]
    if a.startswith('Before'):
        reg_in=eval(a.strip()[7:])
        calcul=b.strip().split(' ')
        reg_out=eval(c.strip()[7:])
        if len(test_func(reg_in,calcul,reg_out,fonctions))>=3:res_1+=1
        reg_func[calcul[0]]=test_func(reg_in,calcul,reg_out,reg_func[calcul[0]])
    if len(a.strip())==len(b.strip())==len(c.strip())==0:program=i+3

print(res_1)

while any(len(reg_func[k])>1 for k in reg_func.keys()):
    for k in reg_func.keys():
        if len(reg_func[k])==1:
            f=reg_func[k][0]
            for k2 in reg_func.keys():
                if k2!=k and f in reg_func[k2]:reg_func[k2].remove(f)

reg=[0,0,0,0]
for i in range(program,len(lines)):
    calcul=lines[i].strip().split(' ')
    reg_func[calcul[0]][0](reg,int(calcul[1]),int(calcul[2]),int(calcul[3]))

print(reg[0])