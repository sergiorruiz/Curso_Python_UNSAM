# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:55:55 2021

@author: Sergio
"""

## Ejercicio 2.7

def buscar_precio(fruta):
    file = open('../Data/precios.csv', 'rt')
    fruta
    with file as f:
        for line in f:
            row = line.split(',')
            if fruta in line:
                return print(f'El precio de la {row[0]} es: {row[1]}')
        else:
            return print(f'{fruta} no esta')
            

buscar_precio('Naranja')
    