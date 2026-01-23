#!/usr/bin/env python3

#własności słownika

sporty = {"bieganie" : "tani", "jazda konna" : "drogi" ,  "spacerowanie" : "łatwy" , "łyżwiarstwo": "trudny"}

def szukamy(słownik, szukany):
	for i in słownik:
		if słownik[i] == szukany:
			return i
	return "brak"

print(szukamy(sporty, input("Podaj cechę sportu: ")))
