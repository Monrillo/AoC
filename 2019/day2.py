# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:41:19 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2019\day2.txt','r') as f: code_in=[int(l) for l in f.read().split(',')]

#code=[1,1,1,4,99,5,6,0,99]

#Loop
def comp(code):
    p=0
    while True:
        if code[p]==1: code[code[p+3]]=code[code[p+1]]+code[code[p+2]];p+=4
        elif code[p]==2: code[code[p+3]]=code[code[p+1]]*code[code[p+2]];p+=4
        elif code[p]==99: break
    return code[0]

# Replacing for Part 1
code=code_in.copy()
code[1]=12
code[2]=2

print(comp(code))

for noun in range(100):
    for verb in range(100):
        #print(noun,verb)
        code=code_in.copy()
        code[1]=noun
        code[2]=verb
        if comp(code)==19690720:print((100 * noun) + verb)


