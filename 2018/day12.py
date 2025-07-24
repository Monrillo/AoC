# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 14:38:17 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day12.txt','r') as f: lines=f.readlines()

lines=['initial state: #..#.#..##......###...###',
'',
'...## => #',
'..#.. => #',
'.#... => #',
'.#.#. => #',
'.#.## => #',
'.##.. => #',
'.#### => #',
'#.#.# => #',
'#.### => #',
'##.#. => #',
'##.## => #',
'###.. => #',
'###.# => #',
'####. => #']

# Initialisation
state='.....'+lines[0][15:]+'.............'

[i for i,n in enumerate(state) if n =='#']

result=state.count('#')
print('0 : '+state+' ',result)

# Recipe
mod=[l.split(' => ')[0] for l in lines[2:]]
res=[l.split(' => ')[1] for l in lines[2:]]

for j in range(1,21):
    new_state='.'*len(state)
    for i,(a,b,c,d,e) in enumerate(zip(state,state[1:],state[2:],state[3:],state[4:])):
        pat=''.join((a,b,c,d,e))
        if pat in mod: new_state=new_state[:i+2]+res[mod.index(pat)]+new_state[i+3:]
    state=new_state
    result+=state.count('#')
    print(j,' : '+state+' ',result)

print(result)






#############################################################

def nextg(cur, recipe):
  start = min(cur)
  end = max(cur)
  x = set()

  for i in range(start - 3, end + 4):
    pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
    if pat in recipe:
      x.add(i)

  return x

def viz(cur):
  print (''.join('#' if i in cur else '.' for i in range(-5, 120)))

#with open('day12test.txt') as f:
with open('day12input.txt') as f:
  lines = [l.rstrip('\n') for l in f]
  print (lines)

  init = lines[0][len('initial state: '):]
  recipe = set()
  for l in lines[2:]:
    if l[-1] == '#':  # I forgot this line the first time around.
      recipe.add(l[:5]) 

  cur = set(i for i, c in enumerate(init) if c == '#')

  # Part 1:
  for i in range(20):
    cur = nextg(cur, recipe)
  print (sum(cur))

  # Part 2:
  ls = 0
  # viz(cur)
  for i in range(2000):
    cur = nextg(cur, recipe)
    # viz(cur)
    s = sum(cur)
    print (i, s, s - ls)
    ls = s
  print (sum(cur))