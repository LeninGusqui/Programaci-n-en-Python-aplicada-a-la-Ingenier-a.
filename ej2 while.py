# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:35:16 2021

@author: Lenin Gusqui
"""

"""Uso del while"""

while True:
    contar=input("Ingrese el numero de veces a contar: ")
    if contar=='q' or contar=='quit':
        break
    contar=int(contar)
    contador=1
    while True:
        print(contador)
        contador=contador+1
        if contador>contar:
            break