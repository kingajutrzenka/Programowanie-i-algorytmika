#!/usr/bin/env python3

#sortowanie bąbelkowe

import random as r

a = []
for  i in range(15):
	a.append(r.randint(5, 180))
print(a)

def sortowanie_bąbelkowe(lista):
	for i in range(len(lista)-1):
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1]  = lista[i+1], lista[i]

sortowanie_bąbelkowe(a)
print(a)

	
