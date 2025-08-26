# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 17:47:22 2025

@author: castelf
"""
from collections import deque

marbles=deque([0])

# Nombre de joueurs
num_p=476
# Dernière bille
last_m=7143100

players={p:0 for p in range(num_p)}

for m in range(1,last_m+1):
    if m%23==0:
        marbles.rotate(7)
        players[m%num_p]+=(m+marbles.pop())
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(m)

print(max(players.values()))

