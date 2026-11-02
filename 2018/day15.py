# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 17:07:34 2025

@author: castelf
"""

matrix = [list(line.strip()) for line in open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day15.txt').readlines()]

goblins = []
elves = []

class Creature:
  def __init__(self, race, position):
      self.race = race
      self.position = position
      self.alive = True
      self.hp = 200
      self.power = 3

matrix=[
'#######',
'#E..G.#',
'#...#.#',
'#.G.#G#',
'#######']

for l in range(len(matrix)):
    for c in range(len(matrix[l])):
        if matrix[l][c] == 'E': elves.append(Creature('elf', (l,c)))
        elif matrix[l][c] == 'G': goblins.append(Creature('goblin', (l,c)))






lines=[
'#######',
'#.G...#',
'#...EG#',
'#.#.#G#',
'#..G#E#',
'#.....#', 
'#######']

