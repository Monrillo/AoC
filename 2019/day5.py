# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 14:18:22 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day5.txt','r') as f: code_in=f.read().split(',')

#code=[1,1,1,4,99,5,6,0,99]

#Loop
def read_code(code):
    p=0
    while True:
        if len(code[p])==5:
            opcode=int(code[p][-2:])
            p1=int(code[p][-3])
            p2=int(code[p][-4])
            p3=int(code[p][-5])
        elif len(code[p])==4:
            opcode=int(code[p][-2:])
            p1=int(code[p][-3])
            p2=int(code[p][-4])
            p3=0
        elif len(code[p])==3:
            opcode=int(code[p][-2:])
            p1=int(code[p][-3])
            p2=0
            p3=0
        else :
            opcode=int(code[p])
            p1=0
            p2=0
            p3=0
            
        if code[p]==1: code[code[p+3]]=code[code[p+1]]+code[code[p+2]];p+=4
        elif code[p]==2: code[code[p+3]]=code[code[p+1]]*code[code[p+2]];p+=4
        elif code[p]==99: break
    return code[0]




n='1002'
len(n)
int(n[-2:])
n[-3]
n[-4]
n[-5]
