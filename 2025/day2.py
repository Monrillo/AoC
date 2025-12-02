# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 09:33:40 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day2.txt','r') as f: data=f.read().split(',')

#data='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'.split(',')


invalid_1=[]
invalid_2=[]

for d in data:
    a,b=d.split('-')
    id_min=int(a)
    id_max=int(b)
    for n in range(id_min,id_max+1):
        num=str(n)
        if num[len(num)//2:]==num[:len(num)//2]: invalid_1.append(n)
        if any(all(num[0:i]==num[i*j:(i*j)+i] for j in range(1,len(num)//i)) for i in range(1,(len(num)//2)+1) if len(num)%i==0): invalid_2.append(n)


print("Part 1:",sum(invalid_1))

print("Part 2:",sum(invalid_2))
