#!/usr/bin/env python3

def zapis_binarny_iteracyjnie(n):
	lista = []
	while n>0:
		if n%2 == 0:
			lista.append(0)
		else:
			lista.append(1)
		n //= 2
	lista = lista[::-1]
	for i in lista:
		print(i)

zapis_binarny_iteracyjnie(42)		
