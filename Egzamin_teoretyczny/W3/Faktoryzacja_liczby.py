#!/usr/bin/env python3

#Faktoryzacja po mojemu

def faktoryzacja(n):
	while n > 1:
		for i in range(2, int(n)+1):
			if n%i == 0:
				print(i)
				n /= i
				break

faktoryzacja(int(input("Podaj liczbę ")))

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
	
