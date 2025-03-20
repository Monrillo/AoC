# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 10:25:35 2025

@author: castelf
"""

import numpy as np

inst=np.array([line.strip().split(' => ') for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day21.txt','r').readlines()])

matrix=np.array([['.','#','.'],['.','.','#'],['#','#','#']])

# lines=['../.# => ##./#../...\n',
# '.#./..#/### => #..#/..../..../#..#']
# inst=np.array([line.strip().split(' => ') for line in lines])

def cons_mat(line):
    res=[]
    for i in line.split('/'): res.append(list(i))
    return np.array(res)

def line_mat(mat):
    line=''
    for i in range(len(mat)):line+=''.join(mat[i])+'/'
    return line[:-1]

def check_mat(mat):
    for m in [mat,np.rot90(mat),np.fliplr(mat),np.rot90(np.fliplr(mat)),np.flipud(mat),np.rot90(np.flipud(mat)),np.fliplr(np.flipud(mat)),np.rot90(np.fliplr(np.flipud(mat)))]:
        if line_mat(m) in inst[:,0]: return np.where(inst[:,0]==line_mat((m)))[0][0];break

for _ in range(5):
    if len(matrix)%2==0: num_mat=len(matrix)//2
    else: num_mat=len(matrix)//3
    
    cut=np.concatenate([np.hsplit(m,num_mat) for m in np.vsplit(matrix,num_mat)])
    new_mat=[cons_mat(inst[check_mat(c),1]) for c in cut]
    matrix=np.block([new_mat[i:i+num_mat] for i in range(len(new_mat)//num_mat)])

print(np.where(matrix=='#')[0].size)


import numpy as np
from collections import Counter


def expand(pre, post):
    rules = []

    for k in [0, 1, 2, 3]:
        rot = np.rot90(pre, k=k)
        rules.append((rot.flatten(), post))
        rules.append((np.fliplr(rot).flatten(), post))
        rules.append((np.flipud(rot).flatten(), post))

    return rules


def match(incell, rules):
    for pre, post in rules:
        if np.allclose(incell.flatten(), pre):
            return post
    assert False


def iterate(grid):
    size = len(grid)
    if size % 2 == 0:
        steps = size // 2
        new_grid = np.zeros((3*steps, 3*steps))
        for row in range(steps):
            for col in range(steps):
                incell = grid[2*row:2*row + 2, 2*col:2*col + 2].copy()
                outcell = match(incell, rules2)
                new_grid[3*row:3*row + 3, 3*col:3*col + 3] = outcell.copy()
    elif size % 3 == 0:
        steps = size // 3
        new_grid = np.zeros((4*steps, 4*steps))
        for row in range(steps):
            for col in range(steps):
                incell = grid[3*row:3*row + 3, 3*col:3*col + 3].copy()
                outcell = match(incell, rules3)
                new_grid[4*row:4*row + 4, 4*col:4*col + 4] = outcell.copy()
    else:
        assert False
    return new_grid


def calc_block_map_3_iters(block_string):
    block = np.array([int(c) for c in block_string]).reshape((3, 3))

    grid = iterate(block)
    grid = iterate(grid)
    grid = iterate(grid)

    counts = Counter()
    for row in range(3):
        for col in range(3):
            to_block = grid[3*row:3*row+3, 3*col:3*col+3]
            to_block = ''.join(str(int(x)) for x in to_block.flatten())
            counts[to_block] += 1

    return counts


def fast_count(init_block, steps):
    if steps % 3 != 0:
        assert False
    steps //= 3

    block_counts = Counter()
    block_counts[init_block] += 1
    maps = {}

    for step in range(steps):
        new_block_counts = Counter()

        for block, count in block_counts.items():
            if block not in maps:
                maps[block] = calc_block_map_3_iters(block)
            for to_block, to_count in maps[block].items():
                new_block_counts[to_block] += count * to_count

        block_counts = new_block_counts

    total_ones = 0
    for block, count in block_counts.items():
        total_ones += block.count("1") * count

    return total_ones


rules2 = []
rules3 = []
with open("C:\\Users\castelf\Documents\GitHub\AoC\\2017\day21.txt") as f:
    for line in f.readlines():
        pre, post = line.strip().split(" => ")
        pre = pre.replace("/", "")
        post = post.replace("/", "")
        pre = np.array([1 if c == "#" else 0 for c in pre])
        post = np.array([1 if c == "#" else 0 for c in post])

        if len(pre) == 4:
            rules2 += expand(pre.reshape((2, 2)), post.reshape((3, 3)))
        elif len(pre) == 9:
            rules3 += expand(pre.reshape((3, 3)), post.reshape((4, 4)))
        else:
            assert False

init_block = "010001111"
print(fast_count(init_block, 12))



lines = open('C:\\Users\castelf\Documents\GitHub\AoC\\2017\day21.txt').read().strip().split('\n')

rules = {}
for line in lines:
    i, o = line.split('=>')
    i = tuple([tuple(s) for s in i.strip().split('/')])
    o = tuple([tuple(s) for s in o.strip().split('/')])

    n = len(i)
    def new_coords(r, c, flipped, reverse_r, reverse_c):
        if reverse_r:
            r = n-1-r
        if reverse_c:
            c = n-1-c
        if flipped:
            r,c = c,r
        return i[r][c]
    for flipped in [True,False]:
        for reverse_r in [True,False]:
            for reverse_c in [True,False]:
                ii = tuple([tuple(new_coords(r,c,flipped,reverse_r,reverse_c) for c in range(n)) for r in range(n)])
                rules[ii] = o

pattern = [list('.#.'), list('..#'), list('###')]

for t in range(19):
    n = len(pattern)

    ans = 0
    for r in range(n):
        for c in range(n):
            if pattern[r][c] == '#':
                ans += 1
    print (t, ans)

    if n%2==0:
        block_size = 2
    else:
        block_size = 3
    assert n%block_size == 0
    new_blocks = []
    for r in range(n//block_size):
        block_row = []
        for c in range(n//block_size):
            block_in = tuple([tuple([pattern[r*block_size+rr][c*block_size+cc] for cc in range(block_size)]) for rr in range(block_size)])
            block_row.append(rules[block_in])
        new_blocks.append(block_row)
    new_n = n//block_size*(block_size+1)
    def from_block(r,c):
        r0, r1 = r//(block_size+1), r%(block_size+1)
        c0, c1 = c//(block_size+1), c%(block_size+1)
        return new_blocks[r0][c0][r1][c1]
    new_pattern = [[from_block(r,c) for c in range(new_n)] for r in range(new_n)]
    pattern = new_pattern