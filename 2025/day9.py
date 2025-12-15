# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 09:41:09 2025

@author: castelf
"""

import numpy as np

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day9.txt','r') as f: lines=f.readlines()

# lines=['7,1',
# '11,1',
# '11,7',
# '9,7',
# '9,5',
# '2,5',
# '2,3',
# '7,3']

tiles=[[int(line.strip().split(',')[1]),int(line.strip().split(',')[0])] for line in lines]

rectangle=[]
for i in range(len(tiles)-1):
    for j in range(i+1,len(tiles)):
        rectangle.append((abs(tiles[i][0]-tiles[j][0])+1)*(abs(tiles[i][1]-tiles[j][1])+1))

print("Part 1:",max(rectangle))

arr_tiles=np.array(tiles)

matrix=np.zeros((np.max(arr_tiles[:,0])+2,np.max(arr_tiles[:,1])+3),dtype=int)
for t in tiles:
    matrix[t[0],t[1]]=1

for i in range(matrix.shape[0]):
    if len(np.where(matrix[i]==1)[0])>0:
        matrix[i][np.where(matrix[i]==1)[0][0]:np.where(matrix[i]==1)[0][-1]+1]=1

for i in range(matrix.shape[1]):
    if len(np.where(matrix[:,i]==1)[0])>0:
        matrix[:,i][np.where(matrix[:,i]==1)[0][0]:np.where(matrix[:,i]==1)[0][-1]+1]=1

print(matrix)
print(np.sum(matrix))


print(len(np.where(matrix=='#')[0]))


matrix=np.zeros((np.max(tiles[:,0])+2,np.max(tiles[:,1])+3),dtype=bool)
for t in tiles:
    matrix[t[0],t[1]]=True

print(matrix)


# From mine49r (AoC solution Reddit) 

# INPUT_FILE = "input.txt"

# def part1():
#     with open(INPUT_FILE, "r") as f:
#         coords = [[int(n) for n in line.strip().split(",")] for line in f]

#     area = 0
#     for i in range(len(coords)):
#         x1, y1 = coords[i]
#         for j in range(i+1, len(coords)):
#             x2, y2 = coords[j]
#             if x1 != x2 and y1 != y2:
#                 a = (abs(x1-x2)+1) * (abs(y1-y2)+1)
#                 area = max(area, a)
#     print(area)


# def part2():
#     with open(INPUT_FILE, "r") as f:
#         coords = [[int(n) for n in line.strip().split(",")] for line in f]

#     max_x = max([c[0] for c in coords])
#     max_y = max([c[1] for c in coords])

#     # Vertical sweep
#     spans = [None for y in range(max_y+2)]
#     coords.append(coords[0])
#     for i in range(1, len(coords)):
#         x1, y1 = coords[i-1]
#         x2, y2 = coords[i]
#         if x1 > x2: x1,x2 = x2,x1
#         if y1 > y2: y1,y2 = y2,y1
#         for y in range(y1,y2+1):
#             if spans[y] is None:
#                 spans[y] = [x1, x2]
#             else:
#                 sx1, sx2 = spans[y]
#                 spans[y] = [min(x1, sx1), max(x2, sx2)]
#     coords.pop()

#     '''
#     for y in range(max_y+2):
#         if spans[y] is None:
#             print("." * (max_x+2))
#         else:
#             sx1, sx2 = spans[y]
#             print(f"{'.' * sx1}{'X' * (sx2-sx1+1)}{'.' * (max_x+1-sx2)}")
#     return
#     '''

#     def rect_ok(x1, y1, x2, y2):
#         if x1 > x2: x1,x2 = x2,x1
#         if y1 > y2: y1,y2 = y2,y1
#         for y in range(y1, y2+1):
#             sx1, sx2 = spans[y]
#             if x1 < sx1 or x1 > sx2 or x2 < sx1 or x2 > sx2:
#                 return False
#         return True

#     area = 0
#     for i in range(len(coords)):
#         x1, y1 = coords[i]
#         for j in range(i+1, len(coords)):
#             x2, y2 = coords[j]
#             if x1 != x2 and y1 != y2:
#                 a = (abs(x1-x2)+1) * (abs(y1-y2)+1)
#                 if a > area and rect_ok(x1, y1, x2, y2):
#                     area = a
#     print(area)

# part1()
# part2()
