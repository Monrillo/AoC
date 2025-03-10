# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 15:10:25 2025

@author: castelf
"""
import numpy as np

circ=np.arange(256)
length=np.array([206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3])

# circ=np.arange(5)
# length=np.array([3,4,1,5])

skip=0
cpt=0
for l in length:
    if cpt+l<=len(circ): circ[cpt:cpt+l]=np.flip(circ[cpt:cpt+l])
    elif cpt+l>len(circ):
        newarr=np.flip(np.concatenate((circ[cpt:cpt+l],circ[:(cpt+l)%len(circ)])))
        circ[cpt:cpt+l]=newarr[:len(circ[cpt:cpt+l])]
        circ[:(cpt+l)%len(circ)]=newarr[len(circ[cpt:cpt+l]):]
    cpt+=(l+skip)
    cpt=cpt%len(circ)
    skip+=1
print(circ[0]*circ[1])

test='206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3'

from functools import reduce

lens = [ord(x) for x in test]
lens.extend([17,31,73,47,23])
nums = [x for x in range(0,256)]
pos = 0
skip = 0
for _ in range(64):
	for l in lens:
		to_reverse = []
		for x in range(l):
			n = (pos + x) % 256
			to_reverse.append(nums[n])
		to_reverse.reverse()
		for x in range(l):
			n = (pos + x) % 256
			nums[n] = to_reverse[x]
		pos += l + skip
		pos = pos % 256
		skip += 1
dense = []
for x in range(0,16):
	subslice = nums[16*x:16*x+16]
	dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
print(''.join(dense))