# -*- coding: utf-8 -*-
"""
Created on Fri Jan  9 09:51:14 2026

@author: castelf
"""

# import numpy as np

# with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day6.txt','r') as f: fish=np.array([int(x) for x in f.read().split(',')])

# fish=np.array([3,4,3,1,2])

# length=[len(fish)]

# for d in range(256):
#     fish-=1
#     fish=np.append(fish,np.full(len(np.where(fish==-1)[0]),8))
#     fish=np.where(fish==-1,6,fish)
#     #print("day ",d+1,": ",fish)
#     if (d+1)%7==0: print("day ",d+1,": ",len(fish))
#     length.append(len(fish))

# #print("Part 1:",len(fish))
# length=np.array(length)
# np.diff(length)
# np.diff(np.diff(length))




# Solution from MaxMaxoff

def calculate_grow(initial_state, days):
    new_state = {}
    if days > 0:
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            if i == 0 and initial_state.get(i):
                new_state[8] = initial_state[i]
                if new_state.get(6):
                    new_state[6] += initial_state[i]
                else:
                    new_state[6] = initial_state[i]
            elif i > 0 and initial_state.get(i):
                new_state[i - 1] = initial_state[i]
        return calculate_grow(new_state, days - 1)
    else:
        return initial_state


def main():
    # days = 18
    # days = 80
    days = 256
    initial_state = {}
    result_state = {}
    with open("C:\\Users\castelf\Documents\GitHub\AoC\\2021\day6.txt") as f:
        initial_list = list(map(int, f.readline().split(',')))
    for item in initial_list:
        if initial_state.get(item):
            initial_state[item] += 1
        else:
            initial_state[item] = 1
    qty = 0
    result_state = calculate_grow(initial_state, days)
    for key in result_state:
        qty += result_state[key]
    print(qty)


if __name__ == "__main__":
    main()

