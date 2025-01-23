# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:09:44 2025

@author: castelf
"""

import numpy as np

words = np.loadtxt('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day6.txt',dtype=str)
code=[]

for word in words:
    code.append(np.array(list(word)))
code=np.array(code).T
res=[]

for c in code:
    res.append(''.join(c))
alphabet='abcdefghijklmnopqrstuvwxyz'
ans1=''
ans2=''

for resul in res:
    num=np.array([resul.count(x) for x in alphabet])
    ans1+=alphabet[np.where(num==np.max(num))[0][0]]
    ans2+=alphabet[np.where(num==np.min(num))[0][0]]

print(ans1)
print(ans2)

# from collections import Counter
# ans1, ans2 = '', ''
# with open('06.txt') as fp:
#     for stuff in zip(*fp.read().strip().split('\n')):
#         counter = Counter(stuff).most_common()
#         ans1 += counter[0][0]
#         ans2 += counter[-1][0]
# print(ans1)
# print(ans2)