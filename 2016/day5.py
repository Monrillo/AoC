# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:26:16 2025

@author: castelf
"""
import hashlib
import numpy as np

n=0
pwd=''
new_pwd=np.zeros(8,dtype=str)
cpt=0
while cpt<8:
    string='reyedfim'+str(n)
    hash = hashlib.md5(string.encode()).hexdigest()
    if hash[:5]=='00000':
        if len(pwd)<8:
            pwd+=hash[5]
        try:
            pos=int(hash[5])
            if new_pwd[pos]=='':
                new_pwd[pos]=hash[6]
                cpt+=1
        except:
            pass
    n+=1

print(pwd)
print(''.join(new_pwd))

# from tqdm import tqdm
# import time

# for i in tqdm(range(1000)):
#     time.sleep(0.01)

# import hashlib
# import random
# index = 0
# password = '________'
# while 1:
#     m = hashlib.md5()
#     m.update(('reyedfim'+str(index)).encode('utf-8'))
#     hex_m = m.hexdigest()
#     if hex_m[0:5] == '00000':
#         password_pos = int(hex_m[5], 16)
#         if password_pos < 8:
#             password_dig = int(hex_m[6], 16)
#             if password[password_pos] == '_':
#                 password = password[:password_pos] + hex(password_dig)[-1] + password[password_pos + 1:]
#     if index % 30000 == 0:
#         for char in password:
#             if char == '_':
#                 print(str(random.random())[-1], end='')
#             else:
#                 print(char, end='')
#         print('\r', end='')
#     index += 1