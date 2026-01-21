#!/usr/bin/env python3

def Fibonacci_iteracyjnie(n):
	F1 = 1 #poprzednia liczba
	F2 = 1 #bierząca liczba 
	for i in range(n-2):
		F2, F1 = F1+F2, F2
	return F2

print(Fibonacci_iteracyjnie(100))
	

