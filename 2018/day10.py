# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 14:50:04 2025

@author: castelf
"""
import re

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2018\day10.txt','r') as f: lines=f.readlines()


re.findall(r'(-?\d+)', lines[5].strip())
