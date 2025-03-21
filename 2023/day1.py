# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:01:43 2025

@author: castelf
"""

import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2023\day1.txt','r') as f: lines=f.readlines()

nums=[''.join(re.findall('(\d+)', line.strip())) for line in lines]
res=0
for num in nums: res+=int(num[0]+num[-1])
print(res)

