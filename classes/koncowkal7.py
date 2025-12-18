#!/usr/bin/env python3

#zdjęcie grafu w tel

"""Zadanie 8.
W pierwszym wierszu pliku dane.in zapisana jest liczba wierzchołków i po spacji liczba
łuków digrafu acyklicznego D. W kolejnych m wierszach zapisane są po dwie liczby
oddzielone spacją wyznaczające łuki digrafu, para i j oznacza, że łuk prowadzi od i do j.
Wyświetl na ekranie topologiczną kolejność wierzchołków digrafu D. Zastosuj algorytm
omówiony na wykładzie."""

#PRZYGOTUJ SIĘ W DOMU!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""Zadanie 9.

Dany jest graf o n wierzchołkach i m krawędziach (n, m<10)

a) Wyświetl na ekranie macierz sąsiedztwa tego grafu oraz listę sąsiadów. Skorzystaj z
przykładu na podanego na wykładzie i porównaj wyniki. Dla obydwu reprezentacji:
b) oblicz stopnie wierzchołów tego grafu.
c) znajdź wierzchołek o najwyższym stopniu, jeśli jest takich więcej, wypisz wszystkie."""

#with open ("dane.in", "r") as d

graf = [[0, 1, 0, 0, 1], \
		[1, 0, 1, 1, 0], \
		[0, 1, 0, 0, 1], \
		[0, 1, 0, 0, 1], \
		[1, 0, 1, 1, 0]]

print(graf)

ls={0:[1, 4],\
	1:[0, 2, 3], \
	2:[1, 4], \
	3:[1, 4], \
	4:[0, 2, 3]}
	
print(ls)

stopnie = dict()
for numer, lista in ls.items():
	stopnie[numer] = len(lista)
print(stopnie)

i = 0
for wiersz in graf:
	stopnie[i] = sum(wiersz)
	i += 1

a = max(stopnie.values())
for i in stopnie:
	if stopnie[i] == a:
		print(i)

"""Zadanie 10.
Napisz dwie funkcje, dla sprawdzenia, czy graf o n wierzchołkach i m krawędziach:
a) ma cykl Eulera (eulerowskie)
b) ma drogę Eulera

Cykl Eulera: Przechodzi przez wszystkie krawędzie raz i wraca do startu. (Wszystkie wierzchołki mają stopień parzysty).

Ścieżka Eulera: Przechodzi przez wszystkie krawędzie raz, ale kończy się w innym miejscu niż zaczęła.
(Dokładnie dwa wierzchołki mają stopień nieparzysty – są to start i meta)."""

#a
def cykl(graf):
	for wiersz in graf:
		if sum(wiersz)%2 == 1:
			return False
	return True
graf = [[0, 1, 0, 0, 1], \
		[1, 0, 1, 1, 0], \
		[0, 1, 0, 0, 1], \
		[0, 1, 0, 0, 1], \
		[1, 0, 1, 1, 0]]

print(cykl(graf))

def cykl(graf):
	o = 0
	for wiersz in graf:
		if sum(wiersz)%2 == 1:
			o += 1
	if o == 2:
		return True

print(cykl(graf))


