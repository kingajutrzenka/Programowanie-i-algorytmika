#!/usr/bin/env python3

"""Zadanie 4.
Polskie imiona żeńskie kończą się literą ‘a’. Napisz program, który uzupełni początek listu do
Ciebie na podstawie Twojego imienia: Szanowna Pani, Szanowny Panie."""

imie = str(input("Podaj imie: "))

if imie[-1] == "a":
	print(f"Szanowna Pani {imie}")
else:
	print(f"Szanowny Panie {imie}")

"""Zadanie 5.
Dane są: a, b c N. Oblicz reszta z dzielenia a przez b:
a) wykorzystując działanie %
b) bez wykorzystania działania %."""
# a
a = 256
b = 3
print(a%b)
#b
a = 256
b = 3

if a>=b:
	while a >= b:
		a -= b
	print(a)
else:
    print(a)
	
"""Zadanie 6.
Dane są: a, b c N. Oblicz część całkowita z dzielenia a przez b.
a) wykorzystując działanie //
b) bez wykorzystania działania //."""

# a
a = 5
b = 30
print(a//b)

# b
licznik = 0
if a >= 0:
	while a >= b:
		a -= b
		licznik += 1
	print(licznik)
else: 
	print(a)

"""Zadanie 7.
Dana jest liczba naturalna n:

#b wypisz na ekranie cyfry liczby n w kolejności od najmniej znaczącej:"""

n= 5
while n > 0:
	print(str(n)[-1])
	n = n/10
	n = int(n)
	
# c oblicz sumę cyfr liczby n:

n = 120
w = 0
while n > 0:
	o = str(n)[-1]
	o = int(o)
	w += o
	n = n/10
	n = int(n)
print(w)

# d zapisz liczbę n w systemie dwójkowym

n = 3914
lista = []
while n>0:
	lista.append(n%2)
	n = n//2
print(lista[::-1])


# e zapisz liczbę n w dowolnym systemie o podstawie 2<=p<=10

n=3914
l = int(input("Podaj liczbę 2<=p<=10: "))
lista = []
while n>0:
	lista.append(n%l)
	n = n//l
print(lista[::-1])

# f zapisz liczbę n w systemie dwójkowym

n = 3914
lista = []
while n>0:
	lista.append(n%2)
	n = n//2
print(len(lista))

