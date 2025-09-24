# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:38:56 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2020\day4.txt','r') as f: lines=f.readlines()

passports=[]
carac={}

for line in lines:
    if len(line.strip().split(' ')[0])==0:passports.append(carac);carac={}
    else:
        for el in line.strip().split(' '):
            k,v=el.split(':')
            carac[k]=v
passports.append(carac)

valid_carac=['hcl','iyr','eyr','ecl','pid','byr','hgt']
valid_pass=[p for p in passports if all(e in list(p.keys()) for e in valid_carac)]

print("Part 1:",len(valid_pass))

def autom_valid(p):
    try:
        b=int(p['byr'])
        i=int(p['iyr'])
        e=int(p['eyr'])
        h=int(p['hgt'][:-2])
        pi=int(p['pid'])
    except:
        return False
    if not (1920<=b<=2002 and 2010<=i<=2020 and 2020<=e<=2030):return False
    if p['hgt'][-2:]=='in':
        if not 59<=h<=76:return False
    elif p['hgt'][-2:]=='cm':
        if not 150<=h<=193:return False
    elif p['hgt'][-2:]!='cm' or p['hgt'][-2:]!='in':return False
    #if not (p['hgt'][-2:]=='in' and 59<=h<=76) or not (p['hgt'][-2:]=='cm' and 150<=h<=193):return False
    if not (len(p['hcl'])==7 and p['hcl'][0]=='#' and len(re.findall('[a-f]|[0-9]', p['hcl']))==6):return False
    if not (p['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']):return False
    if not (len(p['pid'])==9 and pi<=999999999):return False
    else: return True

valid_pass_2=[p for p in valid_pass if autom_valid(p)]

print("Part 2:",len(valid_pass_2))

