# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:39:47 2021

@author: Lenin Gusqui
"""

hostnames=["R1", "R2", "R3", "S1", "S2"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)

print(hostnames[2])
print(hostnames[-1])

hostnames[0]="RTR1"
print(hostnames)

del hostnames[3]
print(hostnames)



