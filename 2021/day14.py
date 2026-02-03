# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 13:45:36 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day14.txt','r') as f: lines=f.readlines()

# lines=['NNCB',
# '',
# 'CH -> B',
# 'HH -> N',
# 'CB -> H',
# 'NH -> C',
# 'HB -> C',
# 'HC -> B',
# 'HN -> C',
# 'NN -> C',
# 'BH -> H',
# 'NC -> B',
# 'NB -> B',
# 'BN -> B',
# 'BB -> N',
# 'BC -> B',
# 'CC -> N',
# 'CN -> C']

recipe={l.strip('\n').split(' -> ')[0]:[l.strip('\n').split(' -> ')[0][0]+l.strip('\n').split(' -> ')[1],\
                                        l.strip('\n').split(' -> ')[1]+l.strip('\n').split(' -> ')[0][1],\
                                            l.strip('\n').split(' -> ')[1]] for l in lines[2:]}
initial_pairs={l.strip('\n').split(' -> ')[0]:0 for l in lines[2:]}
letters={}
for p in initial_pairs:
    if p[0] not in letters:letters[p[0]]=0
    if p[1] not in letters:letters[p[1]]=0
for l in lines[0].strip('\n'):letters[l]+=1
    
pairs=initial_pairs.copy()
for i in range(len(lines[0].strip('\n'))-1):pairs[lines[0].strip('\n')[i:i+2]]=1

for step in range(10):
    new_pairs=initial_pairs.copy()
    for p in pairs:
        val=pairs[p]
        new_pairs[recipe[p][0]]+=val
        new_pairs[recipe[p][1]]+=val
        letters[recipe[p][2]]+=val
    pairs=new_pairs.copy()

print("Part 1:",max(letters.values())-min(letters.values()))

for step in range(30):
    new_pairs=initial_pairs.copy()
    for p in pairs:
        val=pairs[p]
        new_pairs[recipe[p][0]]+=val
        new_pairs[recipe[p][1]]+=val
        letters[recipe[p][2]]+=val
    pairs=new_pairs.copy()

print("Part 2:",max(letters.values())-min(letters.values()))


##########################################################################

from collections import Counter

def main():
    
    with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day14.txt') as f:
        data = f.read().splitlines()
    
    pairs = pairs_count(data[0])                              # get intial count of pairs from polymer string
    ltr_count = dict(Counter(i for i in data[0]))             # get intial polymer letter count
    pair_rules = [([i[0], i[1], i[6]]) for i in data[2:]]     # create list of pair insertion rules from data
    steps = 40                                                # set number of steps to iterate

    s = solve(steps, pairs, ltr_count, pair_rules)

    max_v = max(s.values())     # get max value
    min_v = min(s.values())     # get min value

    print(max_v - min_v)


def pairs_count(str):
    # returns a dict of pair counts from the intial polymer string

    pairs = {}

    for i in range(len(str) - 1):
        key = str[i] + str[i + 1]
        if key not in pairs:
            pairs[key] = 1
        else:
            pairs[key] += 1
    return pairs 


def solve(steps, pairs, ltr_count, pair_rules):
    # returns a dict of letter counts

    for step in range(steps):

        new_pairs = pairs.copy()

        for rule in pair_rules:
            key = rule[0] + rule[1]
            left_side = rule[0] + rule[2]
            right_side = rule[2] + rule[1]
            letter_to_insert = rule[2]

            new_pairs.setdefault(key, 0)
            new_pairs.setdefault(left_side, 0)
            new_pairs.setdefault(right_side, 0)

            if key in pairs:
                if pairs[key] > 0:   # essentially: if the pair exists, continue

                    val = pairs[key]   # set val to current value returned by pair

                    if letter_to_insert not in ltr_count:
                        ltr_count[letter_to_insert] = val
                    else:
                        ltr_count[letter_to_insert] += val
                    
                    new_pairs[key] -= val               # remove the center pairs
                    new_pairs[left_side] += val         # add the left-side pairs by val
                    new_pairs[right_side] += val        # add the right-side pairs by val
    
        pairs = new_pairs  # after 1 iteration let list of pairs = the new list of pairs
    return ltr_count


if __name__ == '__main__':
    main()