#!/usr/bin/env python3

# sortowanie przez zliczanie 

lista = [3, 5, 3, 1, 4, 2, 2, 1, 9, 1, 0, 7]
długość_listy = len(lista)

	#zliczamy wyrazy
def sortowanie_przez_zliczanie(n, ciąg):
	lista_pomocnicza = []
	for i in range(10):
		lista_pomocnicza.append(0)
	for m in range(n):
		lista_pomocnicza[ciąg[m]] += 1
	
	#wstawiamy spowrotem do listy głównej
	k = 0
	for n in range(len(lista_pomocnicza)):
		for p in range(lista_pomocnicza[n]):
				ciąg[k] = n
				k += 1

sortowanie_przez_zliczanie(długość_listy, lista)
print(lista)
