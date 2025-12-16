# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 13:34:21 2025

@author: castelf
"""

import numpy as np
import itertools as it

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day10.txt','r') as f: lines=f.readlines()

# lines=['[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
# '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
# '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']

def light_out(length,button,clic):
    lights=np.ones(length,dtype=int)*-1
    for c in clic:lights[button[c]]*=-1
    return lights

resultat=0
for line in lines:
    elems=line.strip().split(' ')
    l_good=[-1 if x=='.' else 1 for x in list(elems[0])[1:-1]]
    inter=[[int(x) for x in elems[i][1:-1].split(',')] for i in range(1,len(elems)-1)]
    
    res=None
    for i in range(1,len(inter)+1):
        for prop in it.permutations(range(len(inter)), i):
            if np.array_equiv(light_out(len(l_good),inter,prop), l_good): res=i;break
        else: continue
        break
    resultat+=res
            
print("Part 1:",resultat)

# from collections import deque

# InputList = []
# with open('C:\\Users\castelf\Documents\GitHub\AoC\\2025\day10.txt', "r") as data:
#     for t in data:
#         Line = t.strip().split(" ")
#         FinalState = Line[0][1:-1]
#         Joltages = Line[-1][1:-1]
#         Buttons = tuple(Line[1:-1])
#         InputList.append((FinalState, Buttons, Joltages))

# LightsDict = {"#": "1", ".": "0", "1": "#", "0": ","}
# SwitchDict = {"#": ".", ".": "#"}

# def AnAPressIsAnAPress(Goal, Buttons):
#     LenLights = len(Goal)
#     BlankLights = ""
#     for u in range(LenLights):
#         BlankLights += "."
#     ImperialFrontier = deque()
#     ImperialCore = set()
#     ImperialFrontier.append((0,BlankLights))

#     while ImperialFrontier:
#         Presses, Lights = ImperialFrontier.popleft()

#         for B in Buttons:
#             NewLights = list(Lights)
#             for Bu in B:
#                 NewLights[Bu] = SwitchDict[NewLights[Bu]]
#             NewLights = "".join(NewLights)
#             if NewLights == Goal:
#                 return Presses+1
#             elif NewLights in ImperialCore:
#                 continue
#             ImperialFrontier.append((Presses+1,NewLights))
#             ImperialCore.add(NewLights)

# #@cache This entire function is deprecated but remains in the code for posterity
# def YouCantSayItsOnlyHalfDeprecated(Goal, Buttons):
#     #LowestJoltage = 10000
#     #for v, t in enumerate(Goal):
#     #    if t < LowestJoltage and t > 0:
#     #        LowestJoltage = t
#     #        LowestJoltPosition = v
    

#     MaxPressesPerButton = []
#     LengthofLongestButton = 0
#     MaxValueofLongestButton = 1000
#     for v, B in enumerate(Buttons):
#         MaxValue = max(Goal)
#         for t in B:
#             if Goal[t] < MaxValue:
#                 MaxValue = Goal[t]
#         MaxPressesPerButton.append(MaxValue)
#         ButtonLength = len(B)
#         if ButtonLength > LengthofLongestButton:
#             LengthofLongestButton = ButtonLength
#             MaxValueofLongestButton = MaxValue
#             LongestButton = v
#         elif ButtonLength == LengthofLongestButton and MaxValue < MaxValueofLongestButton:
#             MaxValueofLongestButton = MaxValue
#             LongestButton = v
    
#     for t in reversed(range(MaxValueofLongestButton+1)):
#         if len(Buttons) >= 12 and t > 0:
#             continue
#         GoalList = list(Goal)
#         ButtonsList2 = list(Buttons)
#         for y in ButtonsList2[LongestButton]:
#             GoalList[y] -= t
#         if len(set(GoalList)) == 1 and GoalList[0] == 0:
#             return t
        
#         MaxPressesPerButton[LongestButton] = 0
#         for y in reversed(range(len(MaxPressesPerButton))):
#             if MaxPressesPerButton[y] == 0:
#                 del ButtonsList2[y]
#         NewButtons = tuple((ButtonsList2))
#         RemainingSwitchSet = set()
#         for U in ButtonsList2:
#             for x in U:
#                 RemainingSwitchSet.add(x)
#         for v, i in enumerate(GoalList):
#             if i > 0 and v not in RemainingSwitchSet:
#                 return None
#         if len(ButtonsList2) == 1 and sum(GoalList) % len(ButtonsList2[0]) != 0:
#             continue


#         if ButtonsList2:
#             NewGoal = tuple(GoalList)
#             NextValues = YouCantSayItsOnlyHalf(NewGoal, NewButtons)
#             if NextValues != None:
#                 return NextValues + t
    
#     return None

# #@cache #I needed help for this one
# def YouCantSayItsOnlyHalf(Goal, Buttons):
#     NumButtons = len(Buttons)
#     ValidInitialButtonPresses = []
#     for r in range(2**NumButtons):
#         NewBinary = bin(r)[2:]
#         while len(NewBinary) < NumButtons:
#             NewBinary = "0" + NewBinary
#         ButtonsPressed = 0
#         NewGoal = list(Goal)
#         Negatives = False
#         for v, t in enumerate(NewBinary):
#             if t == "1":
#                 ButtonsPressed += 1
#                 for l in Buttons[v]:
#                     NewGoal[l] -= 1
#                     if NewGoal[l] < 0:
#                         Negatives = True
#                         break
#         if Negatives:
#             continue
#         Valid = True
#         for v, f in enumerate(NewGoal):
#             if f % 2 == 1:
#                 Valid = False
#                 break
#             NewGoal[v] = f//2
#         if Valid:
#             NewGoal = tuple(NewGoal)
#             ValidInitialButtonPresses.append((ButtonsPressed, NewGoal))
    
#     if not(ValidInitialButtonPresses):
#         return 100000000
    
#     LowestButtonPresses = 1000000000
#     for B, NewGoal in ValidInitialButtonPresses:
#         if sum(NewGoal) == 0:
#             if B < LowestButtonPresses:
#                 LowestButtonPresses = B
#             continue
#         NewSum = B + 2*YouCantSayItsOnlyHalf(NewGoal, Buttons)
#         if NewSum < LowestButtonPresses:
#             LowestButtonPresses = NewSum
    
#     return LowestButtonPresses
            




# Part1Answer = 0
# Part2Answer = 0
# Count = 0
# for Goal, Buttons, Joltages in InputList:
#     ButtonsList = []
#     for B in Buttons:
#         Trimmed = B[1:-1]
#         Trimmed = Trimmed.split(",")
#         ButtonTuple = []
#         for t in Trimmed:
#             ButtonTuple.append(int(t))
#         ButtonsList.append(tuple(ButtonTuple))
#     PassButtons = tuple(ButtonsList)
#     Joltages = tuple(map(int, Joltages.split(",")))

#     Part1Answer += AnAPressIsAnAPress(Goal, PassButtons)
#     #if len(PassButtons) <= 9:
#     #    P2 = YouCantSayItsOnlyHalfDepricated(Joltages, PassButtons)
#     #    #print(P2)
#     #    Part2Answer += P2
#     #else:
#     P2 = YouCantSayItsOnlyHalf(Joltages, PassButtons)
#     Part2Answer += P2
#     print("BigNumber", P2)
#     Count += 1
#     print(Count)


# print(f"{Part1Answer = }")
# print(f"{Part2Answer = }")