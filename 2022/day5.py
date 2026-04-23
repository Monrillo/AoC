# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:48:51 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day5.txt','r') as f: lines=f.readlines()

# lines=['    [D]    ',
# '[N] [C]    ',
# '[Z] [M] [P]',
# ' 1   2   3 ',
# '',
# 'move 1 from 2 to 1',
# 'move 3 from 1 to 3',
# 'move 2 from 2 to 1',
# 'move 1 from 1 to 2']

stack={}
for i in range(9):
    stack[i+1]=[]

stacking=True
for line in lines:
    if line.strip('\n')=='':
        stacking=False
    elif stacking:
        for i in range(9):
            if line[4*i+1]!=' ':
                try :
                    if int(line[4*i+1])==i+1:stack[i+1].reverse()
                except:
                    stack[i+1].append(line[4*i+1])
    elif not stacking:
        _,num,_,dep,_,arr=line.strip('\n').split(' ')
        for _ in range(int(num)):stack[int(arr)]+=stack[int(dep)].pop(-1)

print("Part 1:",''.join([stack[s][-1] for s in stack]))

stack={}
for i in range(9):
    stack[i+1]=[]

stacking=True
for line in lines:
    if line.strip('\n')=='':
        stacking=False
    elif stacking:
        for i in range(9):
            if line[4*i+1]!=' ':
                try :
                    if int(line[4*i+1])==i+1:stack[i+1].reverse()
                except:
                    stack[i+1].append(line[4*i+1])
    elif not stacking:
        _,num,_,dep,_,arr=line.strip('\n').split(' ')
        stack[int(arr)]+=stack[int(dep)][-int(num):]
        del(stack[int(dep)][-int(num):])

print("Part 2:",''.join([stack[s][-1] for s in stack]))

