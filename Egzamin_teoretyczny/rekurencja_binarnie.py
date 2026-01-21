#!/usr/bin/env python3

#Zapis binarny rekurencja

def rekurencja_binarnie(n):
	if n>0:
		rekurencja_binarnie(n//2)
		print(n%2)

rekurencja_binarnie(65)
	
