# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:33:43 2025

@author: castelf
"""
import re
import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day4.txt','r') as f:
    lines=f.readlines()

# lines=['aaaaa-bbb-z-y-x-123[abxyz]\n',
# 'a-b-c-d-e-f-g-h-987[abcde]\n',
# 'not-a-real-room-404[oarel]\n',
# 'totally-real-room-200[decoy]']

#line='qzmt-zixmtkozy-ivhz-343\n'
#checksum='343'

sector_id=0
for line in lines:
    line=line.strip().split('-')
    letters=''.join(line[:-1])
    words=line[:-1]
    checksum,code=re.findall('(\d+)\[(\w+)\]',line[-1])[0]
    counts={x:letters.count(x) for x in letters}
    if any(x not in list(counts) for x in code):
        continue
    if all(counts[code[i]]>counts[code[i+1]] or \
           (counts[code[i]]==counts[code[i+1]] and ord(code[i])<ord(code[i+1])) for i in range(4)):
        sector_id+=int(checksum)
    phrase=''
    for word in words:
        new_word=np.array([ord(x) for x in word])+int(checksum)%26
        new_word[np.where(new_word>122)[0]]-=26
        phrase+=''.join([chr(x) for x in new_word])+' '
    if phrase.find('north')!=-1:
        sector_northpole=int(checksum)

print(sector_id)
print(sector_northpole)
