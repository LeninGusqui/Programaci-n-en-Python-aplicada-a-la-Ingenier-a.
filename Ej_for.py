# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:20:10 2021

@author: Lenin Gusqui
"""

devices=["R1", "R2", "R3", "S1", "S2"]
print(devices)

for i in devices:
    
    if "R" in i:
        print(i)

switches=[]

for i in devices:
    if "S" in i:
        switches.append(i)

print(switches)
