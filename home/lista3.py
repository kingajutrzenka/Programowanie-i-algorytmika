#!/usr/bin/env python3

lista = []
from random import randint
n = 20
for i in range(1, n+1): 
	lista.append(randint(-100, 101))

"""Zadanie 1.
Wypisz wszystkie liczby parzyste."""

for _ in lista:
	if (_ % 2) == 0:
		print(_)
print(lista)

"""Zadanie 2.
Wypisz wszystkie liczby o nieparzystych indeksach na liście."""

for i in range(1, n+1):
	if (i % 2) != 0:
		print(lista[i])
print(lista)

"""Zadanie 3.
Wypisz zawartość listy w odwrotnej kolejności."""

print(lista[::-1])
print(lista)

"""Zadanie 4.
Znajdź wszystkie liczby o parzystej liczbie cyfr."""

for i in lista:
	if -100<i<-9 or 9<i<100:
		print(i)

"""Zadanie 5.
Utwórz nową listę z liczbami pierwszymi znajdującymi się na liście i wypisz zawartość tej listy."""

o = 0
list = []
for i in lista:
	for _ in range(1, i):
		if (i%_) == 0:
			o += 1
	if o == 1:
		list.append(i)
	o = 0
print(list)
print(lista)

"""Zadanie 6.
Utwórz nową listę z liczbami, które są pełnymi kwadratami liczby naturalnej i wypisz jej zawartość"""

import math

li=[]


for i in lista:
	if i >= 0:
		if math.sqrt(i) == int(math.sqrt(i)):
			li.append(i)
print(li)
print(lista)

"""Zadanie 7.
Znajdź długość najdłuższego podciągu niemalejącego na liście."""

o = 0 
lip = []
for i in range(0, n-1):
	if  lista[i]<= lista[i+1]:
		o += 1
	else: 
		lip.append(o)
		o = 0
lip.sort()
print(lip[-1])
print(lista)

"""Zadanie 8.
Wypisz wszystkie liczby, które zawierają się w przedziale [a, b], gdzie a, b całkowite, a<=b, są podawane z
klawiatury"""

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

for i in lista:
	if a<=i<=b:
		print(i)
print(lista"""

	
