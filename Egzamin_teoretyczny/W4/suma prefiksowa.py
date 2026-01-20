#!/usr/bin/env python3

lista = [1, 3, 2, 2, 1, 1, 0, 1, 0, 1]

def suma_prefiksowa(z):
	pref = []
	for i in range(len(z)+1):
		pref.append(0)
	for m in range(len(z)):
		pref[m+1] += pref[m] + z[m]
	p = int(input("Podaj początek przedziału: "))
	k = int(input("Podaj koniec przedziału: "))
	return pref[k+1] - pref[p]

print(suma_prefiksowa(lista))
	
