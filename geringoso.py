# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:30:22 2021

@author: Sergio
"""

cadena = 'Sergio'
capadepenapa  = ''

for c in cadena.lower():
    capadepenapa = capadepenapa + c
    if c == 'a':
        capadepenapa = capadepenapa + 'pa'
    elif c == 'e':
        capadepenapa = capadepenapa + 'pe'
    elif c == 'i':
        capadepenapa = capadepenapa + 'pi'
    elif c == 'o':
        capadepenapa = capadepenapa + 'po'
    elif c == 'u':
        capadepenapa = capadepenapa + 'pu'
        
        
print(capadepenapa)



        

