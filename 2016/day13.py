# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:25:20 2025

@author: castelf
"""

import numpy as np

area=np.full((10,10),'.')
odfn=10
for x in range(len(area)):
    for y in range(len(area)):
        num=(x*x + 3*x + 2*x*y + y + y*y)+odfn
        if bin(num)[2:].count('1')%2==1: area[y,x]='#'

area[1,1]='O'
area[4,7]='X'

print(area)
