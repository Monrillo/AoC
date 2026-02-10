# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 14:50:51 2026

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day20.txt','r') as f: lines=f.readlines()

def bin_to_dec(n):
    return sum([2**i for i,e in enumerate(n[::-1]) if e==1])

# lines=['..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##',
# '#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###',
# '.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.',
# '.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....',
# '.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..',
# '...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....',
# '..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
# '',
# '#..#.',
# '#....',
# '##..#',
# '..#..',
# '..###']

algo=''
image=[]
algo_sec=True

for l in lines:
    if l.strip('\n')=='':algo_sec=False
    elif algo_sec: algo+=l.strip('\n').replace('.','0').replace('#','1')
    else: image.append(list(l.strip('\n').replace('.','0').replace('#','1')))
image=np.array(image,dtype=int)

def scan(img):
    res=img.reshape(1,9)[0]
    num=bin_to_dec(res)
    return int(algo[num])


for _ in range(2):
    input_image=np.pad(image,2,constant_values=0)
    output_image=np.zeros((input_image.shape[0]-2,input_image.shape[1]-2),dtype=int)
    for l in range(1,input_image.shape[0]-1):
        for c in range(1,input_image.shape[1]-1):
            output_image[l-1][c-1]=scan(input_image[l-1:l+2,c-1:c+2])
    image=output_image.copy()

print("Part 1:",np.sum(image))

###########################################################################

def build_map(map, filler):
    w = len(map[0]) + 2
    new_map = []
    new_map.append([filler] * w)
    for line in map:
        new_map.append([filler] + line + [filler])
    new_map.append([filler] * w)
    return new_map


def get_neighbors(r, c, map, filler):
    bs = ""
    for rm in range(-1, 2):
        for cm in range(-1, 2):
            if r + rm < 0 or r + rm >= len(map) or c + cm < 0 or c + cm >= len(map[0]):
                bs += str(filler)
            else:
                bs += str(map[r + rm][c + cm])
    return 1 if alg[int(bs, 2)] == "#" else 0


data = open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day20.txt').read().strip().split("\n\n")
alg = data.pop(0)
map = [[0 if j == "." else 1 for j in i] for i in data[0].split("\n")]

for i in range(1, 50 + 1):
    # determine state of infinite pixels
    filler = 1 if alg[0] == "#" and alg[-1] == "." and not i % 2 else 0
    map = build_map(map, filler)
    # iterate over map and find updates
    changes = {}
    for r in range(len(map)):
        for c in range(len(map[0])):
            changes[(r, c)] = get_neighbors(r, c, map, filler)
    # apply updates to map
    for r, c in changes:
        map[r][c] = changes[(r, c)]
    if i == 2:
        print(f"Part 1: {sum([val for sublist in map for val in sublist])}")
print(f"Part 2: {sum([val for sublist in map for val in sublist])}")