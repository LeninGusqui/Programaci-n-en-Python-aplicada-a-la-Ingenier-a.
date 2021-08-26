# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:03:36 2021

@author: Lenin Gusqui
"""

ipaddress = {"R1":"10.0.0.1", "R2":"10.2.2.1", "R3":"10.3.3.1"}
print(type(ipaddress))
print(ipaddress)
print(ipaddress['R3'])
ipaddress["S1"]="10.3.2.1"
print(ipaddress)
print("R2" in ipaddress)
print("S2" in ipaddress)