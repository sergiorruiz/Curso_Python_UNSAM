# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:43:50 2021

@author: Sergio
"""
## Ejercicio 2.9


import csv
file = open('../Data/camion.csv')
total = 0
rows = csv.reader(file)
headers = next(rows)
for row in rows:
    subTotal = int(row[1]) * float(row[2])
    total = total + subTotal
print(total)