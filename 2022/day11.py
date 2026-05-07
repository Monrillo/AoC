# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:19:36 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day11.txt','r') as f: lines=f.readlines()

lines=['Monkey 0:',
'  Starting items: 79, 98',
'  Operation: new = old * 19',
'  Test: divisible by 23',
'    If true: throw to monkey 2',
'    If false: throw to monkey 3',
'',
'Monkey 1:',
'  Starting items: 54, 65, 75, 74',
'  Operation: new = old + 6',
'  Test: divisible by 19',
'    If true: throw to monkey 2',
'    If false: throw to monkey 0',
'',
'Monkey 2:',
'  Starting items: 79, 60, 97',
'  Operation: new = old * old',
'  Test: divisible by 13',
'    If true: throw to monkey 1',
'    If false: throw to monkey 3',
'',
'Monkey 3:',
'  Starting items: 74',
'  Operation: new = old + 3',
'  Test: divisible by 17',
'    If true: throw to monkey 0',
'    If false: throw to monkey 1']

class Monkey:
    # Initialize
    def __init__(self):
        self.items=[]
        self.inspection=0
    
    # Setters
    def add_item(self,item):
        self.items.append(item)
    
    def set_oper(self,func):
        self.oper = func
    
    def set_test(self,num):
        self.test_num = num
    
    def set_true(self,num):
        self.true=num
        
    def set_false(self,num):
        self.false=num
    
    # Getters
    def get_inspect(self):
        return self.inspection
    
    def get_items(self):
        return self.items
    
    # Function
    def inspect(self,part1):
        self.inspection+=1
        old=self.items.pop(0)
        new=eval(self.oper)
        if part1: new//=3
        check=new%self.test_num==0
        if check: return (self.true,new)
        else: return (self.false,new)

monkeys=[]
for line in lines:
    if line.strip('\n')=='':monkeys.append(m)
    elif line.strip('\n').startswith('Monkey'):m=Monkey();l=0
    else:
        l+=1
        if l==1:
            for x in line.strip('\n').split(': ')[1].split(', '):
                m.add_item(int(x))
        elif l==2:
            m.set_oper(line.strip('\n').split('= ')[1])
        elif l==3:
            m.set_test(int(line.strip('\n').split('by ')[1]))
        elif l==4:
            m.set_true(int(line.strip('\n').split('monkey ')[1]))
        elif l==5:
            m.set_false(int(line.strip('\n').split('monkey ')[1]))
monkeys.append(m)

# for m in monkeys:
#     print(m.get_items())

for _ in range(20):
    # Round
    for m in monkeys:
        while len(m.get_items())>0:
            receiver,item = m.inspect(True)
            monkeys[receiver].add_item(item)

# Two most active monkeys
a,b=sorted([m.get_inspect() for m in monkeys])[-2:]

print("Part 1:",a*b)

monkeys=[]
for line in lines:
    if line.strip('\n')=='':monkeys.append(m)
    elif line.strip('\n').startswith('Monkey'):m=Monkey();l=0
    else:
        l+=1
        if l==1:
            for x in line.strip('\n').split(': ')[1].split(', '):
                m.add_item(int(x))
        elif l==2:
            m.set_oper(line.strip('\n').split('= ')[1])
        elif l==3:
            m.set_test(int(line.strip('\n').split('by ')[1]))
        elif l==4:
            m.set_true(int(line.strip('\n').split('monkey ')[1]))
        elif l==5:
            m.set_false(int(line.strip('\n').split('monkey ')[1]))
monkeys.append(m)

exchange=[]
r=0
loop=False
while r<700:
    # Round
    r+=1
    for m in monkeys:
        while len(m.get_items())>0:
            receiver,item = m.inspect(False)
            monkeys[receiver].add_item(item)
    # I made superficial copy of items
    res=[m.get_items()[:] for m in monkeys]
    for e in exchange:
        if res==e:
            loop=True
    if loop:
        break
    exchange.append(res)




