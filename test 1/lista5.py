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
nim imion.

with open ("imiona.txt", "r") as imie, open("panie.txt", "w") as panie, open("panowie.txt", "w") as panowie:
	imie = imie.read()
	imie = imie.strip().split()
	k =  0
	m = 0
	for i in imie:
		if i[-1] == "a":
			panie.write(i + ", ")
			k += 1
		else:
			panowie.write(i + ", ")
			m += 1
	panie.write("\n" + str(k))
	panowie.write("\n" + str(m))"""
	
"""Zadanie 2.

Dane są dwa pliki tekstowe: gracz1.txt i gracz2.txt. Każdy z nich zawiera taka
samą ilość liczb naturalnych z przedziału [0,100], są to liczby wylosowane odpowiednio
dla gracza 1. i gracza 2. (pliki można przygotować wcześniej wpisując do nich liczby z
klawiatury). W każdej rundzie gry są porównywane liczby z odpowiadających sobie wierszy
w tych dwóch plikach. Dany gracz wygrywa rundę, jeśli jego liczba jest większa, przegrywa,
gdy jego liczba jest mniejsza, a gdy liczby są równe, wynikiem jest remis. Całą grę wygrywa
gracz z większą liczbą wygranych rund.
Napisz program, który wypisze na ekranie numer gracza, który wygrał całą grę

p1 = 0
p2 = 0
with open("g1.txt", "r") as g1, open ("g2.txt", "r") as g2:
	for l1, l2 in zip(g1, g2):
		if int(l1) > int(l2):
			p1 += 1
		elif int(l1) < int(l2):
			p2 += 1
	if p1 > p2:
		print("wygrał gracz 1")
	elif p1 < p2:
		print("wygrał gracz 2")
	else:
		print("jest remis")"""
		
"""Zadanie 3.

Dane są dwa pliki tekstowe: dane1.txt i dane2.txt. Każdy z nich zawiera ciąg liczb
naturalnych z przedziału [0,100] uporządkowanych niemalejąco. Każda liczba zapisana
jest w oddzielnym wierszu pliku.
Utwórz plik wynik.txt zawierający scalone ciągi z plików dane1.txt i dane2.txt.
Uporządkowane liczby zapisz w jednym wierszu po spacji.

with open("d1.txt", "r") as d1, open("d2.txt", "r") as d2, open("wynik.txt", "w") as w:
	l = []
	for l1, l2 in zip(d1, d2):
		if int(l1) >= int(l2):
			l.append(int(l2))
			l.append(int(l1))
		else:
			l.append(int(l1))
			l.append(int(l2))
	for i in l:
		w.write(str(i) + " ")"""

"""Zadanie 4.

W każdym wierszu pliku dane.txt znajduje się jedna liczba nie większa niż 500. Mówimy,
że dane są dobre do testowania, jeśli wszystkie liczby w pliku są unikatowe, czyli każda
liczba występuje tylko raz. Napisz program, który oczyści z powtórzeń dane pobrane z pliku
dane.txt i oczyszczone dane zapisze w pliku testuj.txt po jednej w każdym wierszu,
przygotowując w ten sposób dane dobre do testowania. Kolejność liczb w pliku wynikowym
nie ma znaczenia.
Wskazówka: Zastosuj zliczanie.

with open("d.txt", "r") as d, open("testuj.txt", "w") as t:
	l = []
	for i in d:
		i = i.strip()
		if i not in l:
			l.append(i)
	for k in l:
		t.write(str(k) + "\n")"""

"""Zadanie 5.

W edytorach tekstów popularna jest funkcjonalność pozwalająca na zamianę wszystkich
wystąpień pewnego tekstu na nowy. Zasymuluj działanie takiej zamiany.

Dany jest plik tekstowy tekst.txt oraz dwa łańcuchy s i t. Napisz program, który
zamieni wszystkie wystąpienia łańcucha s w tym pliku na łańcuch t.

with open ("tekst.txt", "r") as tekst: 
	tekst = tekst.read()
	tekst = tekst.replace("Napisz program", "Nie pisz programu")
with open ("tekst.txt", "w") as t:
	t.write(tekst)"""
	
	
	

