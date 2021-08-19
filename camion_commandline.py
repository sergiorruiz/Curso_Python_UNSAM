# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:26:30 2021

@author: Sergio
"""

##Ejercicio 2.10

import csv
import sys

def costo_camion(nombre_archivo):
    file = open(nombre_archivo)
    total = 0
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        subTotal = int(row[1]) * float(row[2])
        total = total + subTotal
    return total
    
if len(sys.argv) == 2:
   nombre_archivo = sys.argv[1]
else:
   nombre_archivo = '../Data/camion.csv'
        
costo = costo_camion(nombre_archivo)
print('Costo Total: ', costo)
        
        