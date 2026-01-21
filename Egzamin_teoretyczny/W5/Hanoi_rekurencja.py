#!/usr/bin/env python3


def przenieś(n, skąd, dokąd, pom):
	licznik = 0 #moja własna zmienna sprawdzająca
	if n == 1:
		print("Przenieś dysk z", skąd, "na", dokąd)
	else:
		przenieś(n-1, skąd, pom, dokąd)
		przenieś(1, skąd, dokąd, pom)
		przenieś(n-1, pom, dokąd, skąd)

def Hanoi_rekurecja(n):
	przenieś(n, "A", "B", "C")
    

Hanoi_rekurecja(5)

