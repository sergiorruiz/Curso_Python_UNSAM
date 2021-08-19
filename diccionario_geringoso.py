# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:00:29 2021

@author: Sergio
"""

## Ejercicio 2.14

palabras = ['banana', 'manzana', 'mandarina']

diccionario = {}



def geringoso(palabras):
    
    capadepenapa = ''
    for c in palabras:
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
    return capadepenapa

for palabra in palabras:
    ge = geringoso(palabra)
    diccionario[palabra] = ge
    
print(diccionario)
    