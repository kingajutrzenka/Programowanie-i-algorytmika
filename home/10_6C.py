#!/usr/bin/env python3

"""Zadanie 10.

Zapoznaj się z problemem Flawiusza.

Danych jest n osób ustawionych w kole, ponumerowanych od 1 do n. Dana tez jest liczba
naturalna k. Podaj która osoba pozostanie w wyniku zastosowania wyliczanki o kroku k
poczynając od pierwszej osoby."""

# wersja rekurencyjna

"""k = int(input("podaj liczbę: "))
def J(n):
	if n == 1:
		return 1
	return((J(n-1) + k - 1) % n) + 1

print(J(10))"""

# wersja z zajęć

"""n = 10
k = 3
a = 0
lista = [i for i in range(1,n+1)]
stos =[]
while len(lista) > 1:
	for i in range(1,len(lista)-k):
		lista.pop(i*k - i)
		#print(lista)
		a = i*k - k
	#print(a)
	del stos[::]
	for x in range(a):
		stos.append(lista[x])
	#print(stos)
	del lista[:len(stos)-1]
	lista.extend(stos[:-1])
	print(lista)"""
	
#wersja ze zmianą pozycji

n = 10
k = 3

lista = [i for i in range(1, n+1)]
i = 0
#n = 0
while len(lista) > 1:
	"""n = n + 1
	print(f"Kolejka {n} ")
	print(i)
	print(len(lista))"""
	i = (i + k - 1) % len(lista)
	"""print(i)
	print(len(lista))"""
	lista.pop(i)                  

print(lista)
