# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 11:13:44 2025

@author: castelf
"""

card_order=['A','K','Q','J','T','9','8','7','6','5','4','3','2']

hand_order=[(0,0,0,0,5),(1,0,0,4,0),(0,2,3,0,0),(2,0,3,0,0),(1,4,0,0,0),(3,2,0,0,0),(5,0,0,0,0)]

# lines=['32T3K 765',
# 'T55J5 684',
# 'KK677 28',
# 'KTJJT 220',
# 'QQQJA 483']

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day7.txt','r') as f: lines=f.readlines()

class Hand:
    def __init__(self,line):
        self.cards,self.bid=line.split()
        self.hand=tuple([self.cards.count(c) for c in list(self.cards)].count(n) for n in range(1,6))
    
    def get_bid(self): return int(self.bid)
    
    def get_cards(self): return [card_order.index(c) for c in list(self.cards)]
    
    def get_hand(self): return hand_order.index(self.hand)

def tri(hand1,hand2):
    sup=False
    if hand1.get_hand()<hand2.get_hand():sup=True
    elif hand1.get_hand()==hand2.get_hand():
        cpt=0
        while True:
            if hand1.get_cards()[cpt]<hand2.get_cards()[cpt]: sup=True;break
            elif hand1.get_cards()[cpt]>hand2.get_cards()[cpt]: sup=False;break
            cpt+=1
    return sup


# Part 1
res=[Hand(lines[0])]
for line in lines[1:]:
    h=Hand(line)
    inser=False
    for i in range(len(res)):
        if not tri(h,res[i]): res.insert(i,h);inser=True;break
    if not inser:res.append(h)
result=0
for i in range(len(res)):result+=(i+1)*res[i].get_bid()
print(result)

#Part 2
card_order=['A','K','Q','T','9','8','7','6','5','4','3','2','J']

class Hand2(Hand):
    def __init__(self,line):
        super().__init__(line)
        self.hand2=hand_order.index(self.hand)
        if 'J' in self.cards:
            for r in card_order[:-1]:
                new_ord=hand_order.index(tuple([self.cards.replace('J',r).count(c) for c in list(self.cards.replace('J',r))]\
                                          .count(n) for n in range(1,6)))
                if new_ord<self.hand2: self.hand2=new_ord
    
    def get_hand(self): return self.hand2

res=[Hand2(lines[0])]
for line in lines[1:]:
    h=Hand2(line)
    inser=False
    for i in range(len(res)):
        if not tri(h,res[i]): res.insert(i,h);inser=True;break
    if not inser:res.append(h)
result=0
for i in range(len(res)):result+=(i+1)*res[i].get_bid()
print(result)




