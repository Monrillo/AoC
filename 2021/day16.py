# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:39:55 2026

@author: castelf
"""

with open('C:\\Users\castelf\Documents\GitHub\AoC\\2021\day16.txt','r') as f: bits=f.read()

lines=['0 = 0000',
'1 = 0001',
'2 = 0010',
'3 = 0011',
'4 = 0100',
'5 = 0101',
'6 = 0110',
'7 = 0111',
'8 = 1000',
'9 = 1001',
'A = 1010',
'B = 1011',
'C = 1100',
'D = 1101',
'E = 1110',
'F = 1111']

hexa={l.split(' = ')[0]:l.split(' = ')[1] for l in lines}
#bins={l.split(' = ')[1]:l.split(' = ')[0] for l in lines}

#bits='D2FE28'
#bits='38006F45291200'
#bits='EE00D40C823060'
bits='8A004A801A8002F478'
#bits='620080001611562C8802118E34'
#bits='C0015000016115A2E0802F182340'
#bits='A0016C880162017C3686B18A3D4780'

binary_bits=''.join([hexa[i] for i in bits])

binary_bits=binary_bits[18+43:18+86]

version=int(binary_bits[:3],2)
type_ID=int(binary_bits[3:6],2)

if type_ID==4:
    contents=[]
    for i in range(1,len(binary_bits[6:])+1):
        if i%5==0:contents.append(binary_bits[6:][i-5:i])
    
    if all(c[0]=='1' for c in contents[:-1]) and contents[-1][0]=='0':
        message=''.join([c[1:] for c in contents])
    
    number=int(message,2)

else:
    length=binary_bits[6]
    if length=='0':
        label=binary_bits[7:22]
    elif length=='1':
        label=binary_bits[7:18]
        len(binary_bits[18:])//int(label,2)

int(label,2)
len(binary_bits[22:])
binary_bits=binary_bits[22:49]

def traitement(bi):
    version=int(bi[:3],2)
    type_ID=int(bi[3:6],2)
    
    if type_ID==4:
        return version
    else:
        length=bi[6]
        if length=='0':
            label=bi[7:22]
            return version+traitement(bi[22:22+int(label,2)])
        elif length=='1':
            label=bi[7:18]
            num=int(label,2)
            return version+traitement(bi[18:])