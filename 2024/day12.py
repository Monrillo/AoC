# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:47:55 2026

@author: castelf
"""
import numpy as np
#from tqdm import tqdm

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2024\day12.txt','r') as f: lines=f.readlines()

# lines=['RRRRIICCFF',
# 'RRRRIICCCF',
# 'VVRRRCCFFF',
# 'VVRCCCJFFF',
# 'VVVVCJJCFE',
# 'VVIVCCJJEE',
# 'VVIIICJJEE',
# 'MIIIIIJJEE',
# 'MIIISIJEEE',
# 'MMMISSJEEE']

lines=['AAAAAA',
'AAABBA',
'AAABBA',
'ABBAAA',
'ABBAAA',
'AAAAAA']

field=np.array([list(l.strip('\n')) for l in lines])

def step(l,c,d):
    if d=='s':
        if c>0 and l+1<field.shape[0] and field[l+1,c-1]=='.': return ['tr',l+1,c-1]
        elif l+1<field.shape[0] and field[l+1,c]=='.': return [l+1,c]
        else: return ['tl']
    elif d=='e':
        if l+1<field.shape[0] and c+1<field.shape[1] and field[l+1,c+1]=='.': return ['tr',l+1,c+1]
        elif c+1<field.shape[1] and field[l,c+1]=='.': return [l,c+1]
        else: return ['tl']
    elif d=='n':
        if l>0 and c+1<field.shape[1] and field[l-1,c+1]=='.': return ['tr',l-1,c+1]
        elif l>0 and field[l-1,c]=='.': return [l-1,c]
        else: return ['tl']
    elif d=='w':
        if l>0 and c>0 and field[l-1,c-1]=='.': return ['tr',l-1,c-1]
        elif c>0 and field[l,c-1]=='.': return [l,c-1]
        else: return ['tl']

result_1=0
result_2=0
for li in range(field.shape[0]):
    for co in range(field.shape[1]):
        pos=(li,co)
        if field[pos]!='.' and field[pos]!='':
            seed=field[pos]
            path=[pos]
            while len(path)>0:
                tracker=path.pop(0)
                field[tracker]='.'
                if tracker[0]-1>=0 and field[tracker[0]-1,tracker[1]]==seed and not (tracker[0]-1,tracker[1]) in path:path.append((tracker[0]-1,tracker[1]))
                if tracker[0]+1<field.shape[0] and field[tracker[0]+1,tracker[1]]==seed and not (tracker[0]+1,tracker[1]) in path:path.append((tracker[0]+1,tracker[1]))
                if tracker[1]-1>=0 and field[tracker[0],tracker[1]-1]==seed and not (tracker[0],tracker[1]-1) in path:path.append((tracker[0],tracker[1]-1))
                if tracker[1]+1<field.shape[1] and field[tracker[0],tracker[1]+1]==seed and not (tracker[0],tracker[1]+1) in path:path.append((tracker[0],tracker[1]+1))
            
            area=len(np.where(field=='.')[0])
            perimeter=0
            sides=0
            
            dr=['s','w','n','e']
            state=pos[0],pos[1],dr[0]
            initial_state=state
            
            while True:
                if step(*state)[0]=='tr':
                    dr=dr[1:]+dr[:1]
                    sides+=1
                    state=step(*state)[1],step(*state)[2],dr[0]
                elif step(*state)[0]=='tl':
                    dr=dr[-1:]+dr[:-1]
                    sides+=1
                    state=state[0],state[1],dr[0]
                else:
                    state=step(*state)[0],step(*state)[1],dr[0]
                perimeter+=1
                
                if state==initial_state: break
            
            print("perimeter :",perimeter)
            print("sides :",sides)
            
            result_1+=area*perimeter
            result_2+=area*sides
            field[field=='.']=''

print("Part 1:",result_1)

print("Part 2:",result_2)
