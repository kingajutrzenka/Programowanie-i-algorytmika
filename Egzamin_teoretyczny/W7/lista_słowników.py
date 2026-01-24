#!/usr/bin/env python3

przeciwnik 1={ 'kolor': 'czarny', 'liczba' : 100, 'punkty' :10}
przeciwnik 2={ 'kolor': 'zielony', 'liczba' : 50, 'punkty' :20}
przeciwnik 3={ 'kolor': 'żółty', 'liczba' :20, 'punkty' : 50}

#lista słowników
przeciwnicy=[przeciwnik_1,przeciwnik_2, przeciwnik_3]

twoje_punkty=0
with open ('pliki/zestrzeleni.txt') as z:
	for x in z:
		k=x.rstrip ()
		for y in przeciwnicy:
			if y['kolor' ] == k:
				y['liczba' ] -= 1
				twoje_punkty+=y [ 'punkty' ]
print ('Zdobyłeś ' , twoje_punkty, 'punktów. ' )
print ('Masz jeszcze do zestrzelenia:')
for y in przeciwnicy:
	print (y [ 'kolor' ], y['liczba' ] )
