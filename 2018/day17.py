# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 16:59:28 2025

@author: castelf

Solution in a relevant time by nightcoder01 (initially in Python 2)
"""
# from collections import deque

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day17.txt','r') as f: lines=f.readlines()

# lines=['x=495, y=2..7',
# 'y=7, x=495..501',
# 'x=501, y=3..7',
# 'x=498, y=2..4',
# 'x=506, y=1..2',
# 'x=498, y=10..13',
# 'x=504, y=10..13',
# 'y=13, x=498..504']

# blocks = set()
# floor = 0

# for line in lines:
#     a, val_a = line.strip().split(', ')[0].split('=')
#     b, interval_b = line.strip().split(', ')[1].split('=')
#     bounds = [int(x) for x in interval_b.split('..')]
#     for i in range(bounds[0], bounds[1] + 1):
#         if a == 'x':
#             blocks.add((int(val_a), i))
#             floor = max(floor, i)
#         else:
#             blocks.add((i, int(val_a)))
#             floor = max(floor, int(val_a))


# drop = deque([(500, 0)])
# water = set()

# def render(bl, wat):
#     '''Fonction pour afficher la position de l'eau et des blocks (pour le déboggage)'''
#     lines = []
#     for y in range(14):
#         line = ''
#         for x in range(494, 508):
#             if (x, y) in bl:
#                 line += '#'
#             elif (x, y) in wat:
#                 line += '~'
#             else:
#                 line += '.'
#         lines.append(line)
#     return '\n'.join(lines)

# #########################################

# while drop:
#     x, y = drop.pop()
    
#     if y + 1 <= floor:
        
#         if (x, y + 1) not in water and (x, y + 1) not in blocks:
#             drop.appendleft((x, y + 1))
#             water.add((x, y + 1))
#         else:
#             stream = deque([(x, y, 'l'), (x, y, 'r')])
#             leak = False
#             while stream:
#                 nx, ny, direction = stream.pop()
#                 if direction == 'l':
#                     if (nx - 1, ny) not in blocks:
#                         water.add((nx - 1, ny))
#                         if (nx - 1, ny + 1) not in water and (nx - 1, ny + 1) not in blocks:
#                             leak = True
#                             drop.appendleft((nx - 1, ny))
#                         else:
#                             stream.appendleft((nx - 1, ny, 'l'))
                            
#                 elif direction == 'r':
#                     if (nx + 1, ny) not in blocks:
#                         water.add((nx + 1, ny))
#                         if (nx + 1, ny + 1) not in water and (nx + 1, ny + 1) not in blocks:
#                             leak = True
#                             drop.appendleft((nx + 1, ny))
#                         else:
#                             stream.appendleft((nx + 1, ny, 'r'))
            
#             if not leak:
#                 drop.appendleft((x, y - 1))

# print("Part 1:", len(water))




import re
import sys
import time

sys.setrecursionlimit(3000)

def flow(grid, x, y, d):
    if grid[y][x] == '.':
        grid[y][x] = '|'
    if y == len(grid) - 1:
        return
    if grid[y][x] == '#':
        return x
    if grid[y+1][x] == '.':
        flow(grid, x, y+1, 0)
    if grid[y+1][x] in '~#':
        if d:
            return flow(grid, x+d, y, d)
        else:
            leftX = flow(grid, x-1, y, -1)
            rightX = flow(grid, x+1, y, 1)
            if grid[y][leftX] == '#' and grid[y][rightX] == '#':
                for fillX in range(leftX+1, rightX):
                    grid[y][fillX] = '~'
    else:
        return x

def solve(filename):
    data = []
    for line in open(filename).read().splitlines():
        a, b, c = map(int, re.findall('\d+', line))
        data += [(a, a, b, c)] if line[0] == 'x' else [(b, c, a, a)]
    
    # Z = zip(*data)
    # minX, maxX, minY, maxY = min(Z[0]), max(Z[1]), min(Z[2]), max(Z[3])
    
    Z = zip(*data)
    Z_list = list(Z)
    minX, maxX, minY, maxY = min(Z_list[0]), max(Z_list[1]), min(Z_list[2]), max(Z_list[3])
    
    grid = [['.']*(maxX - minX + 2) for _ in range(maxY + 1)]
    for x1, x2, y1, y2 in data:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x - minX + 1] = '#'
    springX, springY = 500 - minX + 1, 0
    grid[0][springX] = '+'
    
    flow(grid, springX, springY, 0)
    
    still = flowing = 0
    for y in range(minY, maxY + 1):
        for x in range(len(grid[0])):
            if grid[y][x] == '|':
                flowing += 1
            elif grid[y][x] == '~':
                still += 1
    
    return still + flowing, still

startTime = time.time()
ans1, ans2 = solve('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day17.txt')
endTime = time.time()
print ('\nfinished in %.6f sec' % (endTime - startTime))
print ('ans (part 1): ' + str(ans1))
print ('ans (part 2): ' + str(ans2))

















