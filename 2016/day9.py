# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:28:35 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day9.txt','r') as f:
    line=f.read()

line='A(2x2)BCD(2x2)EFG'

cpt=0
new_line=''

while cpt<len(line):
    brackets = re.search(r'\((\d+)x(\d+)\)', line[cpt:])
    if not brackets:
        new_line+=line[cpt:]
        break
    pos=brackets.start(0)
    new_line+=line[cpt:pos]
    sz=int(brackets.group(1))
    rpt=int(brackets.group(2))
    pos + len(brackets.group())
    
line[0:1]



    if line[cpt]=='(' and line[cpt+2]=='x' and line[cpt+4]==')':
        for i in range(int(line[cpt+3])):
            new_line+=line[cpt+5:cpt+5+int(line[cpt+1])]
        cpt+=(5+int(line[cpt+1]))
    else:
        new_line+=line[cpt]
        cpt+=1

print(len(new_line))

length=0
while cpt<len(line):
    if line[cpt]=='(' and line[cpt+2]=='x' and line[cpt+4]==')':
        length+=(int(line[cpt+3])*int(line[cpt+1]))
        cpt+=5+int(line[cpt+1])
    else:
        length+=1
        cpt+=1

print(len(new_line))



def day9a(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d)
    if not bracket:
        return len(d)
    pos = brackets.start(0)
    sz = int(brackets.group(1))
    rpt = int(brackets.group(2))
    i = pos + len(brackets.group())
    return len(d[:pos]) + len(d[i:i+sz]) * rpt + day9a(d[i+sz:])

day9a(line)

brackets = re.search(r'\((\d+)x(\d+)\)', line[cpt:])
