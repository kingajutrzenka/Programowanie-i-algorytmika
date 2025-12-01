#!/usr/bin/env python3

#Zadanie 4
#B7,8

"""Zadanie 1.

Napisz program z funkcją rekurencyjną, która daną liczbę naturalną n zapisaną w systemie
dziesiętnym zapisuje w systemie o podstawie k, gdzie 2<=k<=10. Liczby n i k podawane są z
klawiatury.

Przykład: Dane: n=234, k=8 Wynik: 352

Wskazówka: Zmodyfikuj funkcję rekurencyjną podaną na wykładzie, zapisującą liczbę dziesiętna w
systemie dwójkowym."""

bin=[]

def bin_rek(n, m):
    if n>0:
        bin_rek(n//m, m)
        bin.append(n%m)
    return bin    
    
print(bin_rek(int(input("Podaj liczbę: ")), int(input("Podaj liczbę: "))))

"""Zadanie 2.

Dane jest n naturalne podawane z klawiatury. Napisz program z funkcjami iteracyjną i rekurencyjną
obliczającymi wartość n!, gdzie n jest liczba naturalną."""

n = int(input("Podaj liczbę: "))

def sili(k):
	a = 1
	if k == 0:
		return 1
	while k > 0:
		a = a * k
		k = k - 1
	return a
	
print(sili(n))

def silr(k):
	if k == 0:
		return 1
	return k * silr(k-1)
	
print(silr(n))
"""Zadanie 3.

Napisz program z funkcją iteracyjną i rekurencyjną obliczającą z definicji wartość potęgi n
k, dla n i k naturalnych."""

n = 0
k = 5
a = 1
for i in range(1, k+1):
	a = a*n

print(a)

def pot(s, k):
	if k == 0:
		return 1
	return s * pot(s, k-1)
	
print(pot(5, 2))

"""Zadanie 4.

Zastosuj algorytm szybkiego podnoszenia do potęgi w wersji rekurencyjnej do obliczenia wartości
potęgi nk, dla n i k naturalnych."""

def spot(x, n):
	if n == 0:
		return 1
	if n % 2 != 0:
		return x * spot(x, n-1)
	return spot(x, n/2)**2

print(spot(3, 4))


"""Zadanie 5.

Wykorzystaj jedną z napisanych wcześniej funkcji do obliczenia wartości sumy: 1^1+2^2+3^3+ …+ n^n dla
n naturalnego podawanego z klawiatury."""

def pott(k):
	a = 1
	if k == 1:
		return 1
	return k**k + pott(k-1)
	
print(pott(3))

"""Zadanie 6.
Przeczytaj w Wikipedii o trójkącie Pascala. Napisz program z funkcją rekurencyjną obliczającą
wartość symbolu Newtona dla liczb 0<=k<=n, gdzie"""

def Pas(n, k):
	if k == 0 or k == n:
		return 1
	return Pas(n-1, k-1) + Pas(n-1, k)
	
print(Pas(5, 2))

"""Zadanie 7.

Słowo Fibonacciego powstaje zgodnie z następującą definicją...

Napisz program z funkcją rekurencyjną obliczającą wartość n-tego słowa Fibonacciego. Posortuj to
słowo alfabetycznie. Wypisz liczbę wystąpień każdej z liter w tym słowie."""

def Fib(n):
	if n == 0:
		return 'b'
	elif n == 1:
		return 'a'
	return Fib(n-1) + Fib(n-2)
print(Fib(5))
