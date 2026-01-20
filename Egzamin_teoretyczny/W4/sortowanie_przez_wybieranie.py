#!/usr/bin/env python3

#!/usr/bin/env python3

import random as r

a = []
for  i in range(15):
	a.append(r.randint(5, 180))
print(a)

def sortowanie_przez_wybieranie(lista):
	i = 0 #miejsce w którym mamy najdalszy posortowany element
	for i in range(len(lista)-1): #jak w algorytmie lista kroków n-1
		min = i
		for k in range(i+1, len(lista)): #klasyczne szukanie minimum, ale od miejsca po posortowanych elementach
				if lista[k]<lista[min]:
					min=k
		lista[i], lista[min] = lista[min], lista[i] #zamiana miejsc

sortowanie_przez_wybieranie(a)
print(a)
