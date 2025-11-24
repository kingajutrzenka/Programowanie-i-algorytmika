#!/usr/bin/env python3

# PRZYPOMNIJ ZADANIE 7 i 8
# naucz się kuwa tej sumy!!!
# zapamiętaj czym jest liczba sympatyczna


"""Zadanie 1.
Jaś zapomniał, na czym polega dzielenie z resztą. Dlatego, aby sprawdzić, czy liczba
naturalna n dzieli się przez 3 korzysta z innej własności. Sumuje cyfry tej liczby, potem cyfry
powstałej sumy i powtarza to sumowanie, aż uzyska jedną z cyfr 3, 6 lub 9.

Napisz funkcję, która oblicza sumę cyfr danej liczby naturalnej.

Użyj tej funkcji w programie, aby metodą Jasia sprawdzić, czy dana liczba naturalna jest
podzielna przez 3. Twój program powinien odpowiedzieć TAK, jeśli n dzieli się przez 3,
natomiast NIE jeśli n nie dzieli się przez 3.

Przykład: Dla liczby n=23451 Jaś oblicza: 2+3+4+5+1=15 i znów 1+5=6. Stąd wie, że liczba
n jest podzielna przez 3."""

n = 99999999999999999999999999999999999999
def suma_cyfr(n):
	suma = 0
	for cyfra in str(n):
		suma += int(cyfra)
	return suma


while n>9:
	n = suma_cyfr(n)
	print(n)
if n == 3 or n  == 6  or n == 9:
	print("TAK")
else:
	print("NIE")
	
"""Zadanie 2.

Mówimy, że liczba n jest podobna do cyfry p, jeśli obliczając sumę cyfr tej liczby , a potem
sumę cyfr powstałej sumy odpowiednio wiele razy, otrzymamy cyfrę p.

Na przykład: liczba 698799 jest podobna do cyfry 3, bo 6+9+8+7+9+9=48, 4+8= 12, 1+2 =3

Dana jest liczba naturalna n nie większa niż 2 000 000, podana z klawiatury. Napisz funkcję
obliczającą sumę cyfr liczby naturalnej i wykorzystaj ją w programie wskazującym, do jakiej
cyfry jest podobna liczba n."""
	
n = 789
n0 = n
def suma_cyfr(n):
	suma = 0
	for cyfra in str(n):
		suma += int(cyfra)
	return suma


while n>9:
	n = suma_cyfr(n)
	print(n)
print(f"liczba {n0} jest podobna do liczby {n}")

"""Zadanie 3.

Liczba pseudobinarna, to liczba, która w systemie dziesiętnym jest zapisana tylko za
pomocą cyfr 1 lub 0. Takimi liczbami są np. 1100 (tysiąc sto), 101 (sto jeden), ale nie są nimi
np. liczby 123, 1092.

a) Napisz funkcję, która zwróci wartość True, jeśli liczba jest pseudobinarna, a jeśli nie jest –
zwróci wartość False.

Użyj tej funkcji do znalezienia wszystkich liczb pseudobinarnych z zakresu od 1 do n
podanego z klawiatury"""

n = 300

def spr(n):
	o = 0
	for cyfra in str(n):
		if int(cyfra) == 0 or int(cyfra) == 1:
			o += 1
	return o == len(str(n))

print(spr(n))

for i in range(1, n+1):
	if spr(i) == True:
		print(i)

"""Zadanie 4.

Liczby lustrzane pierwsze to para liczb pierwszych, z których jedna powstaje przez
zapisanie cyfr dziesiętnych drugiej w odwrotnej kolejności. Przykładami takich liczb są: 13 i
31, 17 i 71, 37 i 73, 79 i 97, 107 i 701,...

Napisz funkcję sprawdzającą, czy liczba naturalna n jest liczbą pierwszą. Wykorzystaj tę
funkcję do napisania programu sprawdzającego, czy podana z klawiatury liczba naturalna m,
m<2000000, wraz z liczbą k powstałą z zapisania cyfr liczby m w odwrotnej kolejności, są
lustrzanymi liczbami pierwszymi."""


n = 163
def pierwsza(n):
	o = 0
	for i in range(1, n):
		if (n%i) == 0:
			o += 1
	return o == 1

print(pierwsza(n))
if pierwsza(n) == True:
	print(n)
	print((str(n))[::-1])
	
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
naturalnymi podanymi przez użytkownika z klawiatury, takimi, że a<=b"""

#a

def sym(n):
	o = 0
	if n>= 10:
		for i in range(0, len(str(n))-1):
			if not int((str(n))[i+1]) > int((str(n))[i]):
				o += 1
		return o == 0	
	return n>= 10

#b

n = int(input("Podaj liczbę: "))
print(sym(n))

#c 

a = int(input("Podaj liczbę : "))
b = int(input("Podaj liczbę : "))

for i in range(a, b+1):
	if sym(i) == True:
		print(i)

"""Zadanie 6.

Napisz dwie funkcje iteracyjne, jedną obliczającą NWD dwóch liczb naturalnych, drugą
obliczającą NWW dwóch liczb naturalnych. Wykorzystaj te funkcje do rozwiązania zadania:

Dane są cztery liczby naturalne (bez zera) a, b, c, d nie większe niż 100, podawane z
klawiatury, a i b to odpowiednio licznik i mianownik jednego ułamka, c i d to odpowiednio
licznik i mianownik drugiego ułamka.

Napisz program, który sprowadza ułamki a/b i c/d do wspólnego mianownika.

Przykład: Dla 1/3 i 1/2 wynikiem jest np. 2/6 i 3/6"""



def NWD(n, m):
	if n == 0:
		return m
	elif m == 0:
		return n
	while n != m:
		if n > m:
			n -= m
		else:
			m -= n
	return n

def NWW(n, m):
	return (n * m) // NWD(n, m)

a = int(input("Podaj liczbę : "))
b = int(input("Podaj liczbę : "))
c = int(input("Podaj liczbę : "))
d = int(input("Podaj liczbę : "))

c0 = c
d0 = d

y = NWW(b, d)

print(f"ułamek a/b = {(y//b)*a} / {y}")
print(f"ułamek c/d = {(y//d)*c} / {y}")

"""Zadanie 7.

Wykorzystaj tę funkcję NWD obliczającą największy wspólny dzielnik dwóch liczb
naturalnych do rozwiązania zadania:

Dane: n liczb naturalnych nie większych niż 100, podawanych z klawiatury.

Wynik: Program obliczający NWD wszystkich podanych liczb naturalnych. Wykorzystaj jak
najmniejsza liczbę zmiennych.

Wskazówka: Skorzystaj z własności, że NWD(a,b,c)=NWD(NWD(a,b),c)"""


n = 3
x = int(input("Podaj cyfre: "))
for _ in range(1, n): # jest n, a nie n +1, bo już jeden n jest przed
	x = NWD(x, int(input("Podaj cyfre: "))) # x przechodzi do kolejnego
print(x)
"""Zadanie 8.

Punkt kratowy, to punkt którego współrzędne w układzie kartezjańskim są całkowite.

Danych jest n wierzchołków pewnego wielokąta, będących punktami kratowymi. Oblicz, ile
punktów kratowych zawiera się w całym obwodzie tego wielokąta.

Wskazówka: Aby uzyskać rozwiązanie całego zadania, rozpatrz najpierw pojedyncze
krawędzie wielokąta."""

w = [(0,7), (7,0), (7,-3), (-3,-3), (-3, 0)]
suma = 0
for i in range(len(w)):
	(x1, y1) = w[i] 
	(x2, y2) = w[(i+1) % len(w)] 
	dx = abs(x2 - x1) 
	dy = abs(y2 - y1) 
	suma += NWD(dx,dy) 
print(suma)

"""Zadanie 9.

Aby zagrać w totolotka musimy wybrać losowo 6 liczb z 49. Chcielibyśmy wybrać te losowe
liczby w dokładnie sześciu losowaniach, mając pewność, że kolejno losowana liczba nie
powtórzy się. Napisz program, który tak postąpi.

Wskazówka: Jednym ze sposobów jest utworzenie tablicy 49 elementowej z kolejnymi
liczbami od 1 do 49, zamiana pierwszy raz wylosowanej liczby z liczbą z ostatnią w tablicy,
drugiej z przedostatnią, itd. i za każdym razem skracanie zakresu losowania o jeden. Napisz
program, który wylosuje w ten sposób sześć różnych liczb."""

opcje = list(range(1, 50))

import random

random.shuffle(opcje)

print(opcje[0:6])

"""Zadanie 10.

Danych jest n liczb wylosowanych z przedziału [a, b], gdzie n jest liczbą naturalną mniejszą
od 20, a i b są liczbami naturalnymi nie większymi niż 100. Dana jest również liczba
naturalna k <= n. Napisz program, który wypisze k-tą w kolejności od końca największą
liczbę wśród wylosowanych liczb.

Przykład:

Dane: n=10 , a=2, b=25, wylosowane liczby: 21, 10, 14, 15, 14, 13, 4, 23, 2, 3, k=4
Wynik: 14"""

# mój

n = 10
k = 3

a = 20
b = 100

import random

li = []
for i in range(1, n+1):
	li.append(random.randint(20, 100))
li.sort()
print(li)
print(li[-k])

	
	





	
	


			
		



		
