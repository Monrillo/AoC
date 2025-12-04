# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 09:28:06 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day3.txt','r') as f: lines=f.readlines()

# lines=['987654321111111',
# '811111111111119',
# '234234234234278',
# '818181911112111']

def part1(line):
    num1=max(line)
    pos1=line.index(num1)
    numa='';numb=''
    if line[:pos1]!='': numa=max(line[:pos1])
    if line[pos1+1:]!='': numb=max(line[pos1+1:])
    prop1=int(numa+num1)
    prop2=int(num1+numb)
    return max(prop1,prop2)

def part2(line):
    res=''
    pos=len(line)-12
    for c in range(len(line)):
        if len(res)==12:break
        if c>=pos:
            res+=line[c]
        elif c<pos:
            m=max(line[c:pos])
            if line[c]==m and m>=line[pos]:
                res+=line[c]
                if pos<len(line)-1:pos+=1
    return res

resultat=0
resultat_2=0
for l in lines:
    resultat+=part1(l.strip())
    resultat_2+=int(part2(l.strip()))
    
print("Part 1:",resultat)

print("Part 2:",resultat_2)


