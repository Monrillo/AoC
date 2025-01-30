# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:31:36 2025

@author: castelf
"""
#import numpy as np
#import re
from collections import defaultdict

instructions=[line.split() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day10.txt','r')]

# test=['value 5 goes to bot 2\n',
# 'bot 2 gives low to bot 1 and high to bot 0\n',
# 'value 3 goes to bot 1\n',
# 'bot 1 gives low to output 1 and high to bot 0\n',
# 'bot 0 gives low to output 2 and high to output 0\n',
# 'value 2 goes to bot 2']
# instructions=[line.split() for line in test]
#res=[re.search('bot (\d+)',line) for line in test]
#res_out=[re.search('output (\d+)',line) for line in test]

bot=defaultdict(list)
output=defaultdict(list)
workflow={}

#Initialisation
for inst in instructions:
    if inst[0]=='value': bot[int(inst[-1])].append(int(inst[1]))
    elif inst[0]=='bot': workflow[int(inst[1])]=(inst[5],int(inst[6]),inst[10],int(inst[11]))
        
# Assign values
while bot:
    for k in list(bot):
        if len(bot[k])==2:
            if bot[k]==[61,17] or bot[k]==[17,61]: print(k)
            eval(workflow[k][0])[workflow[k][1]].append(min(bot[k]))
            eval(workflow[k][2])[workflow[k][3]].append(max(bot[k]))
            del bot[k]

print(output[0][0]*output[1][0]*output[2][0])
