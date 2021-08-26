# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:21:38 2021

@author: Lenin Gusqui
"""

acl = int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("Es una ACL estandar")
elif acl>=100 and acl<=199:
    print("Es una ACL extendida")
else:
    print("El # ingresado no es de una ACL!")