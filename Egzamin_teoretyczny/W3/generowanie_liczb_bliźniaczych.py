#!/usr/bin/env python3

def naiwny_test_pierwszości(n):
	i = 2
	while i * i <= n:
		if n%i == 0:
			return False
		else:
			i += 1
	return True

zakres = int(input("Podaj zakres genrowania liczb bliźniaczych "))

for k in range(2, zakres-1):
	if naiwny_test_pierwszości(k) and naiwny_test_pierwszości(k+2) :
			print(f"Liczby bliźniacze {k}, {k+2}")

#Faktoryzacja zgodnie z algorytmem

def Faktoryzacja(n, lista): #podajemy liczbę n którą będziemy rozkładać na czynniki pierwsze oraz listę liczb pierwszych
	i = 0  #indeks listy liczb pierwszych
	czynniki = [] #lista z czynnikami które powstaną podczas rozkładu
	while n > 1: #działamy póki n>1
		if n%lista[i] == 0: #jeśli reszta z dzielenia przez liczbę o danym indeksie w liście liczb pierwszych == 0
			czynniki=czynniki + [lista[i]] #dodajemy nasz czynnik do listy
			n=n//lista[i] #dzielimy naszą liczbę n przez czynn
		else:
			i=i+1 #zwiększamy i, by móc brać kolejne liczby pierwsze
	return(czynniki)

pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23]
czynniki=Faktoryzacja(int(input("Podaj liczbę: ")), pierwsze)
print("Oto czynniki pierwsze XD: ")
for i in czynniki:
	print(i)
