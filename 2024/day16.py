# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:12:34 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day16.txt','r') as f: lines=f.readlines()

from collections import deque

# lines=['###############',
# '#.......#....E#',
# '#.#.###.#.###.#',
# '#.....#.#...#.#',
# '#.###.#####.#.#',
# '#.#.#.......#.#',
# '#.#.#####.###.#',
# '#...........#.#',
# '###.#.#####.#.#',
# '#...#.....#.#.#',
# '#.#.#.###.#.#.#',
# '#.....#...#.#.#',
# '#.###.#.#.#.#.#',
# '#S..#.....#...#',
# '###############']

lines=['#################',
'#...#...#...#..E#',
'#.#.#.#.#.#.#.#.#',
'#.#.#.#...#...#.#',
'#.#.#.#.###.#.#.#',
'#...#.#.#.....#.#',
'#.#.#.#.#.#####.#',
'#.#...#.#.#.....#',
'#.#.#####.#.###.#',
'#.#.#.......#...#',
'#.#.###.#####.###',
'#.#.#...#.....#.#',
'#.#.#.#####.###.#',
'#.#.#.........#.#',
'#.#.#.#########.#',
'#S#.............#',
'#################']

maze=[list(l.strip('\n')) for l in lines]
num_l=len(maze)
num_c=len(maze[0])
for l in range(num_l):
    for c in range(num_c):
        if maze[l][c]=='S':
            start=(l,c)
            maze[l][c]='.'
        elif maze[l][c]=='E':
            end=(l,c)
            maze[l][c]='.'

# headings=[ > , v , < , ^ ]
headings=[[0,1],[1,0],[0,-1],[-1,0]]

trackers=deque([(start,0,0)]) # position (l,c), head, score

def possib_tracks(pos,head,score,reverse):
    # reverse=1 for first track and -1 for the reverse track
    h1=(pos[0]+headings[head][0],pos[1]+headings[head][1]),head,score+reverse*(1)
    h2=(pos[0]+headings[(head-1)%4][0],pos[1]+headings[(head-1)%4][1]),(head-1)%4,score+reverse*(1001)
    h3=(pos[0]+headings[(head+1)%4][0],pos[1]+headings[(head+1)%4][1]),(head+1)%4,score+reverse*(1001)
    return h1,h2,h3

while trackers:    
    pos,head,score=trackers.popleft()
    if maze[pos[0]][pos[1]]=='.' or \
        (isinstance(maze[pos[0]][pos[1]],int) and score<maze[pos[0]][pos[1]]):
            maze[pos[0]][pos[1]]=score
            for p in possib_tracks(pos,head,score,1):
                trackers.append(p)

print("Part 1:",maze[end[0]][end[1]])

rev_trackers=deque([(end,1,maze[end[0]][end[1]]),(end,2,maze[end[0]][end[1]])]) # reverse trackers

spot=set()
while rev_trackers:    
    pos,head,score=rev_trackers.popleft()
    if isinstance(maze[pos[0]][pos[1]],int) and (score==maze[pos[0]][pos[1]] or score==maze[pos[0]][pos[1]]-1000):
        spot.add(pos)
        for p in possib_tracks(pos,head,score,-1):
            rev_trackers.append(p)

print("Part 2:",len(spot))

spot.add(pos)


trackers=deque([([end],1,maze[end[0]][end[1]]),([end],2,maze[end[0]][end[1]])]) # path, head, score



#spot={}
# spot=set()
while trackers:    
    path,head,score=trackers.popleft()
    pos=path[-1]
    # if pos==end:
    #     spot|=set(path)
    #     # if not score in spot: spot[score]=set(path)
    #     # else: spot[score]|=set(path)

    for p in possib_tracks(pos,head):
        if p[1]==head:new_score=score+1
        else:new_score=score+1001
        
        if maze[p[0][0]][p[0][1]]=='.' or isinstance(maze[p[0][0]][p[0][1]],int) and new_score<=maze[p[0][0]][p[0][1]]:
            maze[p[0][0]][p[0][1]]=new_score
            trackers.append((path+[p[0]],p[1],new_score))

print("Part 1:",maze[end[0]][end[1]])

rev_trackers=deque([([end],1,maze[end[0]][end[1]])]) # position (l,c), head, score
rev_trackers.append(([end],2,maze[end[0]][end[1]]))

spot=set()
while rev_trackers:    
    path,head,score=rev_trackers.popleft()
    pos=path[-1]
    if pos==start: spot|=set(path)
    tracks=[p for p in possib_tracks(pos,head) if isinstance(maze[p[0][0]][p[0][1]],int) and maze[p[0][0]][p[0][1]]%1000==score%1000-1]
    
    for i in range(len(tracks)):
        t=tracks[i]
        new_score=maze[t[0][0]][t[0][1]]
        if new_score<score: rev_trackers.append((path+[t[0]],t[1],new_score))
        elif new_score>score and t[1]==head and len(tracks)>1: rev_trackers.append((path+[t[0]],t[1],new_score))
    
    if len(rev_trackers)==0:print(pos)
    
    # for p in possib_tracks(pos,head):
        
    #     if isinstance(maze[p[0][0]][p[0][1]],int) and maze[p[0][0]][p[0][1]]%1000==score%1000-1:
    #         rev_trackers.append((path+[p[0]],p[1],maze[p[0][0]][p[0][1]]))

print("Part 2:",len(spot))


# for l in range(num_l):
#     for c in range(num_c):
#         if isinstance(maze[l][c],int):maze[l][c]='.'
# for s in spot:
#     maze[s[0]][s[1]]='O'

# import numpy as np
# print(np.array(maze))

# #########################################################################

dir_map = {
    'u': {'v': (-1, 0), 't': ['l', 'r']}, 'd': {'v': (1, 0), 't': ['l', 'r']},
    'l': {'v': (0, -1), 't': ['u', 'd']}, 'r': {'v': (0, 1), 't': ['u', 'd']}
}

data = [list(l.strip('\n')) for l in lines]
part1 = 0
part2 = 0
m = len(data)
n = len(data[0])
maze = {}
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'S':
            maze[(i, j)] = 0
            start = (i, j)
        elif char == 'E':
            maze[(i, j)] = 1000000000000
            end = (i, j)
        else:
            maze[(i, j)] = char

future_moves, good_spots = deque(), set()

def dfs(loc, score, dir, reverse):
    if maze[loc] == '#' or (isinstance(maze[loc], int) and maze[loc] < score and not reverse):
        return
    if maze[loc] == '.' or maze[loc] > score:
        if reverse:
            return
        maze[loc] = score
    if reverse:
        good_spots.add(loc)
    for n_dr in [dir, *dir_map[dir]['t']]:
        n_loc = tuple([loc[i] + dir_map[n_dr]['v'][i] for i in [0, 1]])
        dif = (1001 if n_dr != dir else 1) * (-1 if reverse else 1)
        future_moves.append([n_loc, score + dif, n_dr, reverse])

future_moves.append([start, 0, 'r', False])
while future_moves:
    dfs(*future_moves.popleft())
future_moves.append([end, maze[end], 'd', True])
future_moves.append([end, maze[end], 'l', True])
while future_moves:
    dfs(*future_moves.popleft())
part1, part2 = maze[end], len(good_spots)

#     def traverse_maze(self):
#         future_moves, good_spots, maze = deque(), set(), self.maze

#         def dfs(loc, score, dir, reverse):
#             if maze[loc] == '#' or (isinstance(maze[loc], int) and
#                                     maze[loc] < score and not reverse):
#                 return
#             if maze[loc] == '.' or maze[loc] > score:
#                 if reverse:
#                     return
#                 maze[loc] = score
#             if reverse:
#                 good_spots.add(loc)
#             for n_dr in [dir, *dir_map[dir]['t']]:
#                 n_loc = tuple([loc[i] + dir_map[n_dr]['v'][i] for i in [0, 1]])
#                 dif = (1001 if n_dr != dir else 1) * (-1 if reverse else 1)
#                 future_moves.append([n_loc, score + dif, n_dr, reverse])

#         future_moves.append([self.start, 0, 'r', False])
#         while future_moves:
#             dfs(*future_moves.popleft())
#         future_moves.append([self.end, maze[self.end], 'd', True])
#         future_moves.append([self.end, maze[self.end], 'l', True])
#         while future_moves:
#             dfs(*future_moves.popleft())
#         self.part1, self.part2 = maze[self.end], len(good_spots)


# if __name__ == '__main__':
#     day16 = AdventDay16()
#     day16.traverse_maze()
#     print(day16.part1, day16.part2)