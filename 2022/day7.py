# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:43:50 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2022\day7.txt','r') as f: lines=f.readlines()

# lines=['$ cd /',
# '$ ls',
# 'dir a',
# '14848514 b.txt',
# '8504156 c.dat',
# 'dir d',
# '$ cd a',
# '$ ls',
# 'dir e',
# '29116 f',
# '2557 g',
# '62596 h.lst',
# '$ cd e',
# '$ ls',
# '584 i',
# '$ cd ..',
# '$ cd ..',
# '$ cd d',
# '$ ls',
# '4060174 j',
# '8033020 d.log',
# '5626152 d.ext',
# '7214296 k']

# Where we are
path = []
# Graph
folders = {}

# List of forlder paths   
folders_list=[]

# Starting with root / folder
folders['/']={}
folders_list.append(['/'])

# implementing graph
for line in lines:
    cmd=line.strip('\n').split(' ')
    if cmd[0]=='$':
        if cmd[1]=='cd' and cmd[2]!='..':
            path.append(cmd[2])
        elif cmd[1]=='cd' and cmd[2]=='..':
            path.pop(-1)
    else:
        dic=folders
        for p in path: dic=dic[p]
        if cmd[0]=='dir':
            dic[cmd[1]]={}
            folders_list.append(path+[cmd[1]])
        else: dic[cmd[1]]=int(cmd[0])

#function for computing score
def folder_size(fol):
    size=0
    for f in fol:
        if isinstance(fol[f], int): size+=fol[f]
        elif isinstance(fol[f], dict): size+=folder_size(fol[f])
    return size

# Sizes of all folders
sizes=[]

for path in folders_list:
    # Positionning at the folder
    dic=folders
    for p in path: dic=dic[p]
    sizes.append(folder_size(dic))
    
print("Part 1:",sum(s for s in sizes if s<=100000))

# The need of free up size
free=sizes[0]-40000000

print("Part 2:",sorted([s for s in sizes if s>=free])[0])

