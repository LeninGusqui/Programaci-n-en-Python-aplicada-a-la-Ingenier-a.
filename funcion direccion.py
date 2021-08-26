# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:36:09 2021

@author: Lenin Gusqui
"""

def directions(ciudad, barrio, calle):
    print("Su dirección de referencia es: ")
    print("Su ciudad es: ", ciudad)
    print("El sector es: ", barrio)
    print("La calle de entrega es: ", calle)
    

ci=input("Ingrese la ciudad:")
ba=input("Ingrese el barrio de referencia:")
ca=input("Ingrese la calle para entrega de su pedido:")

directions(ci, ba, ca)
