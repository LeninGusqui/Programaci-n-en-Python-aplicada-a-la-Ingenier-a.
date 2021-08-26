# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:25:54 2021

@author: Lenin Gusqui
"""

"""Uso del while"""

contar=input("Ingrese el numero de veces a contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador=contador+1
    if contador>contar:
        break