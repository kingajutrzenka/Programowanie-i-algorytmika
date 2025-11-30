#!/usr/bin/env python3

"""Zadanie 1.

Polskie imiona żeńskie zawsze kończą się literą a, natomiast imiona męskie, literą różną od
litery a.

Dany jest plik tekstowy imiona.txt, w którym znajdują się imiona żeńskie wpisane po
spacji. Napisz funkcję sprawdzająca, czy dane imię jest imieniem żeńskim. Wykorzystaj tę
funkcję w programie, który wszystkie imiona żeńskie z tego pliku umieści w pliku
panie.txt, a wszystkie imiona męskie umieści w pliku panowie.txt. Imiona powinny
być oddzielone przecinkiem i znakiem spacji oraz w kolejności zgodnej z kolejnością w pliku
imiona.txt.

Dodatkowo, w ostatnim wierszu każdego pliku wynikowego zapisz liczbę umieszczonych w
nim imion."""

def literkaa(n):
	return str(n)[-1] == 'a'
with open('imiona.txt', 'r') as i, open('panie.txt', 'w') as pa, open('panowie.txt', 'w') as px:
	lpa = 0
	lpx = 0
	i = i.read() 
	ino = i.strip().split()
	for a in ino :
		if literkaa(a) == True:
			pa.write(a + ", ")
			lpa += 1
		else:
			px.write(a + ", ")
			lpx += 1
	pa.write("\n" + str(lpa))
	px.write("\n" + str(lpx))
	
"""Zadanie 2.

Dane są dwa pliki tekstowe: gracz1.txt i gracz2.txt. Każdy z nich zawiera taka 
samą ilość liczb naturalnych z przedziału [0,100], są to liczby wylosowane odpowiednio
dla gracza 1. i gracza 2. (pliki można przygotować wcześniej wpisując do nich liczby z
klawiatury). W każdej rundzie gry są porównywane liczby z odpowiadających sobie wierszy
w tych dwóch plikach. Dany gracz wygrywa rundę, jeśli jego liczba jest większa, przegrywa,
gdy jego liczba jest mniejsza, a gdy liczby są równe, wynikiem jest remis. Całą grę wygrywa
gracz z większą liczbą wygranych rund.

Napisz program, który wypisze na ekranie numer gracza, który wygrał całą grę."""
	
with open("gracz1.txt", "r") as g1, open("gracz2.txt", "r") as g2:
	gw1l = 0
	gw2l = 0
	for linia1, linia2 in zip(g1, g2):
		if int(linia1) > int(linia2):
			gw1l += 1
		elif int(linia1) < int(linia2):
			gw2l += 1
	print(gw1l)
	print(gw2l)
			
"""Zadanie 3.

Dane są dwa pliki tekstowe: dane1.txt i dane2.txt. Każdy z nich zawiera ciąg liczb
naturalnych z przedziału [0,100] uporządkowanych niemalejąco. Każda liczba zapisana
jest w oddzielnym wierszu pliku.

Utwórz plik wynik.txt zawierający scalone ciągi z plików dane1.txt i dane2.txt.

Uporządkowane liczby zapisz w jednym wierszu po spacji."""

with open ("dane1.txt", "r") as d1, open("dane2.txt", "r") as d2, open("wynik.txt", "w") as w:
	for linia1, linia2 in zip(d1, d2):
		if int(linia1) < int(linia2):
			w.write(linia1.strip() + " " + linia2.strip() + " ")
		else:
			w.write(linia2.strip() + " " + linia1.strip() + " ")

"""Zadanie 4.

W każdym wierszu pliku dane.txt znajduje się jedna liczba nie większa niż 500. Mówimy,
że dane są dobre do testowania, jeśli wszystkie liczby w pliku są unikatowe, czyli każda
liczba występuje tylko raz. Napisz program, który oczyści z powtórzeń dane pobrane z pliku
dane.txt i oczyszczone dane zapisze w pliku testuj.txt po jednej w każdym wierszu,
przygotowując w ten sposób dane dobre do testowania. Kolejność liczb w pliku wynikowym
nie ma znaczenia.

Wskazówka: Zastosuj zliczanie."""

lista = []
with open("dane.txt", "r") as d, open("testuj.txt", "w") as t:
	for linia in d:
		if not int(linia) in lista:
			lista.append(int(linia))
	for _ in lista:
		t.write(str(_) + "\n")

"""Zadanie 5.

W edytorach tekstów popularna jest funkcjonalność pozwalająca na zamianę wszystkich
wystąpień pewnego tekstu na nowy. Zasymuluj działanie takiej zamiany.

Dany jest plik tekstowy tekst.txt oraz dwa łańcuchy s i t. Napisz program, który
zamieni wszystkie wystąpienia łańcucha s w tym pliku na łańcuch t."""


with open ("tekst.txt", "r") as t:
	li = []
	for i in t:
		i = i.strip()
		i = str(i).replace("kot", "pies")
		li.append(i)
with open ("tekst.txt", "w") as t:
	for i in li:
		t.write(i)
		
		
	
		
		
	
