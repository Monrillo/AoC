# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 16:33:29 2025

@author: castelf
"""

def read_param(param):
    if len(param)==5:
        opcode=int(param[-2:])
        p1=int(param[-3])
        p2=int(param[-4])
        p3=int(param[-5])
    elif len(param)==4:
        opcode=int(param[-2:])
        p1=int(param[-3])
        p2=int(param[-4])
        p3=0
    elif len(param)==3:
        opcode=int(param[-2:])
        p1=int(param[-3])
        p2=0
        p3=0
    else :
        opcode=int(param)
        p1=0
        p2=0
        p3=0
    return opcode,p1,p2,p3

def intcode(opcode,p1,p2,p3)