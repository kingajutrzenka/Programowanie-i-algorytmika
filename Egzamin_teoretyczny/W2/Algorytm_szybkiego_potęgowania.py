#!/usr/bin/env python3

def szybkie_potęgowanie(x, m): # x to podstawa, m to wykładnik
	wynik = 1 #ustalamy liczbę która nam tworzy wynik na 1
	while m > 0: #dopóki wykładnik>0
		if m%2 == 1: #jesli wykładnik jest parzysty to pomnóż wynik razy podstawę
			wynik = wynik * x 
		x = x**2 # w każdym przypadku podnieś x do kwadratu i podziel całkowicie m przez 2 
		m = m // 2 
	return wynik #zwracamy wynik

print(szybkie_potęgowanie(5, 12))
print(5**12)

