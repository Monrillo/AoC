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
        self.throw=(0,0)
    
    # Setters
    def add_item(self,item):
        self.items.append(item)
    
    def set_oper(self,func):
        self.oper = func
    
    def set_test(self,num):
        self.test_num = num
    
    def set_true(self,num):
        self.throw[0]=num
        
    def set_false(self,num):
        self.throw[1]=num
    
    # Functions
    def inspect(self,old):
        new=eval(self.oper)
        return new

line=' old * old'
old=2
eval(line)









