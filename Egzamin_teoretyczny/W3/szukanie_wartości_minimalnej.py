#!/usr/bin/env python3

#szukanie wartości minimalnej

import random

n = int(input("Podaj liczbę: "))
a = []
for i in range(n):
	a.append(random.randint(1, 270))
print(a)

def szukanie_wartości_minimalnej(n, a):
	min = a[0]
	i = 1
	while i<n:
		if a[i]<min:
			min=a[i]
		i += 1
	return min

print(szukanie_wartości_minimalnej(n, a))
