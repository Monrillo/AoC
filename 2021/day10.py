# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 14:05:59 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day10.txt','r') as f: lines=f.readlines()

# lines=['[({(<(())[]>[[{[]{<()<>>',
# '[(()[<>])]({[<{<<[]>>(',
# '{([(<{}[<>[]}>{[]{[(<()>',
# '(((({<>}<{<{<>}{[]{[]{}',
# '[[<[([]))<([[{}[[()]]]',
# '[{[{({}]{}}([{[{{{}}([]',
# '{<[[]]>}<{[{[{[]{()[[[]',
# '[<(<(<(<{}))><([]([]()',
# '<{([([[(<>()){}]>(<<{{',
# '<{([{{}}[<[[[<>{}]]]>[]]']

incorrect={')':0,']':0,'>':0,'}':0}
scores=[]
for line in lines:
    chunks=''
    corr=True
    for c in list(line.strip('\n')):
        if c in ['(','[','<','{']:chunks+=c
        elif c==')' and chunks[-1]=='(':chunks=chunks[:-1]
        elif c==']' and chunks[-1]=='[':chunks=chunks[:-1]
        elif c=='>' and chunks[-1]=='<':chunks=chunks[:-1]
        elif c=='}' and chunks[-1]=='{':chunks=chunks[:-1]
        else: incorrect[c]+=1;corr=False;break
    if corr:
        score=0
        for el in chunks[::-1]:
            score*=5
            if el=='(':score+=1
            elif el=='[':score+=2
            elif el=='{':score+=3
            elif el=='<':score+=4
        scores.append(score)

points=3*incorrect[')']+57*incorrect[']']+1197*incorrect['}']+25137*incorrect['>']
print("Part 1:",points)

print("Part 2:",sorted(scores)[len(scores)//2])
