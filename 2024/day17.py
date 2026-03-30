# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:20:33 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day17.txt','r') as f: lines=f.readlines()

# lines=['Register A: 729',
# 'Register B: 0',
# 'Register C: 0',
# '',
# 'Program: 0,1,5,4,3,0']

reg={}
for line in lines:
    l=line.strip('\n')
    if l.startswith('Register'):
        k,num=l.strip('Register ').split(': ')
        reg[k]=int(num)
    elif l.startswith('Program'):
        program=[int(x) for x in l.split(': ')[1].split(',')]

def combo(n):
    if n<=3: return n
    elif n==4: return reg['A']
    elif n==5: return reg['B']
    elif n==6: return reg['C']
    else: return

def div(n):
    num=combo(n)
    return int(reg['A']/2**num)

def bxl(n):
    return reg['B'] ^ n

def bxc(n):
    return reg['B'] ^ reg['C']

def mod(n):
    num=combo(n)
    return num%8



def opcode(code,oper):
    global position
    global output
    global copy
    global exact_copy
    if code==0: reg['A']=div(oper); position+=2
    elif code==1: reg['B']=bxl(oper); position+=2
    elif code==2: reg['B']=mod(oper); position+=2
    elif code==3:
        if reg['A']==0: position+=2
        else: position=oper
    elif code==4: reg['B']=bxc(oper); position+=2
    elif code==5:
        output.append(mod(oper))
        copy=output==program[:len(output)]
        if copy and len(output)==len(program):exact_copy=True
        position+=2
    elif code==6: reg['B']=div(oper); position+=2
    elif code==7: reg['C']=div(oper); position+=2

position=0
output=[]
copy=output==program[:len(output)]
while True:
    opcode(program[position],program[position+1])
    if position>=len(program)-1:break

print("Part 1:",output)

#Test with answer : 117440
program=[0,3,5,4,3,0]

exact_copy=False
rega=0
while not exact_copy:
    reg={'A': rega, 'B': 0, 'C': 0}
    position=0
    output=[]
    copy=output==program[:len(output)]
    while position<len(program)-1:
        opcode(program[position],program[position+1])
        if position>=len(program)-1 or not copy or exact_copy:break
    if exact_copy:break
    rega+=1

rega=117440


