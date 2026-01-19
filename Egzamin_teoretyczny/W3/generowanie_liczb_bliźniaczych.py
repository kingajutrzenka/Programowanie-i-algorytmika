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

