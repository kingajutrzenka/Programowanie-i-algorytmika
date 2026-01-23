#!/usr/bin/env python3

#konwerter liczb całkowitych na rzymskie

rzym = {1000:"M", 900:"CM", 500:"D",
400: "CD", 100:"C", 90:"XC",
50: "L", 40: "XL", 10: "X", 9:"IX",
5:"V", 4:"IV", 1:"I"}

def Liczba_rzymska(zbiór, liczba_całkowita):
	for i in zbiór:
		while i <= liczba_całkowita:
			print(zbiór[i])
			liczba_całkowita -= i
			
Liczba_rzymska(rzym, 1025)

			
	
