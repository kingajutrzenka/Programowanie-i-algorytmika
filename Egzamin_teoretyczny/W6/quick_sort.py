#!/usr/bin/env python3

#quick sort - sortowanie szybkie
	
def quick_sort(lista, początek_przedziału, koniec_przedziału):
	if początek_przedziału >= koniec_przedziału: return 	 #jeśli lista ma 1 lub 0 elementów to kończymy
	i, j = początek_przedziału, koniec_przedziału #dodatkowe oznaczenia i to jest to coś co idzie lewo->prawo, a j na odwrót
	pivot = lista[(początek_przedziału+koniec_przedziału)//2] #ustalamy pivot na środek przedziału
	while i <= j: #bo gdy i>j to się mijają i jest koniec kroku
		while lista[i] < pivot: i +=1 #jeśli i jest mniejsze od pivota to niech zostanie i zwiększamy i
		while lista[j] > pivot: j -= 1 #jeśli j jest większe od pivota to zostaje i dodajemy do j 1
		if i <= j: #zamieniamy miejscami by było po dobrej stronie pivota
			lista[i], lista[j]  = lista[j], lista[i]
			i, j = i + 1, j - 1
	quick_sort(lista, początek_przedziału, j)
	quick_sort(lista, i, koniec_przedziału)

lista = [3,6,7,8,3,4,2,5,2,1,2,3,4,12,2]
quick_sort(lista, 0, len(lista)-1)
print(lista)
