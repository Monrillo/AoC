# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:34:31 2025

@author: castelf

Solution thanks to pedrosorio
"""

from collections import deque
from itertools import permutations

mat = [line.strip() for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2016\day24.txt').readlines()]

# lines=['###########',
# '#0.1.....2#',
# '#.#######.#',
# '#4.......3#',
# '###########']

# mat=[line.strip() for line in lines]

# find position of numbers into the map
def find_position(mp, num):
    pos = [(i,j) for i in range(len(mp)) for j in range(len(mp[i])) if mp[i][j]==str(num)]
    if pos:
        return pos[0]

num_pos = [find_position(mat, n) for n in range(10) if find_position(mat, n)!=None]
init_pos = num_pos.pop(0)

directions = set([(-1, 0), (1, 0), (0, 1), (0, -1)])

# I use the bfs algorithm from pedrosorio solution (BST stands for Binary Search Tree)
# to compute the distance between 2 number positions into the map
def dist_from_to(mp, fr, to):
    path = deque([(0, fr)])
    visited = set([fr])
    
    while path:
        dist, pos = path.pop()
        if pos == to:
            return dist
        
        y, x = pos
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if mp[ny][nx]!='#' and (ny, nx) not in visited:
                visited.add((ny, nx))
                path.appendleft((dist+1,(ny, nx)))

# Compute distances from initial position (0)
dst_init = [dist_from_to(mat, init_pos, n_pos) for n_pos in num_pos]

# Compute distances between all other numbers
K = len(num_pos)
distances = [[None for j in range(K)] for i in range(K)]
for i in range(K):
    for j in range(i+1,K):
        distances[i][j] = distances[j][i] = dist_from_to(mat, num_pos[i], num_pos[j])

# Once all distances have been computed between numbers, the problem is like a
# TSP (for Travelling Salesman Problem) with O(K!) complexity but this can be
# computed in our case because of the limited amount of points in our maze

# At first I tried to compute all route lengths and select the shortest one
# It does not work, too many routes, I use the solution from pedrosorio with
# a for loop and returning the shortest result

length_1, length_2 = 1e12, 1e12
for path in permutations(range(K)):
    #computation of the length of a path
    dst = dst_init[path[0]] + sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
    length_1 = min(length_1, dst)
    dst += dst_init[path[-1]]
    length_2 = min(length_2, dst)

print("Part 1:",length_1)

print("Part 2:",length_2)
