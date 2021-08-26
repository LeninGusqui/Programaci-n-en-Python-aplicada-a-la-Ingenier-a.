# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:41:56 2021

@author: Lenin Gusqui
"""

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2,num):
            if num % n == 0:
                return False
        return True
          
    

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
