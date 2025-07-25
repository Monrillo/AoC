# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 14:38:17 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day12.txt','r') as f: lines=f.readlines()

# lines=['initial state: #..#.#..##......###...###',
# '',
# '...## => #',
# '..#.. => #',
# '.#... => #',
# '.#.#. => #',
# '.#.## => #',
# '.##.. => #',
# '.#### => #',
# '#.#.# => #',
# '#.### => #',
# '##.#. => #',
# '##.## => #',
# '###.. => #',
# '###.# => #',
# '####. => #']

# Initialisation
state=lines[0].strip()[15:]
plant=set(i for i,n in enumerate(state) if n =='#')
print('0',sum(plant))

# Recipe
mod=[l.split(' => ')[0] for l in lines[2:] if l.strip().split(' => ')[1]=='#']

# Computation of next generation
def nextgen(p,m):
    st=min(p)
    end=max(p)
    np=set()
    for i in range(st-5,end+5):
        pat=''.join('#' if i+k in p else '.' for k in [-2,-1,0,1,2])
        if pat in m: np.add(i)
    return np

# Part 1
for j in range(1,21):
    plant=nextgen(plant,mod)
    print(j,sum(plant))

# Part 2

# for j in range(1,201):
#     plant=nextgen(plant,mod)
#     print(j,sum(plant))

# 23 every generation, since generation 162
#  4958 at generation 200

part2=(5e10-200)*23+4958
print(part2)

