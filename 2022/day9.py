# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:26:57 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day9.txt','r') as f: lines=f.readlines()

# lines=['R 4',
# 'U 4',
# 'L 3',
# 'D 1',
# 'R 4',
# 'D 1',
# 'L 5',
# 'R 2']

# lines=['R 5',
# 'U 8',
# 'L 8',
# 'D 3',
# 'R 17',
# 'D 10',
# 'L 25',
# 'U 20']

snake=[(0,0)]*10
t1_path=set()
t9_path=set()
t1_path.add(snake[1])
t9_path.add(snake[9])

def touch(h,t):
    hx,hy=h
    tx,ty=t
    dx=hx-tx
    dy=hy-ty
    if dx*dy>=2 and dx>0: return (tx+1,ty+1)
    elif dx*dy>=2 and dx<0: return (tx-1,ty-1)
    elif dx*dy<=-2 and dx>0: return (tx+1,ty-1)
    elif dx*dy<=-2 and dx<0: return (tx-1,ty+1)
    elif dx==2 and dy==0: return (tx+1,ty)
    elif dx==-2 and dy==0: return (tx-1,ty)
    elif dx==0 and dy==2: return (tx,ty+1)
    elif dx==0 and dy==-2: return (tx,ty-1)
    else: return t

for line in lines:
    d,n=line.strip('\n').split(' ')
    for _ in range(int(n)):
        if d=='U':snake[0]=(snake[0][0]+1,snake[0][1])
        elif d=='D':snake[0]=(snake[0][0]-1,snake[0][1])
        elif d=='R':snake[0]=(snake[0][0],snake[0][1]+1)
        elif d=='L':snake[0]=(snake[0][0],snake[0][1]-1)
        for i in range(1,10):
            snake[i]=touch(snake[i-1],snake[i])
        t1_path.add(snake[1])
        t9_path.add(snake[9])
        
print("Part 1:",len(t1_path))

print("Part 2:",len(t9_path))

