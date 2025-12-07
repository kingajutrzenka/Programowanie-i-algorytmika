#!/usr/bin/env python3

#Lista 1

"""Zadanie 9.

Dane: n c N 
Wynik: Odpowiedź na pytanie. czy n jest liczbą doskonałą?

def dosk(n):
	o = 0
	for i in range(1, n):
		if n%i == 0:
			o += i
	return o == n

print(dosk(8))"""
		
"""Zadanie 10.
Dane: n c N Wynik: Odpowiedź na pytanie. czy n jest liczbą pierwszą?

def pier(n):
	o = 0
	for i in range(1, n):
		if n%i == 0:
			o += 1
	return o == 1

print(pier(100))"""

"""Zadanie 11.

Dane: n, m c N 
Wynik: Odpowiedź na pytanie, czy n i m są liczbami zaprzyjaźnionymi?

def zaprzy(n,m):
	on = 0
	om = 0
	for i in range(1, n):
		if n%i == 0:
			on += i
	for i in range(1, m):
		if m%i == 0:
			om += i
	return on == m and om == n

print(zaprzy(1043096, 998104))"""
		
"""Zadanie 12.

Dane: n, m c N Wynik: Odpowiedź na pytanie, czy n i m są liczbami bliźniaczymi?

def pier(n):
	o = 0
	for i in range(1, n):
		if n%i == 0:
			o += 1
	return o == 1

def bli(n, m):
	if pier(n) == True and pier(m) == True:
		return n == m + 2 or m == n + 2
	else:
		return False

print(bli(11, 2))"""
			
"""Zadanie 13.
Dane: n c N Wynik: Faktoryzacja liczby n (rozkład na czynniki pierwsze)

def faktoryzacja(n):
	o = 2
	while n > 1:
		if n%o == 0:
			n /= o
			print(o)
			o = 2
		else:
			o += 1
	
faktoryzacja(111658888888888)"""

"""Zadanie 14.

Dane: n C N 
Wynik: S – suma odwrotności liczb naturalnych od 1 do n


def odw(n):
	s = 0
	for i in range(1, n+1):
		s += 1/int(i)
	return s

print(odw(2))"""

#Lista 4

"""Zadanie 2.

Mówimy, że liczba n jest podobna do cyfry p, jeśli obliczając sumę cyfr tej liczby , a potem
sumę cyfr powstałej sumy odpowiednio wiele razy, otrzymamy cyfrę p.

Na przykład: liczba 698799 jest podobna do cyfry 3, bo 6+9+8+7+9+9=48, 4+8= 12, 1+2 =3

Dana jest liczba naturalna n nie większa niż 2 000 000, podana z klawiatury. Napisz funkcję
obliczającą sumę cyfr liczby naturalnej i wykorzystaj ją w programie wskazującym, do jakiej
cyfry jest podobna liczba n.

n = 698799
def suma(n):
	n0 = n
	while n0>=10:
		n = list(str(n0))
		n0 = 0
		for i in n:
			n0 += int(i)
	return n0
	
print(suma(698799))"""

"""Zadanie 3.

Liczba pseudobinarna, to liczba, która w systemie dziesiętnym jest zapisana tylko za
pomocą cyfr 1 lub 0. Takimi liczbami są np. 1100 (tysiąc sto), 101 (sto jeden), ale nie są nimi
np. liczby 123, 1092.

a) Napisz funkcję, która zwróci wartość True, jeśli liczba jest pseudobinarna, a jeśli nie jest –
zwróci wartość False.

Użyj tej funkcji do znalezienia wszystkich liczb pseudobinarnych z zakresu od 1 do n
podanego z klawiatury


n = 100111
def pseudobin(n):
	o = 0
	n = list(str(n))
	for i in n:
		if int(i) == 1 or int(i) == 0:
			o += 1
	return o == len(n)

for k in range(1, n+1):
	if pseudobin(k) == True:
		print(k)"""

"""Zadanie 4.

Liczby lustrzane pierwsze to para liczb pierwszych, z których jedna powstaje przez
zapisanie cyfr dziesiętnych drugiej w odwrotnej kolejności. Przykładami takich liczb są: 13 i
31, 17 i 71, 37 i 73, 79 i 97, 107 i 701,...

Napisz funkcję sprawdzającą, czy liczba naturalna n jest liczbą pierwszą. Wykorzystaj tę
funkcję do napisania programu sprawdzającego, czy podana z klawiatury liczba naturalna m,
m<2000000, wraz z liczbą k powstałą z zapisania cyfr liczby m w odwrotnej kolejności, są
lustrzanymi liczbami pierwszymi.

def pier(n):
	o = 0
	for i in range(1, n):
		if n%i == 0:
			o+=1
	return o == 1

m = int(input("Podaj liczbe: "))
k = int(str(m)[::-1])

if pier(m) == True and pier(k) == True:
	print(f"Liczby {k} i {m} są lustrzanymi liczbami pierwszymi")
else:
	print(f"Liczby {k} i {m} nie są lustrzanymi liczbami pierwszymi")"""

"""Zadanie 5.

Liczba sympatyczna, to co najmniej dwucyfrowa liczba naturalna, w której każda cyfra jej
zapisu czytanego od lewej do prawej jest mniejsza od następnej. Na przykład liczba 1489 jest
sympatyczna, a liczba 1498 nie jest sympatyczna.

a) Napisz funkcję o nazwie sympatyczna, która zwraca wartość True, jeśli liczba jest
sympatyczna, a wartość False w przeciwnym wypadku.

b) Napisz program, który wykorzysta funkcję sympatyczna do sprawdzenia, czy liczba
podana z klawiatury jest sympatyczna i wypisze odpowiedni komunikat na ekranie.

c) Rozszerz program z punktu b) do programu, który wypisze na ekranie wszystkie
liczby sympatyczne z przedziału domkniętego [a,b], gdzie a i b są liczbami
naturalnymi podanymi przez użytkownika z klawiatury, takimi, że a<=b.


def sympatyczna(n):
	if n >= 10:
		n = list(str(n))
		for i in range (len(n)-1):
			if n[i] >= n[i+1]:
				return False
		return True
	return False

# print(sympatyczna(int(input("Podaj liczbe: "))))

a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))
for i in range(a, b+1):
	if sympatyczna(i) == True:
		print(i)"""

		
	

			
	
