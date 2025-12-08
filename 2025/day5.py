# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 14:26:35 2025

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day5.txt','r') as f: lines=f.readlines()

# lines=['3-5',
# '10-14',
# '16-20',
# '12-18',
# '',
# '1',
# '5',
# '8',
# '11',
# '17',
# '32']

recipe=True
good=[]
ingredients=[]
for l in lines:
    if l.strip()=='':recipe=False
    elif recipe:
        a,b=l.strip().split('-')
        good.append([int(a),int(b)])
    else:
        ingredients.append(int(l.strip()))

good_ingredients=[i for i in ingredients if any(g[0]<=i<=g[1] for g in good)]

print("Part 1:",len(good_ingredients))

start=[g[0] for g in good]
end=[g[1] for g in good]

periods=[]
while len(start)>0:
    m=start.index(min(start))
    fin=end.pop(m)
    deb=start.pop(m)
    while start and fin>=min(start):
        m=start.index(min(start))
        start.pop(m)
        if end[m]>fin:fin=end.pop(m)
        else:end.pop(m)
    periods.append((deb,fin))

print("Part 2:",sum(p[1]-p[0]+1 for p in periods))


