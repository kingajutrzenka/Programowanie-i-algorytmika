#!/usr/bin/env python3

# Graf – macierz sąsiedztwa – implementacja: lista list

graf = []
# funkcja która wypisuje nasz graf w "ładnej formie"

def wypisz_graf(graf):
	for i in graf:
		print(i)

#funkcja która tworzy macierz zerową

def macierz_zerowa(graf, n): #n - liczba wieszkołków
	for i in range(n):
		lista = n*[0] #tworzenie listy która zawiera tyle zer ile jest wierzchołków
		graf.append(lista) #dodajemy listę do grafu

#dodajemy krawędzie do grafu

def krawędzie_graf(graf, m): #m - liczba krawędzi
	for i in range(m):
		początek_krawędzi = int(input("Podaj numer wierzchołka który będzie początkiem krawędzi :"))
		koniec_krawędzi = int(input("Podaj numer wierzchołka który będzie końcem krawędzi :"))
		graf[początek_krawędzi][koniec_krawędzi] = 1
		#gdyby graf był nie skierowany to:  graf[koniec_krawędzi][początek_krawędzi] = 1

"""graf = [
		0 1  2
    0[0, 1, 0],  # wiersz 0: z wierzchołka 0 idzie krawędź do 1 (nie do 0, nie do 2)
    1[0, 0, 1],  # wiersz 1: z wierzchołka 1 idzie krawędź do 2
    2[0, 0, 0]   # wiersz 2: z wierzchołka 2 nie idzie żadna krawędź
]"""

macierz_zerowa(graf, 3)
krawędzie_graf(graf, 2)
wypisz_graf(graf)
