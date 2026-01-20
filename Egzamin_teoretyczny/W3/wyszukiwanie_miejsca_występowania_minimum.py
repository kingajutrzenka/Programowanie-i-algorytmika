#!/usr/bin/env python3

import random as r

a = []
for  i in range(15):
	a.append(r.randint(5, 180))
print(a)
	
def miejsce_minimum(lista):
	mm = 0
	for i in range(1, len(lista)):
		if lista[i] < lista[mm]:
			mm = i
	return mm
	

print(miejsce_minimum(a))
