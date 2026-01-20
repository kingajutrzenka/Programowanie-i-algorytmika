#!/usr/bin/env python3

import random as r

a = []
for  i in range(15):
	a.append(r.randint(5, 180))
print(a)

def sortowanie_przez_wstawianie(lista):
	for i in range(len(lista)):
		y = lista[i]
		k = i - 1
		while y<lista[k] and k>=0:
			lista[k+1] = lista[k]
			k -= 1
		lista[k+1]=y

sortowanie_przez_wstawianie(a)
print(a)
