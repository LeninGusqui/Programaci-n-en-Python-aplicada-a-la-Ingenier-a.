# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:25:44 2021

@author: Lenin Gusqui
"""

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
            
    

resultado= isPrime(3)
print(resultado)
    
  /num == 1 and num/1 == num:
        print("Es un numero primo")
    else:
        print("Es un numero no primo")
    
    
    #
# Su codigo Aqui
#

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
